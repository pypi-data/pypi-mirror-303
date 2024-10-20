# fmt: off
# ruff: noqa
# type: ignore

__codegen__ = True

# Config classes
from nshtrainer.lr_scheduler import LRSchedulerConfigBase as LRSchedulerConfigBase
from nshtrainer.lr_scheduler import LinearWarmupCosineDecayLRSchedulerConfig as LinearWarmupCosineDecayLRSchedulerConfig
from nshtrainer.lr_scheduler import ReduceLROnPlateauConfig as ReduceLROnPlateauConfig
from nshtrainer.lr_scheduler.reduce_lr_on_plateau import MetricConfig as MetricConfig

# Type aliases
from nshtrainer.lr_scheduler.linear_warmup_cosine import DurationConfig as DurationConfig
from nshtrainer.lr_scheduler import LRSchedulerConfig as LRSchedulerConfig

# Submodule exports
from . import _base as _base
from . import linear_warmup_cosine as linear_warmup_cosine
from . import reduce_lr_on_plateau as reduce_lr_on_plateau
