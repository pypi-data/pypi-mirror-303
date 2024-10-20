from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.checkpoint.last_checkpoint import (
        BaseCheckpointCallbackConfig as BaseCheckpointCallbackConfig,
    )
    from nshtrainer.callbacks.checkpoint.last_checkpoint import (
        CheckpointMetadata as CheckpointMetadata,
    )
    from nshtrainer.callbacks.checkpoint.last_checkpoint import (
        LastCheckpointCallbackConfig as LastCheckpointCallbackConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CheckpointMetadata":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint.last_checkpoint"
            ).CheckpointMetadata
        if name == "BaseCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint.last_checkpoint"
            ).BaseCheckpointCallbackConfig
        if name == "LastCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint.last_checkpoint"
            ).LastCheckpointCallbackConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
