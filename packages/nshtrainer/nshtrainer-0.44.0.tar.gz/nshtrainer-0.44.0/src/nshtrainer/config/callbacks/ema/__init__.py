from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.ema import CallbackConfigBase as CallbackConfigBase
    from nshtrainer.callbacks.ema import EMACallbackConfig as EMACallbackConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "EMACallbackConfig":
            return importlib.import_module("nshtrainer.callbacks.ema").EMACallbackConfig
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.ema"
            ).CallbackConfigBase
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
