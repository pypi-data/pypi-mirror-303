from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.checkpoint._base import (
        BaseCheckpointCallbackConfig as BaseCheckpointCallbackConfig,
    )
    from nshtrainer.callbacks.checkpoint._base import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.checkpoint._base import (
        CheckpointMetadata as CheckpointMetadata,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CheckpointMetadata":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint._base"
            ).CheckpointMetadata
        if name == "BaseCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint._base"
            ).BaseCheckpointCallbackConfig
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint._base"
            ).CallbackConfigBase
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
