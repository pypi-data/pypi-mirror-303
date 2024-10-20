import logging
from collections.abc import Iterable, Sequence
from datetime import timedelta
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Annotated,
    Any,
    Literal,
    Protocol,
    TypeAlias,
    runtime_checkable,
)

import nshconfig as C
from lightning.fabric.plugins import CheckpointIO, ClusterEnvironment
from lightning.fabric.plugins.precision.precision import _PRECISION_INPUT
from lightning.pytorch.accelerators import Accelerator
from lightning.pytorch.callbacks.callback import Callback
from lightning.pytorch.loggers import Logger
from lightning.pytorch.plugins import _PLUGIN_INPUT
from lightning.pytorch.plugins.layer_sync import LayerSync
from lightning.pytorch.plugins.precision.precision import Precision
from lightning.pytorch.profilers import Profiler
from lightning.pytorch.strategies.strategy import Strategy
from typing_extensions import TypedDict, TypeVar, override

from .._checkpoint.loader import CheckpointLoadingConfig
from .._hf_hub import HuggingFaceHubConfig
from ..callbacks import (
    BestCheckpointCallbackConfig,
    CallbackConfig,
    EarlyStoppingConfig,
    LastCheckpointCallbackConfig,
    OnExceptionCheckpointCallbackConfig,
)
from ..callbacks.base import CallbackConfigBase
from ..callbacks.debug_flag import DebugFlagCallbackConfig
from ..callbacks.rlp_sanity_checks import RLPSanityChecksConfig
from ..callbacks.shared_parameters import SharedParametersConfig
from ..loggers import (
    CSVLoggerConfig,
    LoggerConfig,
    TensorboardLoggerConfig,
    WandbLoggerConfig,
)
from ..profiler import ProfilerConfig

if TYPE_CHECKING:
    from ..model.config import BaseConfig

log = logging.getLogger(__name__)


class LoggingConfig(CallbackConfigBase):
    enabled: bool = True
    """Enable experiment tracking."""

    loggers: Sequence[LoggerConfig] = [
        WandbLoggerConfig(),
        CSVLoggerConfig(),
        TensorboardLoggerConfig(),
    ]
    """Loggers to use for experiment tracking."""

    log_lr: bool | Literal["step", "epoch"] = True
    """If enabled, will register a `LearningRateMonitor` callback to log the learning rate to the logger."""
    log_epoch: bool = True
    """If enabled, will log the fractional epoch number to the logger."""

    actsave_logged_metrics: bool = False
    """If enabled, will automatically save logged metrics using ActSave (if nshutils is installed)."""

    @property
    def wandb(self):
        return next(
            (
                logger
                for logger in self.loggers
                if isinstance(logger, WandbLoggerConfig)
            ),
            None,
        )

    @property
    def csv(self):
        return next(
            (logger for logger in self.loggers if isinstance(logger, CSVLoggerConfig)),
            None,
        )

    @property
    def tensorboard(self):
        return next(
            (
                logger
                for logger in self.loggers
                if isinstance(logger, TensorboardLoggerConfig)
            ),
            None,
        )

    def create_loggers(self, root_config: "BaseConfig"):
        """
        Constructs and returns a list of loggers based on the provided root configuration.

        Args:
            root_config (BaseConfig): The root configuration object.

        Returns:
            list[Logger]: A list of constructed loggers.
        """
        if not self.enabled:
            return

        for logger_config in sorted(
            self.loggers,
            key=lambda x: x.priority,
            reverse=True,
        ):
            if not logger_config.enabled:
                continue
            if (logger := logger_config.create_logger(root_config)) is None:
                continue
            yield logger

    @override
    def create_callbacks(self, root_config):
        if self.log_lr:
            from lightning.pytorch.callbacks import LearningRateMonitor

            logging_interval: str | None = None
            if isinstance(self.log_lr, str):
                logging_interval = self.log_lr

            yield LearningRateMonitor(logging_interval=logging_interval)

        if self.log_epoch:
            from ..callbacks.log_epoch import LogEpochCallback

            yield LogEpochCallback()

        for logger in self.loggers:
            if not logger or not isinstance(logger, CallbackConfigBase):
                continue

            yield from logger.create_callbacks(root_config)


