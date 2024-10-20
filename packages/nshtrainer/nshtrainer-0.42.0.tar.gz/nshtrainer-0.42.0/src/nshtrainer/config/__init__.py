__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer import BaseConfig as BaseConfig
    from nshtrainer import MetricConfig as MetricConfig
    from nshtrainer._checkpoint.loader import (
        BestCheckpointStrategyConfig as BestCheckpointStrategyConfig,
    )
    from nshtrainer._checkpoint.loader import (
        CheckpointLoadingStrategyConfig as CheckpointLoadingStrategyConfig,
    )
    from nshtrainer._checkpoint.loader import CheckpointMetadata as CheckpointMetadata
    from nshtrainer._checkpoint.loader import (
        LastCheckpointStrategyConfig as LastCheckpointStrategyConfig,
    )
    from nshtrainer._checkpoint.loader import (
        UserProvidedPathCheckpointStrategyConfig as UserProvidedPathCheckpointStrategyConfig,
    )
    from nshtrainer._hf_hub import CallbackConfigBase as CallbackConfigBase
    from nshtrainer._hf_hub import (
        HuggingFaceHubAutoCreateConfig as HuggingFaceHubAutoCreateConfig,
    )
    from nshtrainer._hf_hub import HuggingFaceHubConfig as HuggingFaceHubConfig
    from nshtrainer.callbacks import (
        BestCheckpointCallbackConfig as BestCheckpointCallbackConfig,
    )
    from nshtrainer.callbacks import CallbackConfig as CallbackConfig
    from nshtrainer.callbacks import DebugFlagCallbackConfig as DebugFlagCallbackConfig
    from nshtrainer.callbacks import DirectorySetupConfig as DirectorySetupConfig
    from nshtrainer.callbacks import EarlyStoppingConfig as EarlyStoppingConfig
    from nshtrainer.callbacks import EMAConfig as EMAConfig
    from nshtrainer.callbacks import EpochTimerConfig as EpochTimerConfig
    from nshtrainer.callbacks import FiniteChecksConfig as FiniteChecksConfig
    from nshtrainer.callbacks import GradientSkippingConfig as GradientSkippingConfig
    from nshtrainer.callbacks import (
        LastCheckpointCallbackConfig as LastCheckpointCallbackConfig,
    )
    from nshtrainer.callbacks import NormLoggingConfig as NormLoggingConfig
    from nshtrainer.callbacks import (
        OnExceptionCheckpointCallbackConfig as OnExceptionCheckpointCallbackConfig,
    )
    from nshtrainer.callbacks import PrintTableMetricsConfig as PrintTableMetricsConfig
    from nshtrainer.callbacks import RLPSanityChecksConfig as RLPSanityChecksConfig
    from nshtrainer.callbacks import SharedParametersConfig as SharedParametersConfig
    from nshtrainer.callbacks import ThroughputMonitorConfig as ThroughputMonitorConfig
    from nshtrainer.callbacks import WandbUploadCodeConfig as WandbUploadCodeConfig
    from nshtrainer.callbacks import WandbWatchConfig as WandbWatchConfig
    from nshtrainer.callbacks.actsave import ActSaveConfig as ActSaveConfig
    from nshtrainer.callbacks.checkpoint._base import (
        BaseCheckpointCallbackConfig as BaseCheckpointCallbackConfig,
    )
    from nshtrainer.loggers import BaseLoggerConfig as BaseLoggerConfig
    from nshtrainer.loggers import CSVLoggerConfig as CSVLoggerConfig
    from nshtrainer.loggers import LoggerConfig as LoggerConfig
    from nshtrainer.loggers import TensorboardLoggerConfig as TensorboardLoggerConfig
    from nshtrainer.loggers import WandbLoggerConfig as WandbLoggerConfig
    from nshtrainer.lr_scheduler import (
        LinearWarmupCosineDecayLRSchedulerConfig as LinearWarmupCosineDecayLRSchedulerConfig,
    )
    from nshtrainer.lr_scheduler import LRSchedulerConfig as LRSchedulerConfig
    from nshtrainer.lr_scheduler import LRSchedulerConfigBase as LRSchedulerConfigBase
    from nshtrainer.lr_scheduler import (
        ReduceLROnPlateauConfig as ReduceLROnPlateauConfig,
    )
    from nshtrainer.model import DirectoryConfig as DirectoryConfig
    from nshtrainer.model import TrainerConfig as TrainerConfig
    from nshtrainer.model.base import EnvironmentConfig as EnvironmentConfig
    from nshtrainer.nn import BaseNonlinearityConfig as BaseNonlinearityConfig
    from nshtrainer.nn import ELUNonlinearityConfig as ELUNonlinearityConfig
    from nshtrainer.nn import GELUNonlinearityConfig as GELUNonlinearityConfig
    from nshtrainer.nn import LeakyReLUNonlinearityConfig as LeakyReLUNonlinearityConfig
    from nshtrainer.nn import MishNonlinearityConfig as MishNonlinearityConfig
    from nshtrainer.nn import MLPConfig as MLPConfig
    from nshtrainer.nn import NonlinearityConfig as NonlinearityConfig
    from nshtrainer.nn import PReLUConfig as PReLUConfig
    from nshtrainer.nn import ReLUNonlinearityConfig as ReLUNonlinearityConfig
    from nshtrainer.nn import SigmoidNonlinearityConfig as SigmoidNonlinearityConfig
    from nshtrainer.nn import SiLUNonlinearityConfig as SiLUNonlinearityConfig
    from nshtrainer.nn import SoftmaxNonlinearityConfig as SoftmaxNonlinearityConfig
    from nshtrainer.nn import SoftplusNonlinearityConfig as SoftplusNonlinearityConfig
    from nshtrainer.nn import SoftsignNonlinearityConfig as SoftsignNonlinearityConfig
    from nshtrainer.nn import SwishNonlinearityConfig as SwishNonlinearityConfig
    from nshtrainer.nn import TanhNonlinearityConfig as TanhNonlinearityConfig
    from nshtrainer.nn.nonlinearity import (
        SwiGLUNonlinearityConfig as SwiGLUNonlinearityConfig,
    )
    from nshtrainer.optimizer import AdamWConfig as AdamWConfig
    from nshtrainer.optimizer import OptimizerConfig as OptimizerConfig
    from nshtrainer.optimizer import OptimizerConfigBase as OptimizerConfigBase
    from nshtrainer.profiler import AdvancedProfilerConfig as AdvancedProfilerConfig
    from nshtrainer.profiler import BaseProfilerConfig as BaseProfilerConfig
    from nshtrainer.profiler import ProfilerConfig as ProfilerConfig
    from nshtrainer.profiler import PyTorchProfilerConfig as PyTorchProfilerConfig
    from nshtrainer.profiler import SimpleProfilerConfig as SimpleProfilerConfig
    from nshtrainer.trainer._config import (
        CheckpointCallbackConfig as CheckpointCallbackConfig,
    )
    from nshtrainer.trainer._config import (
        CheckpointLoadingConfig as CheckpointLoadingConfig,
    )
    from nshtrainer.trainer._config import (
        CheckpointSavingConfig as CheckpointSavingConfig,
    )
    from nshtrainer.trainer._config import (
        GradientClippingConfig as GradientClippingConfig,
    )
    from nshtrainer.trainer._config import LoggingConfig as LoggingConfig
    from nshtrainer.trainer._config import OptimizationConfig as OptimizationConfig
    from nshtrainer.trainer._config import (
        ReproducibilityConfig as ReproducibilityConfig,
    )
    from nshtrainer.trainer._config import SanityCheckingConfig as SanityCheckingConfig
    from nshtrainer.util._environment_info import (
        EnvironmentClassInformationConfig as EnvironmentClassInformationConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentCUDAConfig as EnvironmentCUDAConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentGPUConfig as EnvironmentGPUConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentHardwareConfig as EnvironmentHardwareConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentLinuxEnvironmentConfig as EnvironmentLinuxEnvironmentConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentLSFInformationConfig as EnvironmentLSFInformationConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentPackageConfig as EnvironmentPackageConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentSLURMInformationConfig as EnvironmentSLURMInformationConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentSnapshotConfig as EnvironmentSnapshotConfig,
    )
    from nshtrainer.util._environment_info import (
        GitRepositoryConfig as GitRepositoryConfig,
    )
    from nshtrainer.util.config import DTypeConfig as DTypeConfig
    from nshtrainer.util.config import DurationConfig as DurationConfig
    from nshtrainer.util.config import EpochsConfig as EpochsConfig
    from nshtrainer.util.config import StepsConfig as StepsConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "BaseConfig":
            return importlib.import_module("nshtrainer").BaseConfig
        if name == "MetricConfig":
            return importlib.import_module("nshtrainer").MetricConfig
        if name == "CallbackConfigBase":
            return importlib.import_module("nshtrainer._hf_hub").CallbackConfigBase
        if name == "HuggingFaceHubConfig":
            return importlib.import_module("nshtrainer._hf_hub").HuggingFaceHubConfig
        if name == "HuggingFaceHubAutoCreateConfig":
            return importlib.import_module(
                "nshtrainer._hf_hub"
            ).HuggingFaceHubAutoCreateConfig
        if name == "OptimizerConfigBase":
            return importlib.import_module("nshtrainer.optimizer").OptimizerConfigBase
        if name == "AdamWConfig":
            return importlib.import_module("nshtrainer.optimizer").AdamWConfig
        if name == "DirectoryConfig":
            return importlib.import_module("nshtrainer.model").DirectoryConfig
        if name == "DirectorySetupConfig":
            return importlib.import_module("nshtrainer.callbacks").DirectorySetupConfig
        if name == "TrainerConfig":
            return importlib.import_module("nshtrainer.model").TrainerConfig
        if name == "EnvironmentConfig":
            return importlib.import_module("nshtrainer.model.base").EnvironmentConfig
        if name == "BaseNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").BaseNonlinearityConfig
        if name == "MLPConfig":
            return importlib.import_module("nshtrainer.nn").MLPConfig
        if name == "SwiGLUNonlinearityConfig":
            return importlib.import_module(
                "nshtrainer.nn.nonlinearity"
            ).SwiGLUNonlinearityConfig
        if name == "ReLUNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").ReLUNonlinearityConfig
        if name == "SiLUNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").SiLUNonlinearityConfig
        if name == "ELUNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").ELUNonlinearityConfig
        if name == "GELUNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").GELUNonlinearityConfig
        if name == "SoftplusNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").SoftplusNonlinearityConfig
        if name == "SoftsignNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").SoftsignNonlinearityConfig
        if name == "SwishNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").SwishNonlinearityConfig
        if name == "SoftmaxNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").SoftmaxNonlinearityConfig
        if name == "MishNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").MishNonlinearityConfig
        if name == "SigmoidNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").SigmoidNonlinearityConfig
        if name == "TanhNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").TanhNonlinearityConfig
        if name == "PReLUConfig":
            return importlib.import_module("nshtrainer.nn").PReLUConfig
        if name == "LeakyReLUNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").LeakyReLUNonlinearityConfig
        if name == "LRSchedulerConfigBase":
            return importlib.import_module(
                "nshtrainer.lr_scheduler"
            ).LRSchedulerConfigBase
        if name == "LinearWarmupCosineDecayLRSchedulerConfig":
            return importlib.import_module(
                "nshtrainer.lr_scheduler"
            ).LinearWarmupCosineDecayLRSchedulerConfig
        if name == "ReduceLROnPlateauConfig":
            return importlib.import_module(
                "nshtrainer.lr_scheduler"
            ).ReduceLROnPlateauConfig
        if name == "BaseLoggerConfig":
            return importlib.import_module("nshtrainer.loggers").BaseLoggerConfig
        if name == "TensorboardLoggerConfig":
            return importlib.import_module("nshtrainer.loggers").TensorboardLoggerConfig
        if name == "WandbLoggerConfig":
            return importlib.import_module("nshtrainer.loggers").WandbLoggerConfig
        if name == "WandbUploadCodeConfig":
            return importlib.import_module("nshtrainer.callbacks").WandbUploadCodeConfig
        if name == "WandbWatchConfig":
            return importlib.import_module("nshtrainer.callbacks").WandbWatchConfig
        if name == "CSVLoggerConfig":
            return importlib.import_module("nshtrainer.loggers").CSVLoggerConfig
        if name == "EnvironmentPackageConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentPackageConfig
        if name == "EnvironmentSnapshotConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentSnapshotConfig
        if name == "EnvironmentLSFInformationConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentLSFInformationConfig
        if name == "EnvironmentLinuxEnvironmentConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentLinuxEnvironmentConfig
        if name == "EnvironmentSLURMInformationConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentSLURMInformationConfig
        if name == "EnvironmentClassInformationConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentClassInformationConfig
        if name == "GitRepositoryConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).GitRepositoryConfig
        if name == "EnvironmentCUDAConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentCUDAConfig
        if name == "EnvironmentGPUConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentGPUConfig
        if name == "EnvironmentHardwareConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentHardwareConfig
        if name == "EpochsConfig":
            return importlib.import_module("nshtrainer.util.config").EpochsConfig
        if name == "StepsConfig":
            return importlib.import_module("nshtrainer.util.config").StepsConfig
        if name == "DTypeConfig":
            return importlib.import_module("nshtrainer.util.config").DTypeConfig
        if name == "CheckpointLoadingConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).CheckpointLoadingConfig
        if name == "OptimizationConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).OptimizationConfig
        if name == "GradientClippingConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).GradientClippingConfig
        if name == "LastCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).LastCheckpointCallbackConfig
        if name == "OnExceptionCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).OnExceptionCheckpointCallbackConfig
        if name == "RLPSanityChecksConfig":
            return importlib.import_module("nshtrainer.callbacks").RLPSanityChecksConfig
        if name == "EarlyStoppingConfig":
            return importlib.import_module("nshtrainer.callbacks").EarlyStoppingConfig
        if name == "DebugFlagCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).DebugFlagCallbackConfig
        if name == "CheckpointSavingConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).CheckpointSavingConfig
        if name == "BestCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).BestCheckpointCallbackConfig
        if name == "LoggingConfig":
            return importlib.import_module("nshtrainer.trainer._config").LoggingConfig
        if name == "SanityCheckingConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).SanityCheckingConfig
        if name == "SharedParametersConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).SharedParametersConfig
        if name == "ReproducibilityConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).ReproducibilityConfig
        if name == "CheckpointMetadata":
            return importlib.import_module(
                "nshtrainer._checkpoint.loader"
            ).CheckpointMetadata
        if name == "BestCheckpointStrategyConfig":
            return importlib.import_module(
                "nshtrainer._checkpoint.loader"
            ).BestCheckpointStrategyConfig
        if name == "LastCheckpointStrategyConfig":
            return importlib.import_module(
                "nshtrainer._checkpoint.loader"
            ).LastCheckpointStrategyConfig
        if name == "UserProvidedPathCheckpointStrategyConfig":
            return importlib.import_module(
                "nshtrainer._checkpoint.loader"
            ).UserProvidedPathCheckpointStrategyConfig
        if name == "PrintTableMetricsConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).PrintTableMetricsConfig
        if name == "ThroughputMonitorConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).ThroughputMonitorConfig
        if name == "GradientSkippingConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).GradientSkippingConfig
        if name == "EMAConfig":
            return importlib.import_module("nshtrainer.callbacks").EMAConfig
        if name == "ActSaveConfig":
            return importlib.import_module("nshtrainer.callbacks.actsave").ActSaveConfig
        if name == "FiniteChecksConfig":
            return importlib.import_module("nshtrainer.callbacks").FiniteChecksConfig
        if name == "NormLoggingConfig":
            return importlib.import_module("nshtrainer.callbacks").NormLoggingConfig
        if name == "EpochTimerConfig":
            return importlib.import_module("nshtrainer.callbacks").EpochTimerConfig
        if name == "BaseCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint._base"
            ).BaseCheckpointCallbackConfig
        if name == "BaseProfilerConfig":
            return importlib.import_module("nshtrainer.profiler").BaseProfilerConfig
        if name == "PyTorchProfilerConfig":
            return importlib.import_module("nshtrainer.profiler").PyTorchProfilerConfig
        if name == "AdvancedProfilerConfig":
            return importlib.import_module("nshtrainer.profiler").AdvancedProfilerConfig
        if name == "SimpleProfilerConfig":
            return importlib.import_module("nshtrainer.profiler").SimpleProfilerConfig
        if name == "OptimizerConfig":
            return importlib.import_module("nshtrainer.optimizer").OptimizerConfig
        if name == "LoggerConfig":
            return importlib.import_module("nshtrainer.loggers").LoggerConfig
        if name == "NonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").NonlinearityConfig
        if name == "DurationConfig":
            return importlib.import_module("nshtrainer.util.config").DurationConfig
        if name == "LRSchedulerConfig":
            return importlib.import_module("nshtrainer.lr_scheduler").LRSchedulerConfig
        if name == "CallbackConfig":
            return importlib.import_module("nshtrainer.callbacks").CallbackConfig
        if name == "CheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).CheckpointCallbackConfig
        if name == "ProfilerConfig":
            return importlib.import_module("nshtrainer.profiler").ProfilerConfig
        if name == "CheckpointLoadingStrategyConfig":
            return importlib.import_module(
                "nshtrainer._checkpoint.loader"
            ).CheckpointLoadingStrategyConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# Submodule exports
from . import _checkpoint as _checkpoint
from . import _directory as _directory
from . import _hf_hub as _hf_hub
from . import callbacks as callbacks
from . import loggers as loggers
from . import lr_scheduler as lr_scheduler
from . import metrics as metrics
from . import model as model
from . import nn as nn
from . import optimizer as optimizer
from . import profiler as profiler
from . import runner as runner
from . import trainer as trainer
from . import util as util
