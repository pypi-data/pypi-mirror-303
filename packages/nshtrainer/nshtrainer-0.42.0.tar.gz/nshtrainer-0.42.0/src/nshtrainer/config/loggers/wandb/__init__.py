__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.loggers.wandb import BaseLoggerConfig as BaseLoggerConfig
    from nshtrainer.loggers.wandb import CallbackConfigBase as CallbackConfigBase
    from nshtrainer.loggers.wandb import WandbLoggerConfig as WandbLoggerConfig
    from nshtrainer.loggers.wandb import WandbUploadCodeConfig as WandbUploadCodeConfig
    from nshtrainer.loggers.wandb import WandbWatchConfig as WandbWatchConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.loggers.wandb"
            ).CallbackConfigBase
        if name == "WandbLoggerConfig":
            return importlib.import_module("nshtrainer.loggers.wandb").WandbLoggerConfig
        if name == "WandbUploadCodeConfig":
            return importlib.import_module(
                "nshtrainer.loggers.wandb"
            ).WandbUploadCodeConfig
        if name == "WandbWatchConfig":
            return importlib.import_module("nshtrainer.loggers.wandb").WandbWatchConfig
        if name == "BaseLoggerConfig":
            return importlib.import_module("nshtrainer.loggers.wandb").BaseLoggerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
