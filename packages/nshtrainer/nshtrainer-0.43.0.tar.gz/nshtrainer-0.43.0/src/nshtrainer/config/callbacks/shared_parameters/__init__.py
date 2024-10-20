from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.shared_parameters import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.shared_parameters import (
        SharedParametersCallbackConfig as SharedParametersCallbackConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "SharedParametersCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.shared_parameters"
            ).SharedParametersCallbackConfig
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.shared_parameters"
            ).CallbackConfigBase
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
