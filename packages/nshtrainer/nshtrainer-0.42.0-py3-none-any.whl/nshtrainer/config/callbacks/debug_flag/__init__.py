__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.debug_flag import CallbackConfigBase as CallbackConfigBase
    from nshtrainer.callbacks.debug_flag import (
        DebugFlagCallbackConfig as DebugFlagCallbackConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.debug_flag"
            ).CallbackConfigBase
        if name == "DebugFlagCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.debug_flag"
            ).DebugFlagCallbackConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
