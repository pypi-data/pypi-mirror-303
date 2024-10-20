from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.loggers.tensorboard import BaseLoggerConfig as BaseLoggerConfig
    from nshtrainer.loggers.tensorboard import (
        TensorboardLoggerConfig as TensorboardLoggerConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "BaseLoggerConfig":
            return importlib.import_module(
                "nshtrainer.loggers.tensorboard"
            ).BaseLoggerConfig
        if name == "TensorboardLoggerConfig":
            return importlib.import_module(
                "nshtrainer.loggers.tensorboard"
            ).TensorboardLoggerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