class GradientClippingConfig(C.Config):
    enabled: bool = True
    """Enable gradient clipping."""
    value: int | float
    """Value to use for gradient clipping."""
    algorithm: Literal["value", "norm"] = "norm"
    """Norm type to use for gradient clipping."""


class OptimizationConfig(CallbackConfigBase):
    log_grad_norm: bool | str | float = False
    """If enabled, will log the gradient norm (averaged across all model parameters) to the logger."""
    log_grad_norm_per_param: bool | str | float = False
    """If enabled, will log the gradient norm for each model parameter to the logger."""

    log_param_norm: bool | str | float = False
    """If enabled, will log the parameter norm (averaged across all model parameters) to the logger."""
    log_param_norm_per_param: bool | str | float = False
    """If enabled, will log the parameter norm for each model parameter to the logger."""

    gradient_clipping: GradientClippingConfig | None = None
    """Gradient clipping configuration, or None to disable gradient clipping."""

    @override
    def create_callbacks(self, root_config):
        from ..callbacks.norm_logging import NormLoggingConfig

        yield from NormLoggingConfig(
            log_grad_norm=self.log_grad_norm,
            log_grad_norm_per_param=self.log_grad_norm_per_param,
            log_param_norm=self.log_param_norm,
            log_param_norm_per_param=self.log_param_norm_per_param,
        ).create_callbacks(root_config)


TPlugin = TypeVar(
    "TPlugin",
    Precision,
    ClusterEnvironment,
    CheckpointIO,
    LayerSync,
    infer_variance=True,
)


@runtime_checkable
class PluginConfigProtocol(Protocol[TPlugin]):
    def create_plugin(self) -> TPlugin: ...


@runtime_checkable
class AcceleratorConfigProtocol(Protocol):
    def create_accelerator(self) -> Accelerator: ...


@runtime_checkable
class StrategyConfigProtocol(Protocol):
    def create_strategy(self) -> Strategy: ...


AcceleratorLiteral: TypeAlias = Literal[
    "cpu", "gpu", "tpu", "ipu", "hpu", "mps", "auto"
]

StrategyLiteral: TypeAlias = Literal[
    "auto",
    "ddp",
    "ddp_find_unused_parameters_false",
    "ddp_find_unused_parameters_true",
    "ddp_spawn",
    "ddp_spawn_find_unused_parameters_false",
    "ddp_spawn_find_unused_parameters_true",
    "ddp_fork",
    "ddp_fork_find_unused_parameters_false",
    "ddp_fork_find_unused_parameters_true",
    "ddp_notebook",
    "dp",
    "deepspeed",
    "deepspeed_stage_1",
    "deepspeed_stage_1_offload",
    "deepspeed_stage_2",
    "deepspeed_stage_2_offload",
    "deepspeed_stage_3",
    "deepspeed_stage_3_offload",
    "deepspeed_stage_3_offload_nvme",
    "fsdp",
    "fsdp_cpu_offload",
    "single_xla",
    "xla_fsdp",
    "xla",
    "single_tpu",
]


class ReproducibilityConfig(C.Config):
    deterministic: bool | Literal["warn"] | None = None
    """
    If ``True``, sets whether PyTorch operations must use deterministic algorithms.
        Set to ``"warn"`` to use deterministic algorithms whenever possible, throwing warnings on operations
        that don't support deterministic mode. If not set, defaults to ``False``. Default: ``None``.
    """


CheckpointCallbackConfig: TypeAlias = Annotated[
    BestCheckpointCallbackConfig
    | LastCheckpointCallbackConfig
    | OnExceptionCheckpointCallbackConfig,
    C.Field(discriminator="name"),
]


