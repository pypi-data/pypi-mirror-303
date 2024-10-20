from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.loggers.wandb import BaseLoggerConfig as BaseLoggerConfig
    from nshtrainer.loggers.wandb import CallbackConfigBase as CallbackConfigBase
    from nshtrainer.loggers.wandb import WandbLoggerConfig as WandbLoggerConfig
    from nshtrainer.loggers.wandb import (
        WandbUploadCodeCallbackConfig as WandbUploadCodeCallbackConfig,
    )
    from nshtrainer.loggers.wandb import (
        WandbWatchCallbackConfig as WandbWatchCallbackConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "WandbLoggerConfig":
            return importlib.import_module("nshtrainer.loggers.wandb").WandbLoggerConfig
        if name == "WandbUploadCodeCallbackConfig":
            return importlib.import_module(
                "nshtrainer.loggers.wandb"
            ).WandbUploadCodeCallbackConfig
        if name == "WandbWatchCallbackConfig":
            return importlib.import_module(
                "nshtrainer.loggers.wandb"
            ).WandbWatchCallbackConfig
        if name == "BaseLoggerConfig":
            return importlib.import_module("nshtrainer.loggers.wandb").BaseLoggerConfig
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.loggers.wandb"
            ).CallbackConfigBase
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
