from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.lr_scheduler._base import (
        LRSchedulerConfigBase as LRSchedulerConfigBase,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "LRSchedulerConfigBase":
            return importlib.import_module(
                "nshtrainer.lr_scheduler._base"
            ).LRSchedulerConfigBase
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
