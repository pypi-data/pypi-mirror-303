from typing import Annotated

import nshconfig as C

from . import checkpoint as checkpoint
from .base import CallbackConfigBase as CallbackConfigBase
from .checkpoint import BestCheckpoint as BestCheckpoint
from .checkpoint import BestCheckpointCallbackConfig as BestCheckpointCallbackConfig
from .checkpoint import LastCheckpoint as LastCheckpoint
from .checkpoint import LastCheckpointCallbackConfig as LastCheckpointCallbackConfig
from .checkpoint import OnExceptionCheckpoint as OnExceptionCheckpoint
from .checkpoint import (
    OnExceptionCheckpointCallbackConfig as OnExceptionCheckpointCallbackConfig,
)
from .debug_flag import DebugFlagCallback as DebugFlagCallback
from .debug_flag import DebugFlagCallbackConfig as DebugFlagCallbackConfig
from .directory_setup import DirectorySetupCallback as DirectorySetupCallback
from .directory_setup import DirectorySetupConfig as DirectorySetupConfig
from .early_stopping import EarlyStopping as EarlyStopping
from .early_stopping import EarlyStoppingConfig as EarlyStoppingConfig
from .ema import EMA as EMA
from .ema import EMAConfig as EMAConfig
from .finite_checks import FiniteChecksCallback as FiniteChecksCallback
from .finite_checks import FiniteChecksConfig as FiniteChecksConfig
from .gradient_skipping import GradientSkipping as GradientSkipping
from .gradient_skipping import GradientSkippingConfig as GradientSkippingConfig
from .interval import EpochIntervalCallback as EpochIntervalCallback
from .interval import IntervalCallback as IntervalCallback
from .interval import StepIntervalCallback as StepIntervalCallback
from .log_epoch import LogEpochCallback as LogEpochCallback
from .norm_logging import NormLoggingCallback as NormLoggingCallback
from .norm_logging import NormLoggingConfig as NormLoggingConfig
from .print_table import PrintTableMetricsCallback as PrintTableMetricsCallback
from .print_table import PrintTableMetricsConfig as PrintTableMetricsConfig
from .rlp_sanity_checks import RLPSanityChecksCallback as RLPSanityChecksCallback
from .rlp_sanity_checks import RLPSanityChecksConfig as RLPSanityChecksConfig
from .shared_parameters import SharedParametersCallback as SharedParametersCallback
from .shared_parameters import SharedParametersConfig as SharedParametersConfig
from .throughput_monitor import ThroughputMonitorConfig as ThroughputMonitorConfig
from .timer import EpochTimer as EpochTimer
from .timer import EpochTimerConfig as EpochTimerConfig
from .wandb_upload_code import WandbUploadCodeCallback as WandbUploadCodeCallback
from .wandb_upload_code import WandbUploadCodeConfig as WandbUploadCodeConfig
from .wandb_watch import WandbWatchCallback as WandbWatchCallback
from .wandb_watch import WandbWatchConfig as WandbWatchConfig

CallbackConfig = Annotated[
    DebugFlagCallbackConfig
    | EarlyStoppingConfig
    | ThroughputMonitorConfig
    | EpochTimerConfig
    | PrintTableMetricsConfig
    | FiniteChecksConfig
    | NormLoggingConfig
    | GradientSkippingConfig
    | EMAConfig
    | BestCheckpointCallbackConfig
    | LastCheckpointCallbackConfig
    | OnExceptionCheckpointCallbackConfig
    | SharedParametersConfig
    | RLPSanityChecksConfig
    | WandbWatchConfig
    | WandbUploadCodeConfig,
    C.Field(discriminator="name"),
]
