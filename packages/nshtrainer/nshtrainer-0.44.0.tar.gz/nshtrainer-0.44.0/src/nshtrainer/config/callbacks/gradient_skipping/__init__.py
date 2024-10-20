from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.gradient_skipping import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.gradient_skipping import (
        GradientSkippingCallbackConfig as GradientSkippingCallbackConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "GradientSkippingCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.gradient_skipping"
            ).GradientSkippingCallbackConfig
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.gradient_skipping"
            ).CallbackConfigBase
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