class CheckpointSavingConfig(CallbackConfigBase):
    enabled: bool = True
    """Enable checkpoint saving."""

    checkpoint_callbacks: Sequence[CheckpointCallbackConfig] = [
        BestCheckpointCallbackConfig(throw_on_no_metric=False),
        LastCheckpointCallbackConfig(),
        OnExceptionCheckpointCallbackConfig(),
    ]
    """Checkpoint callback configurations."""

    def disable_(self):
        self.enabled = False
        return self

    def should_save_checkpoints(self, root_config: "BaseConfig"):
        if not self.enabled:
            return False

        if root_config.trainer.fast_dev_run:
            return False

        return True

    @override
    def create_callbacks(self, root_config: "BaseConfig"):
        if not self.should_save_checkpoints(root_config):
            return

        for callback_config in self.checkpoint_callbacks:
            yield from callback_config.create_callbacks(root_config)


class LightningTrainerKwargs(TypedDict, total=False):
    accelerator: str | Accelerator
    """Supports passing different accelerator types ("cpu", "gpu", "tpu", "ipu", "hpu", "mps", "auto")
    as well as custom accelerator instances."""

    strategy: str | Strategy
    """Supports different training strategies with aliases as well custom strategies.
    Default: ``"auto"``.
    """

    devices: list[int] | str | int
    """The devices to use. Can be set to a positive number (int or str), a sequence of device indices
    (list or str), the value ``-1`` to indicate all available devices should be used, or ``"auto"`` for
    automatic selection based on the chosen accelerator. Default: ``"auto"``.
    """

    num_nodes: int
    """Number of GPU nodes for distributed training.
    Default: ``1``.
    """

    precision: _PRECISION_INPUT | None
    """Double precision (64, '64' or '64-true'), full precision (32, '32' or '32-true'),
    16bit mixed precision (16, '16', '16-mixed') or bfloat16 mixed precision ('bf16', 'bf16-mixed').
    Can be used on CPU, GPU, TPUs, HPUs or IPUs.
    Default: ``'32-true'``.
    """

    logger: Logger | Iterable[Logger] | bool | None
    """Logger (or iterable collection of loggers) for experiment tracking. A ``True`` value uses
    the default ``TensorBoardLogger`` if it is installed, otherwise ``CSVLogger``.
    ``False`` will disable logging. If multiple loggers are provided, local files
    (checkpoints, profiler traces, etc.) are saved in the ``log_dir`` of the first logger.
    Default: ``True``.
    """

    callbacks: list[Callback] | Callback | None
    """Add a callback or list of callbacks.
    Default: ``None``.
    """

    fast_dev_run: int | bool
    """Runs n if set to ``n`` (int) else 1 if set to ``True`` batch(es)
    of train, val and test to find any bugs (ie: a sort of unit test).
    Default: ``False``.
    """

    max_epochs: int | None
    """Stop training once this number of epochs is reached. Disabled by default (None).
    If both max_epochs and max_steps are not specified, defaults to ``max_epochs = 1000``.
    To enable infinite training, set ``max_epochs = -1``.
    """

    min_epochs: int | None
    """Force training for at least these many epochs. Disabled by default (None).
    """

    max_steps: int
    """Stop training after this number of steps. Disabled by default (-1). If ``max_steps = -1``
    and ``max_epochs = None``, will default to ``max_epochs = 1000``. To enable infinite training, set
    ``max_epochs`` to ``-1``.
    """

    min_steps: int | None
    """Force training for at least these number of steps. Disabled by default (``None``).
    """

    max_time: str | timedelta | dict[str, int] | None
    """Stop training after this amount of time has passed. Disabled by default (``None``).
    The time duration can be specified in the format DD:HH:MM:SS (days, hours, minutes seconds), as a
    :class:`datetime.timedelta`, or a dictionary with keys that will be passed to
    :class:`datetime.timedelta`.
    """

    limit_train_batches: int | float | None
    """How much of training dataset to check (float = fraction, int = num_batches).
    Default: ``1.0``.
    """

    limit_val_batches: int | float | None
    """How much of validation dataset to check (float = fraction, int = num_batches).
    Default: ``1.0``.
    """

    limit_test_batches: int | float | None
    """How much of test dataset to check (float = fraction, int = num_batches).
    Default: ``1.0``.
    """

    limit_predict_batches: int | float | None
    """How much of prediction dataset to check (float = fraction, int = num_batches).
    Default: ``1.0``.
    """

    overfit_batches: int | float
    """Overfit a fraction of training/validation data (float) or a set number of batches (int).
    Default: ``0.0``.
    """

    val_check_interval: int | float | None
    """How often to check the validation set. Pass a ``float`` in the range [0.0, 1.0] to check
    after a fraction of the training epoch. Pass an ``int`` to check after a fixed number of training
    batches. An ``int`` value can only be higher than the number of training batches when
    ``check_val_every_n_epoch=None``, which validates after every ``N`` training batches
    across epochs or during iteration-based training.
    Default: ``1.0``.
    """

    check_val_every_n_epoch: int | None
    """Perform a validation loop every after every `N` training epochs. If ``None``,
    validation will be done solely based on the number of training batches, requiring ``val_check_interval``
    to be an integer value.
    Default: ``1``.
    """

    num_sanity_val_steps: int | None
    """Sanity check runs n validation batches before starting the training routine.
    Set it to `-1` to run all batches in all validation dataloaders.
    Default: ``2``.
    """

    log_every_n_steps: int | None
    """How often to log within steps.
    Default: ``50``.
    """

    enable_checkpointing: bool | None
    """If ``True``, enable checkpointing.
    It will configure a default ModelCheckpoint callback if there is no user-defined ModelCheckpoint in
    :paramref:`~lightning.pytorch.trainer.trainer.Trainer.callbacks`.
    Default: ``True``.
    """

    enable_progress_bar: bool | None
    """Whether to enable to progress bar by default.
    Default: ``True``.
    """

    enable_model_summary: bool | None
    """Whether to enable model summarization by default.
    Default: ``True``.
    """

    accumulate_grad_batches: int
    """Accumulates gradients over k batches before stepping the optimizer.
    Default: 1.
    """

    gradient_clip_val: int | float | None
    """The value at which to clip gradients. Passing ``gradient_clip_val=None`` disables
    gradient clipping. If using Automatic Mixed Precision (AMP), the gradients will be unscaled before.
    Default: ``None``.
    """

    gradient_clip_algorithm: str | None
    """The gradient clipping algorithm to use. Pass ``gradient_clip_algorithm="value"``
    to clip by value, and ``gradient_clip_algorithm="norm"`` to clip by norm. By default it will
    be set to ``"norm"``.
    """

    deterministic: bool | Literal["warn"] | None
    """If ``True``, sets whether PyTorch operations must use deterministic algorithms.
    Set to ``"warn"`` to use deterministic algorithms whenever possible, throwing warnings on operations
    that don't support deterministic mode. If not set, defaults to ``False``. Default: ``None``.
    """

    benchmark: bool | None
    """The value (``True`` or ``False``) to set ``torch.backends.cudnn.benchmark`` to.
    The value for ``torch.backends.cudnn.benchmark`` set in the current session will be used
    (``False`` if not manually set). If :paramref:`~lightning.pytorch.trainer.trainer.Trainer.deterministic`
    is set to ``True``, this will default to ``False``. Override to manually set a different value.
    Default: ``None``.
    """

    inference_mode: bool
    """Whether to use :func:`torch.inference_mode` or :func:`torch.no_grad` during
    evaluation (``validate``/``test``/``predict``).
    """

    use_distributed_sampler: bool
    """Whether to wrap the DataLoader's sampler with
    :class:`torch.utils.data.DistributedSampler`. If not specified this is toggled automatically for
    strategies that require it. By default, it will add ``shuffle=True`` for the train sampler and
    ``shuffle=False`` for validation/test/predict samplers. If you want to disable this logic, you can pass
    ``False`` and add your own distributed sampler in the dataloader hooks. If ``True`` and a distributed
    sampler was already added, Lightning will not replace the existing one. For iterable-style datasets,
    we don't do this automatically.
    """

    profiler: Profiler | str | None
    """To profile individual steps during training and assist in identifying bottlenecks.
    Default: ``None``.
    """

    detect_anomaly: bool
    """Enable anomaly detection for the autograd engine.
    Default: ``False``.
    """

    barebones: bool
    """Whether to run in "barebones mode", where all features that may impact raw speed are
    disabled. This is meant for analyzing the Trainer overhead and is discouraged during regular training
    runs. The following features are deactivated:
    :paramref:`~lightning.pytorch.trainer.trainer.Trainer.enable_checkpointing`,
    :paramref:`~lightning.pytorch.trainer.trainer.Trainer.logger`,
    :paramref:`~lightning.pytorch.trainer.trainer.Trainer.enable_progress_bar`,
    :paramref:`~lightning.pytorch.trainer.trainer.Trainer.log_every_n_steps`,
    :paramref:`~lightning.pytorch.trainer.trainer.Trainer.enable_model_summary`,
    :paramref:`~lightning.pytorch.trainer.trainer.Trainer.num_sanity_val_steps`,
    :paramref:`~lightning.pytorch.trainer.trainer.Trainer.fast_dev_run`,
    :paramref:`~lightning.pytorch.trainer.trainer.Trainer.detect_anomaly`,
    :paramref:`~lightning.pytorch.trainer.trainer.Trainer.profiler`,
    :meth:`~lightning.pytorch.core.LightningModule.log`,
    :meth:`~lightning.pytorch.core.LightningModule.log_dict`.
    """

    plugins: _PLUGIN_INPUT | list[_PLUGIN_INPUT] | None
    """Plugins allow modification of core behavior like ddp and amp, and enable custom lightning plugins.
    Default: ``None``.
    """

    sync_batchnorm: bool
    """Synchronize batch norm layers between process groups/whole world.
    Default: ``False``.
    """

    reload_dataloaders_every_n_epochs: int
    """Set to a positive integer to reload dataloaders every n epochs.
    Default: ``0``.
    """

    default_root_dir: Path | None
    """Default path for logs and weights when no logger/ckpt_callback passed.
    Default: ``os.getcwd()``.
    Can be remote file paths such as `s3://mybucket/path` or 'hdfs://path/'
    """


