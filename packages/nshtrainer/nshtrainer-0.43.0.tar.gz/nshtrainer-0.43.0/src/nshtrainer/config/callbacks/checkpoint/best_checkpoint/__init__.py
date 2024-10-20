from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.checkpoint.best_checkpoint import (
        BaseCheckpointCallbackConfig as BaseCheckpointCallbackConfig,
    )
    from nshtrainer.callbacks.checkpoint.best_checkpoint import (
        BestCheckpointCallbackConfig as BestCheckpointCallbackConfig,
    )
    from nshtrainer.callbacks.checkpoint.best_checkpoint import (
        CheckpointMetadata as CheckpointMetadata,
    )
    from nshtrainer.callbacks.checkpoint.best_checkpoint import (
        MetricConfig as MetricConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CheckpointMetadata":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint.best_checkpoint"
            ).CheckpointMetadata
        if name == "BaseCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint.best_checkpoint"
            ).BaseCheckpointCallbackConfig
        if name == "MetricConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint.best_checkpoint"
            ).MetricConfig
        if name == "BestCheckpointCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.checkpoint.best_checkpoint"
            ).BestCheckpointCallbackConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
