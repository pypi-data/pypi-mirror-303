__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.checkpoint.on_exception_checkpoint import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.checkpoint.on_exception_checkpoint import (
        OnExceptionCheckpointCallbackConfig as OnExceptionCheckpointCallbackConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint.on_exception_checkpoint"
            ).CallbackConfigBase
        if name == "OnExceptionCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint.on_exception_checkpoint"
            ).OnExceptionCheckpointCallbackConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
