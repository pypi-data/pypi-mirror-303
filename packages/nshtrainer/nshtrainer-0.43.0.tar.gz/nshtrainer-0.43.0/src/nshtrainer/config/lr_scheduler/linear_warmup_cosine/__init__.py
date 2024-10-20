from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.lr_scheduler.linear_warmup_cosine import (
        DurationConfig as DurationConfig,
    )
    from nshtrainer.lr_scheduler.linear_warmup_cosine import (
        LinearWarmupCosineDecayLRSchedulerConfig as LinearWarmupCosineDecayLRSchedulerConfig,
    )
    from nshtrainer.lr_scheduler.linear_warmup_cosine import (
        LRSchedulerConfigBase as LRSchedulerConfigBase,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "LinearWarmupCosineDecayLRSchedulerConfig":
            return importlib.import_module(
                "nshtrainer.lr_scheduler.linear_warmup_cosine"
            ).LinearWarmupCosineDecayLRSchedulerConfig
        if name == "LRSchedulerConfigBase":
            return importlib.import_module(
                "nshtrainer.lr_scheduler.linear_warmup_cosine"
            ).LRSchedulerConfigBase
        if name == "DurationConfig":
            return importlib.import_module(
                "nshtrainer.lr_scheduler.linear_warmup_cosine"
            ).DurationConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
