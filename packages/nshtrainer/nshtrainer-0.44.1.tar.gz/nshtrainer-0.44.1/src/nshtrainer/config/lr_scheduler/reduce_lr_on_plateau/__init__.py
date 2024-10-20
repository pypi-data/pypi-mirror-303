from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.lr_scheduler.reduce_lr_on_plateau import (
        LRSchedulerConfigBase as LRSchedulerConfigBase,
    )
    from nshtrainer.lr_scheduler.reduce_lr_on_plateau import (
        MetricConfig as MetricConfig,
    )
    from nshtrainer.lr_scheduler.reduce_lr_on_plateau import (
        ReduceLROnPlateauConfig as ReduceLROnPlateauConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "LRSchedulerConfigBase":
            return importlib.import_module(
                "nshtrainer.lr_scheduler.reduce_lr_on_plateau"
            ).LRSchedulerConfigBase
        if name == "MetricConfig":
            return importlib.import_module(
                "nshtrainer.lr_scheduler.reduce_lr_on_plateau"
            ).MetricConfig
        if name == "ReduceLROnPlateauConfig":
            return importlib.import_module(
                "nshtrainer.lr_scheduler.reduce_lr_on_plateau"
            ).ReduceLROnPlateauConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
