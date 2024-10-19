import dataclasses
import threading
import time
from typing import Optional, Union, Tuple

from . import globals
from .config_evaluation import _ConfigEvaluation
from .diagnostics import Context, Diagnostics, Marker
from .dynamic_config import DynamicConfig
from .evaluation_details import DataSource
from .evaluator import _Evaluator
from .feature_gate import FeatureGate
from .layer import Layer
from .sdk_configs import _SDK_Configs
from .spec_store import _SpecStore, EntityType
from .statsig_context import InitContext
from .statsig_error_boundary import _StatsigErrorBoundary
from .statsig_errors import StatsigNameError, StatsigRuntimeError, StatsigValueError
from .statsig_event import StatsigEvent
from .statsig_logger import _StatsigLogger
from .statsig_metadata import _StatsigMetadata
from .statsig_network import _StatsigNetwork
from .statsig_options import StatsigOptions
from .statsig_user import StatsigUser
from .ttl_set import TTLSet
from .utils import HashingAlgorithm, compute_dedupe_key_for_gate, is_hash_in_sampling_rate, \
    compute_dedupe_key_for_config, compute_dedupe_key_for_layer
from .version import __version__

RULESETS_SYNC_INTERVAL = 10
IDLISTS_SYNC_INTERVAL = 60


class InitializeDetails:
    duration: int
    source: str
    init_success: bool
    store_populated: bool
    error: Optional[Exception]

    def __init__(self, duration: int, source: str, init_success: bool, store_populated: bool,
                 error: Optional[Exception]):
        self.duration = duration
        self.source = source
        self.init_success = init_success
        self.error = error
        self.store_populated = store_populated


