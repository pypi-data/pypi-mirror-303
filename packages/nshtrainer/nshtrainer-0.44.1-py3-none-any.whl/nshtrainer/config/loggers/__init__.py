from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.loggers import BaseLoggerConfig as BaseLoggerConfig
    from nshtrainer.loggers import CSVLoggerConfig as CSVLoggerConfig
    from nshtrainer.loggers import LoggerConfig as LoggerConfig
    from nshtrainer.loggers import TensorboardLoggerConfig as TensorboardLoggerConfig
    from nshtrainer.loggers import WandbLoggerConfig as WandbLoggerConfig
    from nshtrainer.loggers.wandb import CallbackConfigBase as CallbackConfigBase
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
        if name == "BaseLoggerConfig":
            return importlib.import_module("nshtrainer.loggers").BaseLoggerConfig
        if name == "TensorboardLoggerConfig":
            return importlib.import_module("nshtrainer.loggers").TensorboardLoggerConfig
        if name == "WandbLoggerConfig":
            return importlib.import_module("nshtrainer.loggers").WandbLoggerConfig
        if name == "WandbUploadCodeCallbackConfig":
            return importlib.import_module(
                "nshtrainer.loggers.wandb"
            ).WandbUploadCodeCallbackConfig
        if name == "WandbWatchCallbackConfig":
            return importlib.import_module(
                "nshtrainer.loggers.wandb"
            ).WandbWatchCallbackConfig
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.loggers.wandb"
            ).CallbackConfigBase
        if name == "CSVLoggerConfig":
            return importlib.import_module("nshtrainer.loggers").CSVLoggerConfig
        if name == "LoggerConfig":
            return importlib.import_module("nshtrainer.loggers").LoggerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# Submodule exports
from . import _base as _base
from . import csv as csv
from . import tensorboard as tensorboard
from . import wandb as wandb
