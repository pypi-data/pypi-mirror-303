from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.loggers.csv import BaseLoggerConfig as BaseLoggerConfig
    from nshtrainer.loggers.csv import CSVLoggerConfig as CSVLoggerConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CSVLoggerConfig":
            return importlib.import_module("nshtrainer.loggers.csv").CSVLoggerConfig
        if name == "BaseLoggerConfig":
            return importlib.import_module("nshtrainer.loggers.csv").BaseLoggerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
