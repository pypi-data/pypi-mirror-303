# fmt: off
# ruff: noqa
# type: ignore

__codegen__ = True

# Config classes
from nshtrainer.loggers import TensorboardLoggerConfig as TensorboardLoggerConfig
from nshtrainer.loggers import BaseLoggerConfig as BaseLoggerConfig
from nshtrainer.loggers import WandbLoggerConfig as WandbLoggerConfig
from nshtrainer.loggers.wandb import WandbUploadCodeConfig as WandbUploadCodeConfig
from nshtrainer.loggers.wandb import CallbackConfigBase as CallbackConfigBase
from nshtrainer.loggers.wandb import WandbWatchConfig as WandbWatchConfig
from nshtrainer.loggers import CSVLoggerConfig as CSVLoggerConfig

# Type aliases
from nshtrainer.loggers import LoggerConfig as LoggerConfig

# Submodule exports
from . import _base as _base
from . import csv as csv
from . import tensorboard as tensorboard
from . import wandb as wandb
