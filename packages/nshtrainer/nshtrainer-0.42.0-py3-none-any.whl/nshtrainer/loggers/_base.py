from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import nshconfig as C
from lightning.pytorch.loggers import Logger

if TYPE_CHECKING:
    from ..model import BaseConfig


class BaseLoggerConfig(C.Config, ABC):
    enabled: bool = True
    """Enable this logger."""

    priority: int = 0
    """Priority of the logger. Higher priority loggers are created first."""

    log_dir: C.DirectoryPath | None = None
    """Directory to save the logs to. If None, will use the default log directory for the trainer."""

    @abstractmethod
    def create_logger(self, root_config: "BaseConfig") -> Logger | None: ...

    def disable_(self):
        self.enabled = False
        return self
