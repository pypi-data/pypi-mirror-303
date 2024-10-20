from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.trainer.checkpoint_connector import (
        CheckpointLoadingConfig as CheckpointLoadingConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CheckpointLoadingConfig":
            return importlib.import_module(
                "nshtrainer.trainer.checkpoint_connector"
            ).CheckpointLoadingConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
