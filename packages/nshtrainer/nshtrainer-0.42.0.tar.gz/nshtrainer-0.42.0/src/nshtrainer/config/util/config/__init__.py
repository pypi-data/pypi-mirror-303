__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.util.config import DTypeConfig as DTypeConfig
    from nshtrainer.util.config import DurationConfig as DurationConfig
    from nshtrainer.util.config import EpochsConfig as EpochsConfig
    from nshtrainer.util.config import StepsConfig as StepsConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "EpochsConfig":
            return importlib.import_module("nshtrainer.util.config").EpochsConfig
        if name == "StepsConfig":
            return importlib.import_module("nshtrainer.util.config").StepsConfig
        if name == "DTypeConfig":
            return importlib.import_module("nshtrainer.util.config").DTypeConfig
        if name == "DurationConfig":
            return importlib.import_module("nshtrainer.util.config").DurationConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# Submodule exports
from . import dtype as dtype
from . import duration as duration
