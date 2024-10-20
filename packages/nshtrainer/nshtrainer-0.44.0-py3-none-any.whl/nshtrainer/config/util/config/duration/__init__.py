from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.util.config.duration import DurationConfig as DurationConfig
    from nshtrainer.util.config.duration import EpochsConfig as EpochsConfig
    from nshtrainer.util.config.duration import StepsConfig as StepsConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "EpochsConfig":
            return importlib.import_module(
                "nshtrainer.util.config.duration"
            ).EpochsConfig
        if name == "StepsConfig":
            return importlib.import_module(
                "nshtrainer.util.config.duration"
            ).StepsConfig
        if name == "DurationConfig":
            return importlib.import_module(
                "nshtrainer.util.config.duration"
            ).DurationConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
