from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.norm_logging import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.norm_logging import (
        NormLoggingCallbackConfig as NormLoggingCallbackConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "NormLoggingCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.norm_logging"
            ).NormLoggingCallbackConfig
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.norm_logging"
            ).CallbackConfigBase
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
