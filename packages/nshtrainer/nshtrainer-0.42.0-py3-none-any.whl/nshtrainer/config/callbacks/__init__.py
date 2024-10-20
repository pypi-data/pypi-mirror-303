__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks import (
        BestCheckpointCallbackConfig as BestCheckpointCallbackConfig,
    )
    from nshtrainer.callbacks import CallbackConfig as CallbackConfig
    from nshtrainer.callbacks import CallbackConfigBase as CallbackConfigBase
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
    from nshtrainer.callbacks.checkpoint._base import (
        CheckpointMetadata as CheckpointMetadata,
    )
    from nshtrainer.callbacks.early_stopping import MetricConfig as MetricConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module("nshtrainer.callbacks").CallbackConfigBase
        if name == "PrintTableMetricsConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).PrintTableMetricsConfig
        if name == "DebugFlagCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).DebugFlagCallbackConfig
        if name == "ThroughputMonitorConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).ThroughputMonitorConfig
        if name == "GradientSkippingConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).GradientSkippingConfig
        if name == "RLPSanityChecksConfig":
            return importlib.import_module("nshtrainer.callbacks").RLPSanityChecksConfig
        if name == "WandbUploadCodeConfig":
            return importlib.import_module("nshtrainer.callbacks").WandbUploadCodeConfig
        if name == "MetricConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.early_stopping"
            ).MetricConfig
        if name == "EarlyStoppingConfig":
            return importlib.import_module("nshtrainer.callbacks").EarlyStoppingConfig
        if name == "WandbWatchConfig":
            return importlib.import_module("nshtrainer.callbacks").WandbWatchConfig
        if name == "EMAConfig":
            return importlib.import_module("nshtrainer.callbacks").EMAConfig
        if name == "DirectorySetupConfig":
            return importlib.import_module("nshtrainer.callbacks").DirectorySetupConfig
        if name == "ActSaveConfig":
            return importlib.import_module("nshtrainer.callbacks.actsave").ActSaveConfig
        if name == "FiniteChecksConfig":
            return importlib.import_module("nshtrainer.callbacks").FiniteChecksConfig
        if name == "NormLoggingConfig":
            return importlib.import_module("nshtrainer.callbacks").NormLoggingConfig
        if name == "LastCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).LastCheckpointCallbackConfig
        if name == "BestCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).BestCheckpointCallbackConfig
        if name == "OnExceptionCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).OnExceptionCheckpointCallbackConfig
        if name == "EpochTimerConfig":
            return importlib.import_module("nshtrainer.callbacks").EpochTimerConfig
        if name == "SharedParametersConfig":
            return importlib.import_module(
                "nshtrainer.callbacks"
            ).SharedParametersConfig
        if name == "CheckpointMetadata":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint._base"
            ).CheckpointMetadata
        if name == "BaseCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint._base"
            ).BaseCheckpointCallbackConfig
        if name == "CallbackConfig":
            return importlib.import_module("nshtrainer.callbacks").CallbackConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# Submodule exports
from . import actsave as actsave
from . import base as base
from . import checkpoint as checkpoint
from . import debug_flag as debug_flag
from . import directory_setup as directory_setup
from . import early_stopping as early_stopping
from . import ema as ema
from . import finite_checks as finite_checks
from . import gradient_skipping as gradient_skipping
from . import norm_logging as norm_logging
from . import print_table as print_table
from . import rlp_sanity_checks as rlp_sanity_checks
from . import shared_parameters as shared_parameters
from . import throughput_monitor as throughput_monitor
from . import timer as timer
from . import wandb_upload_code as wandb_upload_code
from . import wandb_watch as wandb_watch
