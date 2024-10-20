__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.early_stopping import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.early_stopping import (
        EarlyStoppingConfig as EarlyStoppingConfig,
    )
    from nshtrainer.callbacks.early_stopping import MetricConfig as MetricConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.early_stopping"
            ).CallbackConfigBase
        if name == "MetricConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.early_stopping"
            ).MetricConfig
        if name == "EarlyStoppingConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.early_stopping"
            ).EarlyStoppingConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
