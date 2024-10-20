__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.norm_logging import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.norm_logging import NormLoggingConfig as NormLoggingConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.norm_logging"
            ).CallbackConfigBase
        if name == "NormLoggingConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.norm_logging"
            ).NormLoggingConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
