from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.loggers._base import BaseLoggerConfig as BaseLoggerConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "BaseLoggerConfig":
            return importlib.import_module("nshtrainer.loggers._base").BaseLoggerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
