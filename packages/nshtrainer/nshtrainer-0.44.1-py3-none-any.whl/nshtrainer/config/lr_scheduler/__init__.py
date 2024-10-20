from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.lr_scheduler import (
        LinearWarmupCosineDecayLRSchedulerConfig as LinearWarmupCosineDecayLRSchedulerConfig,
    )
    from nshtrainer.lr_scheduler import LRSchedulerConfig as LRSchedulerConfig
    from nshtrainer.lr_scheduler import LRSchedulerConfigBase as LRSchedulerConfigBase
    from nshtrainer.lr_scheduler import (
        ReduceLROnPlateauConfig as ReduceLROnPlateauConfig,
    )
    from nshtrainer.lr_scheduler.linear_warmup_cosine import (
        DurationConfig as DurationConfig,
    )
    from nshtrainer.lr_scheduler.reduce_lr_on_plateau import (
        MetricConfig as MetricConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "LRSchedulerConfigBase":
            return importlib.import_module(
                "nshtrainer.lr_scheduler"
            ).LRSchedulerConfigBase
        if name == "LinearWarmupCosineDecayLRSchedulerConfig":
            return importlib.import_module(
                "nshtrainer.lr_scheduler"
            ).LinearWarmupCosineDecayLRSchedulerConfig
        if name == "MetricConfig":
            return importlib.import_module(
                "nshtrainer.lr_scheduler.reduce_lr_on_plateau"
            ).MetricConfig
        if name == "ReduceLROnPlateauConfig":
            return importlib.import_module(
                "nshtrainer.lr_scheduler"
            ).ReduceLROnPlateauConfig
        if name == "DurationConfig":
            return importlib.import_module(
                "nshtrainer.lr_scheduler.linear_warmup_cosine"
            ).DurationConfig
        if name == "LRSchedulerConfig":
            return importlib.import_module("nshtrainer.lr_scheduler").LRSchedulerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# Submodule exports
from . import _base as _base
from . import linear_warmup_cosine as linear_warmup_cosine
from . import reduce_lr_on_plateau as reduce_lr_on_plateau
