__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.wandb_watch import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.wandb_watch import WandbWatchConfig as WandbWatchConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.wandb_watch"
            ).CallbackConfigBase
        if name == "WandbWatchConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.wandb_watch"
            ).WandbWatchConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
