from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.model import BaseConfig as BaseConfig
    from nshtrainer.model import DirectoryConfig as DirectoryConfig
    from nshtrainer.model import MetricConfig as MetricConfig
    from nshtrainer.model import TrainerConfig as TrainerConfig
    from nshtrainer.model.base import EnvironmentConfig as EnvironmentConfig
    from nshtrainer.model.config import CallbackConfigBase as CallbackConfigBase
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "MetricConfig":
            return importlib.import_module("nshtrainer.model").MetricConfig
        if name == "TrainerConfig":
            return importlib.import_module("nshtrainer.model").TrainerConfig
        if name == "BaseConfig":
            return importlib.import_module("nshtrainer.model").BaseConfig
        if name == "EnvironmentConfig":
            return importlib.import_module("nshtrainer.model.base").EnvironmentConfig
        if name == "DirectoryConfig":
            return importlib.import_module("nshtrainer.model").DirectoryConfig
        if name == "CallbackConfigBase":
            return importlib.import_module("nshtrainer.model.config").CallbackConfigBase
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# Submodule exports
from . import base as base
from . import config as config
from . import mixins as mixins
