from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.model.config import BaseConfig as BaseConfig
    from nshtrainer.model.config import CallbackConfigBase as CallbackConfigBase
    from nshtrainer.model.config import DirectoryConfig as DirectoryConfig
    from nshtrainer.model.config import EnvironmentConfig as EnvironmentConfig
    from nshtrainer.model.config import MetricConfig as MetricConfig
    from nshtrainer.model.config import TrainerConfig as TrainerConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "MetricConfig":
            return importlib.import_module("nshtrainer.model.config").MetricConfig
        if name == "TrainerConfig":
            return importlib.import_module("nshtrainer.model.config").TrainerConfig
        if name == "BaseConfig":
            return importlib.import_module("nshtrainer.model.config").BaseConfig
        if name == "EnvironmentConfig":
            return importlib.import_module("nshtrainer.model.config").EnvironmentConfig
        if name == "DirectoryConfig":
            return importlib.import_module("nshtrainer.model.config").DirectoryConfig
        if name == "CallbackConfigBase":
            return importlib.import_module("nshtrainer.model.config").CallbackConfigBase
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