class StatsigServer:
    _initialized: bool

    _errorBoundary: _StatsigErrorBoundary

    _options: StatsigOptions
    __shutdown_event: threading.Event
    __statsig_metadata: dict
    _network: _StatsigNetwork
    _logger: _StatsigLogger
    _spec_store: _SpecStore
    _evaluator: _Evaluator

    def __init__(self) -> None:
        self._initialized = False

        self._errorBoundary = _StatsigErrorBoundary()

    def is_initialized(self):
        return self._initialized

    def initialize(self, sdkKey: str, options: Optional[StatsigOptions] = None) -> InitializeDetails:
        if self._initialized:
            globals.logger.info("Statsig is already initialized.")
            return InitializeDetails(0, self.get_init_source(), True, self.is_store_populated(), None)

        if sdkKey is None or not sdkKey.startswith("secret-"):
            raise StatsigValueError(
                "Invalid key provided. You must use a Server Secret Key from the Statsig console."
            )

        if options is None or not isinstance(options, StatsigOptions):
            options = StatsigOptions()

        environment_tier = options.get_sdk_environment_tier() or 'unknown'
        globals.logger.info(
            f"Initializing Statsig SDK (v{__version__}) instance. "
            f"Current environment tier: {environment_tier}."
        )

        init_details = self._initialize_impl(sdkKey, options)
        self._post_init_logging(options, init_details)

        return init_details

    def _post_init_logging(self, options: StatsigOptions, init_details: InitializeDetails):
        if options.local_mode:
            if init_details.init_success:
                globals.logger.info(
                    "Statsig SDK instance initialized in local mode. No data will be fetched from the Statsig servers.")
            else:
                globals.logger.error("Statsig SDK instance failed to initialize in local mode.")
            return

        if init_details.init_success:
            if init_details.store_populated:
                globals.logger.info(
                    f"Statsig SDK instance initialized successfully with data from {init_details.source}")
            else:
                globals.logger.error(
                    "Statsig SDK instance initialized, but config store is not populated. The SDK is using default values for evaluation.")
        else:
            globals.logger.error("Statsig SDK instance Initialized failed!")

    def _initialize_impl(self, sdk_key: str, options: Optional[StatsigOptions]):
        threw_error = False
        try:
            init_context = InitContext()
            diagnostics = Diagnostics()
            diagnostics.add_marker(Marker().overall().start())

            self._errorBoundary.set_api_key(sdk_key)
            self._errorBoundary.set_diagnostics(diagnostics)
            self._errorBoundary.set_init_context(init_context)
            if options is None:
                options = StatsigOptions()
            self._options = options
            self.__shutdown_event = threading.Event()
            self.__statsig_metadata = _StatsigMetadata.get()
            self._errorBoundary.set_statsig_options_and_metadata(
                self._options, self.__statsig_metadata
            )
            self._network = _StatsigNetwork(
                sdk_key, self._options, self.__statsig_metadata, self._errorBoundary, diagnostics, self.__shutdown_event
            )
            self._logger = _StatsigLogger(
                self._network,
                self.__shutdown_event,
                self.__statsig_metadata,
                self._errorBoundary,
                self._options,
                diagnostics
            )
            diagnostics.set_logger(self._logger)
            diagnostics.set_statsig_options(self._options)
            diagnostics.set_diagnostics_enabled(self._options.disable_diagnostics)

            self._spec_store = _SpecStore(
                self._network,
                self._options,
                self.__statsig_metadata,
                self._errorBoundary,
                self.__shutdown_event,
                sdk_key,
                diagnostics
            )

            self._evaluator = _Evaluator(self._spec_store)
            self._sampling_key_set = TTLSet(self.__shutdown_event)

            self._spec_store.initialize()
            self._initialized = True

        except (StatsigValueError, StatsigNameError, StatsigRuntimeError) as e:
            threw_error = True
            raise e

        except Exception as e:
            threw_error = True
            self._errorBoundary.log_exception("initialize", e)
            self._initialized = True
        finally:
            diagnostics.add_marker(Marker().overall().end({"success": not threw_error}))
            diagnostics.log_diagnostics(Context.INITIALIZE)
            init_context.source = self.get_init_source()
            init_context.store_populated = self.is_store_populated()
            init_context.success = not threw_error

        return InitializeDetails(int(time.time() * 1000) - init_context.start_time, init_context.source,
                                 init_context.success, init_context.store_populated, init_context.error)

    def is_store_populated(self):
        try:
            return self._spec_store.last_update_time() > 0
        except Exception:
            return False

    def get_init_source(self):
        try:
            return self._spec_store.init_source
        except Exception:
            return DataSource.UNINITIALIZED

    def get_feature_gate(self, user: StatsigUser, gate_name: str, log_exposure=True):
        def task():
            if not self._verify_inputs(user, gate_name):
                feature_gate = FeatureGate(
                    False,
                    gate_name,
                    "",
                )
                if not self._options.evaluation_callback is None:
                    self._options.evaluation_callback(feature_gate)
                return False

            result = self.__check_gate(user, gate_name, log_exposure)
            feature_gate = FeatureGate(
                result.boolean_value,
                gate_name,
                result.rule_id,
                result.group_name,
                result.evaluation_details
            )
            self.safe_eval_callback(feature_gate)
            return feature_gate

        return self._errorBoundary.capture(
            "get_feature_gate", task, lambda: False, {"configName": gate_name}
        )

    def check_gate(self, user: StatsigUser, gate_name: str, log_exposure=True):
        def task():
            result = self.get_feature_gate(user, gate_name, log_exposure)
            return result.value

        return self._errorBoundary.capture(
            "check_gate", task, lambda: False, {"configName": gate_name}
        )

    def manually_log_gate_exposure(self, user: StatsigUser, gate_name: str):
        user = self.__normalize_user(user)
        result = self._evaluator.check_gate(user, gate_name)
        self._logger.log_gate_exposure(
            user,
            gate_name,
            result.boolean_value,
            result.rule_id,
            result.secondary_exposures,
            result.evaluation_details,
            is_manual_exposure=True,
        )

    def get_config(self, user: StatsigUser, config_name: str, log_exposure=True):
        def task():
            if not self._verify_inputs(user, config_name):
                dynamicConfig = DynamicConfig({}, config_name, "")
                if not self._options.evaluation_callback is None:
                    self._options.evaluation_callback(dynamicConfig)
                return dynamicConfig

            result = self.__get_config(user, config_name, log_exposure)
            dynamicConfig = DynamicConfig(
                result.json_value,
                config_name,
                result.rule_id,
                result.user,
                group_name=result.group_name,
                evaluation_details=result.evaluation_details,
                secondary_exposures=result.secondary_exposures
            )
            self.safe_eval_callback(dynamicConfig)
            return dynamicConfig

        return self._errorBoundary.capture(
            "get_config",
            task,
            lambda: DynamicConfig({}, config_name, ""),
            {"configName": config_name},
        )

    def manually_log_config_exposure(self, user: StatsigUser, config_name: str):
        user = self.__normalize_user(user)
        result = self._evaluator.get_config(user, config_name)
        self._logger.log_config_exposure(
            user,
            config_name,
            result.rule_id,
            result.secondary_exposures,
            result.evaluation_details,
            is_manual_exposure=True,
        )

    def log_exposure_for_config(self, config_eval: DynamicConfig):
        user = self.__normalize_user(config_eval.user)
        self._logger.log_config_exposure(
            user,
            config_eval.name,
            config_eval.rule_id,
            config_eval.secondary_exposures,
            config_eval.evaluation_details,
            is_manual_exposure=True,
        )

    def get_experiment(
            self, user: StatsigUser, experiment_name: str, log_exposure=True
    ):
        def task():
            if not self._verify_inputs(user, experiment_name):
                dynamicConfig = DynamicConfig({}, experiment_name, "")
                if not self._options.evaluation_callback is None:
                    self._options.evaluation_callback(dynamicConfig)
                return dynamicConfig
            result = self.__get_config(user, experiment_name, log_exposure)
            dynamicConfig = DynamicConfig(
                result.json_value,
                experiment_name,
                result.rule_id,
                user,
                group_name=result.group_name,
                evaluation_details=result.evaluation_details,
                secondary_exposures=result.secondary_exposures,
            )
            self.safe_eval_callback(dynamicConfig)
            return dynamicConfig

        return self._errorBoundary.capture(
            "get_experiment",
            task,
            lambda: DynamicConfig({}, experiment_name, ""),
            {"configName": experiment_name},
        )

    def manually_log_experiment_exposure(self, user: StatsigUser, experiment_name: str):
        user = self.__normalize_user(user)
        result = self._evaluator.get_config(user, experiment_name, True)
        self._logger.log_config_exposure(
            user,
            experiment_name,
            result.rule_id,
            result.secondary_exposures,
            result.evaluation_details,
            is_manual_exposure=True,
        )

    def get_layer(self, user: StatsigUser, layer_name: str, log_exposure=True) -> Layer:
        def task():
            if not self._verify_inputs(user, layer_name):
                layer = Layer._create(layer_name, {}, "")
                if not self._options.evaluation_callback is None:
                    self._options.evaluation_callback(layer)
                return layer

            normal_user = self.__normalize_user(user)
            result = self._evaluator.get_layer(normal_user, layer_name)

            def log_func(layer: Layer, parameter_name: str):
                should_log, logged_sampling_rate, shadow_logged = self.__determine_sampling(
                    EntityType.LAYER, layer_name, result, user, parameter_name)

                if log_exposure and should_log:
                    self._logger.log_layer_exposure(
                        normal_user, layer, parameter_name, result, sampling_rate=logged_sampling_rate,
                        shadow_logged=shadow_logged,
                        sampling_mode=_SDK_Configs.get_config_str_value("sampling_mode")
                    )

            layer = Layer._create(
                layer_name,
                result.json_value,
                result.rule_id,
                result.group_name,
                result.allocated_experiment,
                log_func,
                evaluation_details=result.evaluation_details
            )
            self.safe_eval_callback(layer)
            return layer

        return self._errorBoundary.capture(
            "get_layer",
            task,
            lambda: Layer._create(layer_name, {}, ""),
            {"configName": layer_name},
        )

    def manually_log_layer_parameter_exposure(
            self, user: StatsigUser, layer_name: str, parameter_name: str
    ):
        user = self.__normalize_user(user)
        result = self._evaluator.get_layer(user, layer_name)
        layer = Layer._create(
            layer_name,
            result.json_value,
            result.rule_id,
            result.group_name,
            result.allocated_experiment,
        )
        self._logger.log_layer_exposure(
            user, layer, parameter_name, result, is_manual_exposure=True
        )

    def safe_eval_callback(self, config: Union[FeatureGate, DynamicConfig, Layer]):
        if self._options.evaluation_callback is not None:
            self._options.evaluation_callback(config)

    def log_event(self, event: StatsigEvent):
        def task():
            if not self._initialized:
                raise StatsigRuntimeError(
                    "Must call initialize before checking gates/configs/experiments or logging events"
                )

            self._verify_bg_threads_running()

            event.user = self.__normalize_user(event.user)
            self._logger.log(event)

        self._errorBoundary.swallow("log_event", task)

    def flush(self):
        if self._logger is not None:
            self._logger.flush()

    def shutdown(self):
        def task():
            self.__shutdown_event.set()
            self._logger.shutdown()
            self._spec_store.shutdown()
            self._network.shutdown()
            self._errorBoundary.shutdown()
            self._initialized = False

        self._errorBoundary.swallow("shutdown", task)

    def override_gate(self, gate: str, value: bool, user_id: Optional[str] = None):
        self._errorBoundary.swallow(
            "override_gate", lambda: self._evaluator.override_gate(gate, value, user_id)
        )

    def override_config(
            self, config: str, value: object, user_id: Optional[str] = None
    ):
        self._errorBoundary.swallow(
            "override_config",
            lambda: self._evaluator.override_config(config, value, user_id),
        )

    def override_experiment(
            self, experiment: str, value: object, user_id: Optional[str] = None
    ):
        self._errorBoundary.swallow(
            "override_experiment",
            lambda: self._evaluator.override_config(experiment, value, user_id),
        )

    def override_layer(self, layer: str, value: object, user_id: Optional[str] = None):
        self._errorBoundary.swallow(
            "override_layer",
            lambda: self._evaluator.override_layer(layer, value, user_id),
        )

    def remove_gate_override(self, gate: str, user_id: Optional[str] = None):
        self._errorBoundary.swallow(
            "remove_gate_override",
            lambda: self._evaluator.remove_gate_override(gate, user_id),
        )

    def remove_config_override(self, config: str, user_id: Optional[str] = None):
        self._errorBoundary.swallow(
            "remove_config_override",
            lambda: self._evaluator.remove_config_override(config, user_id),
        )

    def remove_experiment_override(
            self, experiment: str, user_id: Optional[str] = None
    ):
        self._errorBoundary.swallow(
            "remove_experiment_override",
            lambda: self._evaluator.remove_config_override(experiment, user_id),
        )

    def remove_layer_override(self, layer: str, user_id: Optional[str] = None):
        self._errorBoundary.swallow(
            "remove_layer_override",
            lambda: self._evaluator.remove_layer_override(layer, user_id),
        )

    def remove_all_overrides(self):
        self._errorBoundary.swallow(
            "remove_all_overrides", lambda: self._evaluator.remove_all_overrides()
        )

    def get_client_initialize_response(
            self, user: StatsigUser,
            client_sdk_key: Optional[str] = None,
            hash: Optional[HashingAlgorithm] = HashingAlgorithm.SHA256,
            include_local_overrides: Optional[bool] = False,
    ):
        hash_value = hash.value if hash is not None else HashingAlgorithm.SHA256.value

        def task():
            result = self._evaluator.get_client_initialize_response(
                self.__normalize_user(user), hash or HashingAlgorithm.SHA256, client_sdk_key, include_local_overrides
            )
            if result is None:
                self._errorBoundary.log_exception("get_client_initialize_response",
                                                  StatsigValueError("Failed to get client initialize response"),
                                                  {'clientKey': client_sdk_key, 'hash': hash_value})
            return result

        def recover():
            return None

        return self._errorBoundary.capture(
            "get_client_initialize_response", task, recover, {'clientKey': client_sdk_key, 'hash': hash_value}
        )

    def evaluate_all(self, user: StatsigUser):
        def task():
            all_gates = {}
            for gate in self._spec_store.get_all_gates():
                result = self.__check_gate(user, gate, False)
                all_gates[gate] = {
                    "value": result.boolean_value,
                    "rule_id": result.rule_id,
                }

            all_configs = {}
            for config in self._spec_store.get_all_configs():
                result = self.__get_config(user, config, False)
                all_configs[config] = {
                    "value": result.json_value,
                    "rule_id": result.rule_id,
                }
            return dict({"feature_gates": all_gates, "dynamic_configs": all_configs})

        def recover():
            return dict({"feature_gates": {}, "dynamic_configs": {}})

        return self._errorBoundary.capture("evaluate_all", task, recover)

    def _verify_inputs(self, user: StatsigUser, variable_name: str):
        if not self._initialized:
            raise StatsigRuntimeError(
                "Must call initialize before checking gates/configs/experiments or logging events"
            )

        if not user or (not user.user_id and not user.custom_ids):
            raise StatsigValueError(
                "A non-empty StatsigUser with user_id or custom_ids is required. See "
                "https://docs.statsig.com/messages/serverRequiredUserID"
            )

        if not variable_name:
            return False

        self._verify_bg_threads_running()

        return True

    def _verify_bg_threads_running(self):
        if self._logger is not None:
            self._logger.spawn_bg_threads_if_needed()

        if self._spec_store is not None:
            self._spec_store.spec_updater.start_background_threads()

        if self._network is not None:
            self._network.spawn_bg_threads_if_needed()

    def __check_gate(self, user: StatsigUser, gate_name: str, log_exposure=True):
        user = self.__normalize_user(user)
        result = self._evaluator.check_gate(user, gate_name)
        should_log, logged_sampling_rate, shadow_logged = self.__determine_sampling(EntityType.GATE, gate_name, result,
                                                                                    user)

        if log_exposure and should_log:
            self._logger.log_gate_exposure(
                user,
                gate_name,
                result.boolean_value,
                result.rule_id,
                result.secondary_exposures,
                result.evaluation_details,
                sampling_rate=logged_sampling_rate,
                shadow_logged=shadow_logged,
                sampling_mode=_SDK_Configs.get_config_str_value("sampling_mode")
            )
        return result

    def __get_config(self, user: StatsigUser, config_name: str, log_exposure=True):
        user = self.__normalize_user(user)

        result = self._evaluator.get_config(user, config_name)
        result.user = user
        should_log, logged_sampling_rate, shadow_logged = self.__determine_sampling(EntityType.CONFIG, config_name,
                                                                                    result, user)

        if log_exposure and should_log:
            self._logger.log_config_exposure(
                user,
                config_name,
                result.rule_id,
                result.secondary_exposures,
                result.evaluation_details,
                sampling_rate=logged_sampling_rate,
                shadow_logged=shadow_logged,
                sampling_mode=_SDK_Configs.get_config_str_value("sampling_mode")
            )
        return result

    def __determine_sampling(self, type: EntityType, name: str, result: _ConfigEvaluation, user: StatsigUser,
                             param_name="") -> Tuple[
        bool, Optional[int], Optional[str]]:  # should_log, logged_sampling_rate, shadow_logged
        try:
            shadow_should_log, logged_sampling_rate = True, None
            env = self._options.get_sdk_environment_tier()
            sampling_mode = _SDK_Configs.get_config_str_value("sampling_mode")
            special_case_sampling_rate = _SDK_Configs.get_config_int_value("special_case_sampling_rate")
            special_case_rules = ["disabled", "default", ""]

            if sampling_mode is None or sampling_mode == "none" or env != "production":
                return True, None, None

            if result.forward_all_exposures:
                return True, None, None

            if result.rule_id.endswith((':override', ':id_override')):
                return True, None, None

            samplingSetKey = f"{name}_{result.rule_id}"
            if not self._sampling_key_set.contains(samplingSetKey):
                self._sampling_key_set.add(samplingSetKey)
                return True, None, None

            should_sample = result.sample_rate is not None or result.rule_id in special_case_rules
            if not should_sample:
                return True, None, None

            exposure_key = ""
            if type == EntityType.GATE:
                exposure_key = compute_dedupe_key_for_gate(name, result.rule_id, result.boolean_value,
                                                           user.user_id, user.custom_ids)
            elif type == EntityType.CONFIG:
                exposure_key = compute_dedupe_key_for_config(name, result.rule_id, user.user_id, user.custom_ids)
            elif type == EntityType.LAYER:
                exposure_key = compute_dedupe_key_for_layer(name, result.allocated_experiment, param_name,
                                                            result.rule_id,
                                                            user.user_id, user.custom_ids)

            if result.sample_rate is not None:
                shadow_should_log = is_hash_in_sampling_rate(exposure_key, result.sample_rate)
                logged_sampling_rate = result.sample_rate
            elif result.rule_id in special_case_rules and special_case_sampling_rate is not None:
                shadow_should_log = is_hash_in_sampling_rate(exposure_key, special_case_sampling_rate)
                logged_sampling_rate = special_case_sampling_rate

            shadow_logged = None if logged_sampling_rate is None else "logged" if shadow_should_log else "dropped"
            if sampling_mode == "on":
                return shadow_should_log, logged_sampling_rate, shadow_logged
            if sampling_mode == "shadow":
                return True, logged_sampling_rate, shadow_logged

            return True, None, None
        except Exception as e:
            self._errorBoundary.log_exception("__determine_sampling", e, log_mode="debug")
            return True, None, None

    def __normalize_user(self, user):
        userCopy = dataclasses.replace(user)
        if self._options is not None and self._options._environment is not None:
            userCopy._statsig_environment = self._options._environment
        return userCopy

    def _sync(self, sync_func, interval):
        while True:
            try:
                if self.__shutdown_event.wait(interval):
                    break
                sync_func()
            except Exception as e:
                self._errorBoundary.log_exception("_sync", e)
