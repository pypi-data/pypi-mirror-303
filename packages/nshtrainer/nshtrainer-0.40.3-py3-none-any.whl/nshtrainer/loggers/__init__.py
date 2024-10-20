from typing import Annotated, TypeAlias

import nshconfig as C

from ._base import BaseLoggerConfig as BaseLoggerConfig
from .csv import CSVLoggerConfig as CSVLoggerConfig
from .tensorboard import TensorboardLoggerConfig as TensorboardLoggerConfig
from .wandb import WandbLoggerConfig as WandbLoggerConfig

LoggerConfig: TypeAlias = Annotated[
    CSVLoggerConfig | TensorboardLoggerConfig | WandbLoggerConfig,
    C.Field(discriminator="name"),
]
