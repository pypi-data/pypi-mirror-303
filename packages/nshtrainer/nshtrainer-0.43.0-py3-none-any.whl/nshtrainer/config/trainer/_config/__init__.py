from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.trainer._config import (
        BestCheckpointCallbackConfig as BestCheckpointCallbackConfig,
    )
    from nshtrainer.trainer._config import CallbackConfig as CallbackConfig
    from nshtrainer.trainer._config import CallbackConfigBase as CallbackConfigBase
    from nshtrainer.trainer._config import (
        CheckpointCallbackConfig as CheckpointCallbackConfig,
    )
    from nshtrainer.trainer._config import (
        CheckpointLoadingConfig as CheckpointLoadingConfig,
    )
    from nshtrainer.trainer._config import (
        CheckpointSavingConfig as CheckpointSavingConfig,
    )
    from nshtrainer.trainer._config import CSVLoggerConfig as CSVLoggerConfig
    from nshtrainer.trainer._config import (
        DebugFlagCallbackConfig as DebugFlagCallbackConfig,
    )
    from nshtrainer.trainer._config import (
        EarlyStoppingCallbackConfig as EarlyStoppingCallbackConfig,
    )
    from nshtrainer.trainer._config import (
        GradientClippingConfig as GradientClippingConfig,
    )
    from nshtrainer.trainer._config import HuggingFaceHubConfig as HuggingFaceHubConfig
    from nshtrainer.trainer._config import (
        LastCheckpointCallbackConfig as LastCheckpointCallbackConfig,
    )
    from nshtrainer.trainer._config import LoggerConfig as LoggerConfig
    from nshtrainer.trainer._config import LoggingConfig as LoggingConfig
    from nshtrainer.trainer._config import (
        OnExceptionCheckpointCallbackConfig as OnExceptionCheckpointCallbackConfig,
    )
    from nshtrainer.trainer._config import OptimizationConfig as OptimizationConfig
    from nshtrainer.trainer._config import ProfilerConfig as ProfilerConfig
    from nshtrainer.trainer._config import (
        ReproducibilityConfig as ReproducibilityConfig,
    )
    from nshtrainer.trainer._config import (
        RLPSanityChecksCallbackConfig as RLPSanityChecksCallbackConfig,
    )
    from nshtrainer.trainer._config import SanityCheckingConfig as SanityCheckingConfig
    from nshtrainer.trainer._config import (
        SharedParametersCallbackConfig as SharedParametersCallbackConfig,
    )
    from nshtrainer.trainer._config import (
        TensorboardLoggerConfig as TensorboardLoggerConfig,
    )
    from nshtrainer.trainer._config import TrainerConfig as TrainerConfig
    from nshtrainer.trainer._config import WandbLoggerConfig as WandbLoggerConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "SanityCheckingConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).SanityCheckingConfig
        if name == "TrainerConfig":
            return importlib.import_module("nshtrainer.trainer._config").TrainerConfig
        if name == "OnExceptionCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).OnExceptionCheckpointCallbackConfig
        if name == "GradientClippingConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).GradientClippingConfig
        if name == "WandbLoggerConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).WandbLoggerConfig
        if name == "LoggingConfig":
            return importlib.import_module("nshtrainer.trainer._config").LoggingConfig
        if name == "TensorboardLoggerConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).TensorboardLoggerConfig
        if name == "RLPSanityChecksCallbackConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).RLPSanityChecksCallbackConfig
        if name == "CheckpointSavingConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).CheckpointSavingConfig
        if name == "CSVLoggerConfig":
            return importlib.import_module("nshtrainer.trainer._config").CSVLoggerConfig
        if name == "HuggingFaceHubConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).HuggingFaceHubConfig
        if name == "CheckpointLoadingConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).CheckpointLoadingConfig
        if name == "DebugFlagCallbackConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).DebugFlagCallbackConfig
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).CallbackConfigBase
        if name == "LastCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).LastCheckpointCallbackConfig
        if name == "SharedParametersCallbackConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).SharedParametersCallbackConfig
        if name == "ReproducibilityConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).ReproducibilityConfig
        if name == "EarlyStoppingCallbackConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).EarlyStoppingCallbackConfig
        if name == "OptimizationConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).OptimizationConfig
        if name == "BestCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).BestCheckpointCallbackConfig
        if name == "CallbackConfig":
            return importlib.import_module("nshtrainer.trainer._config").CallbackConfig
        if name == "CheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.trainer._config"
            ).CheckpointCallbackConfig
        if name == "LoggerConfig":
            return importlib.import_module("nshtrainer.trainer._config").LoggerConfig
        if name == "ProfilerConfig":
            return importlib.import_module("nshtrainer.trainer._config").ProfilerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
