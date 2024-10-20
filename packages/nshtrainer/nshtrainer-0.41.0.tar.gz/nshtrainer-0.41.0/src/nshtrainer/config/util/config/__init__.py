# fmt: off
# ruff: noqa
# type: ignore

__codegen__ = True

# Config classes
from nshtrainer.util.config import EpochsConfig as EpochsConfig
from nshtrainer.util.config import StepsConfig as StepsConfig
from nshtrainer.util.config import DTypeConfig as DTypeConfig

# Type aliases
from nshtrainer.util.config import DurationConfig as DurationConfig

# Submodule exports
from . import dtype as dtype
from . import duration as duration