class SanityCheckingConfig(C.Config):
    reduce_lr_on_plateau: Literal["disable", "error", "warn"] = "error"
    """
    If enabled, will do some sanity checks if the `ReduceLROnPlateau` scheduler is used:
        - If the `interval` is step, it makes sure that validation is called every `frequency` steps.
        - If the `interval` is epoch, it makes sure that validation is called every `frequency` epochs.
    Valid values are: "disable", "warn", "error".
    """


class TrainerConfig(C.Config):
    ckpt_path: Literal["none"] | str | Path | None = None
    """Path to a checkpoint to load and resume training from. If ``"none"``, will not load a checkpoint."""

    checkpoint_loading: CheckpointLoadingConfig | Literal["auto", "none"] = "auto"
    """Checkpoint loading configuration options.
    `"auto"` will automatically determine the best checkpoint loading strategy based on the provided.
    `"none"` will disable checkpoint loading.
    """

    checkpoint_saving: CheckpointSavingConfig = CheckpointSavingConfig()
    """Checkpoint saving configuration options."""

    hf_hub: HuggingFaceHubConfig = HuggingFaceHubConfig()
    """Hugging Face Hub configuration options."""

    logging: LoggingConfig = LoggingConfig()
    """Logging/experiment tracking (e.g., WandB) configuration options."""

    optimizer: OptimizationConfig = OptimizationConfig()
    """Optimization configuration options."""

    reproducibility: ReproducibilityConfig = ReproducibilityConfig()
    """Reproducibility configuration options."""

    reduce_lr_on_plateau_sanity_checking: RLPSanityChecksConfig | None = (
        RLPSanityChecksConfig()
    )
    """
    If enabled, will do some sanity checks if the `ReduceLROnPlateau` scheduler is used:
        - If the `interval` is step, it makes sure that validation is called every `frequency` steps.
        - If the `interval` is epoch, it makes sure that validation is called every `frequency` epochs.
    """

    early_stopping: EarlyStoppingConfig | None = None
    """Early stopping configuration options."""

    profiler: ProfilerConfig | None = None
    """
    To profile individual steps during training and assist in identifying bottlenecks.
        Default: ``None``.
    """

    callbacks: list[CallbackConfig] = []
    """Callbacks to use during training."""

    detect_anomaly: bool | None = None
    """Enable anomaly detection for the autograd engine.
    Default: ``False``.
    """

    plugins: list[PluginConfigProtocol] | None = None
    """
    Plugins allow modification of core behavior like ddp and amp, and enable custom lightning plugins.
        Default: ``None``.
    """

    auto_determine_num_nodes: bool = True
    """
    If enabled, will automatically determine the number of nodes for distributed training.

    This will only work on:
    - SLURM clusters
    - LSF clusters
    """

    fast_dev_run: int | bool = False
    """Runs n if set to ``n`` (int) else 1 if set to ``True`` batch(es)
    of train, val and test to find any bugs (ie: a sort of unit test).
    Default: ``False``.
    """

    precision: (
        Literal[
            "64-true",
            "32-true",
            "fp16-mixed",
            "bf16-mixed",
            "16-mixed-auto",
        ]
        | None
    ) = None
    """
    Training precision. Can be one of:
        - "64-true": Double precision (64-bit).
        - "32-true": Full precision (32-bit).
        - "fp16-mixed": Float16 mixed precision.
        - "bf16-mixed": BFloat16 mixed precision.
        - "16-mixed-auto": Automatic 16-bit: Uses bfloat16 if available, otherwise float16.
    """

    max_epochs: int | None = None
    """Stop training once this number of epochs is reached. Disabled by default (None).
    If both max_epochs and max_steps are not specified, defaults to ``max_epochs = 1000``.
    To enable infinite training, set ``max_epochs = -1``.
    """

    min_epochs: int | None = None
    """Force training for at least these many epochs. Disabled by default (None).
    """

    max_steps: int = -1
    """Stop training after this number of steps. Disabled by default (-1). If ``max_steps = -1``
    and ``max_epochs = None``, will default to ``max_epochs = 1000``. To enable infinite training, set
    ``max_epochs`` to ``-1``.
    """

    min_steps: int | None = None
    """Force training for at least these number of steps. Disabled by default (``None``).
    """

    max_time: str | timedelta | dict[str, int] | None = None
    """Stop training after this amount of time has passed. Disabled by default (``None``).
    The time duration can be specified in the format DD:HH:MM:SS (days, hours, minutes seconds), as a
    :class:`datetime.timedelta`, or a dictionary with keys that will be passed to
    :class:`datetime.timedelta`.
    """

    limit_train_batches: int | float | None = None
    """How much of training dataset to check (float = fraction, int = num_batches).
    Default: ``1.0``.
    """

    limit_val_batches: int | float | None = None
    """How much of validation dataset to check (float = fraction, int = num_batches).
    Default: ``1.0``.
    """

    limit_test_batches: int | float | None = None
    """How much of test dataset to check (float = fraction, int = num_batches).
    Default: ``1.0``.
    """

    limit_predict_batches: int | float | None = None
    """How much of prediction dataset to check (float = fraction, int = num_batches).
    Default: ``1.0``.
    """

    overfit_batches: int | float = 0.0
    """Overfit a fraction of training/validation data (float) or a set number of batches (int).
    Default: ``0.0``.
    """

    val_check_interval: int | float | None = None
    """How often to check the validation set. Pass a ``float`` in the range [0.0, 1.0] to check
    after a fraction of the training epoch. Pass an ``int`` to check after a fixed number of training
    batches. An ``int`` value can only be higher than the number of training batches when
    ``check_val_every_n_epoch=None``, which validates after every ``N`` training batches
    across epochs or during iteration-based training.
    Default: ``1.0``.
    """

    check_val_every_n_epoch: int | None = 1
    """Perform a validation loop every after every `N` training epochs. If ``None``,
    validation will be done solely based on the number of training batches, requiring ``val_check_interval``
    to be an integer value.
    Default: ``1``.
    """

    num_sanity_val_steps: int | None = None
    """Sanity check runs n validation batches before starting the training routine.
    Set it to `-1` to run all batches in all validation dataloaders.
    Default: ``2``.
    """

    log_every_n_steps: int | None = None
    """How often to log within steps.
    Default: ``50``.
    """

    inference_mode: bool = True
    """Whether to use :func:`torch.inference_mode` (if `True`) or :func:`torch.no_grad` (if `False`) during evaluation (``validate``/``test``/``predict``).
    Default: ``True``.
    """

    use_distributed_sampler: bool | None = None
    """Whether to wrap the DataLoader's sampler with
    :class:`torch.utils.data.DistributedSampler`. If not specified this is toggled automatically for
    strategies that require it. By default, it will add ``shuffle=True`` for the train sampler and
    ``shuffle=False`` for validation/test/predict samplers. If you want to disable this logic, you can pass
    ``False`` and add your own distributed sampler in the dataloader hooks. If ``True`` and a distributed
    sampler was already added, Lightning will not replace the existing one. For iterable-style datasets,
    we don't do this automatically.
    Default: ``True``.
    """

    accelerator: AcceleratorConfigProtocol | AcceleratorLiteral | None = None
    """Supports passing different accelerator types ("cpu", "gpu", "tpu", "ipu", "hpu", "mps", "auto")
    as well as custom accelerator instances.
    Default: ``"auto"``.
    """

    strategy: StrategyConfigProtocol | StrategyLiteral | None = None
    """Supports different training strategies with aliases as well custom strategies.
    Default: ``"auto"``.
    """

    devices: tuple[int, ...] | Sequence[int] | Literal["auto", "all"] | None = None
    """The devices to use. Can be set to a sequence of device indices, "all" to indicate all available devices should be used, or ``"auto"`` for
    automatic selection based on the chosen accelerator. Default: ``"auto"``.
    """

    shared_parameters: SharedParametersConfig | None = SharedParametersConfig()
    """If enabled, the model supports scaling the gradients of shared parameters that
    are registered in the self.shared_parameters list. This is useful for models that
    share parameters across multiple modules (e.g., in a GPT model) and want to
    downscale the gradients of these parameters to avoid overfitting.
    """

    auto_set_default_root_dir: bool = True
    """If enabled, will automatically set the default root dir to [cwd/lightning_logs/<id>/]. There is basically no reason to disable this."""
    save_checkpoint_metadata: bool = True
    """If enabled, will save additional metadata whenever a checkpoint is saved."""
    auto_set_debug_flag: DebugFlagCallbackConfig | None = DebugFlagCallbackConfig()
    """If enabled, will automatically set the debug flag to True if:
    - The trainer is running in fast_dev_run mode.
    - The trainer is running a sanity check (which happens before starting the training routine).
    """

    lightning_kwargs: LightningTrainerKwargs = LightningTrainerKwargs()
    """
    Additional keyword arguments to pass to the Lightning `pl.Trainer` constructor.

    Please refer to the Lightning documentation for a list of valid keyword arguments.
    """

    additional_lightning_kwargs: dict[str, Any] = {}
    """
    Additional keyword arguments to pass to the Lightning `pl.Trainer` constructor.

    This is essentially a non-type-checked version of `lightning_kwargs`.
    """

    set_float32_matmul_precision: Literal["medium", "high", "highest"] | None = None
    """If enabled, will set the torch float32 matmul precision to the specified value. Useful for faster training on Ampere+ GPUs."""

    def _nshtrainer_all_callback_configs(self) -> Iterable[CallbackConfigBase | None]:
        yield self.early_stopping
        yield self.checkpoint_saving
        yield self.logging
        yield self.optimizer
        yield self.hf_hub
        yield self.shared_parameters
        yield self.reduce_lr_on_plateau_sanity_checking
        yield self.auto_set_debug_flag
        yield from self.callbacks
