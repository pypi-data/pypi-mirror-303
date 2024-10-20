__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.gradient_skipping import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.gradient_skipping import (
        GradientSkippingConfig as GradientSkippingConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.gradient_skipping"
            ).CallbackConfigBase
        if name == "GradientSkippingConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.gradient_skipping"
            ).GradientSkippingConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
