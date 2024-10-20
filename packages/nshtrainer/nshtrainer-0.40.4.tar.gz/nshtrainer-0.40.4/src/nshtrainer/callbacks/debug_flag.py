import logging
from typing import TYPE_CHECKING, Literal, cast

from lightning.pytorch import LightningModule, Trainer
from lightning.pytorch.callbacks import Callback
from typing_extensions import override

from .base import CallbackConfigBase

if TYPE_CHECKING:
    from ..model.config import BaseConfig

log = logging.getLogger(__name__)


class DebugFlagCallbackConfig(CallbackConfigBase):
    name: Literal["debug_flag"] = "debug_flag"

    enabled: bool = True
    """Whether to enable the callback."""

    def __bool__(self):
        return self.enabled

    @override
    def create_callbacks(self, root_config):
        if not self:
            return

        yield DebugFlagCallback(self)


class DebugFlagCallback(Callback):
    """
    Sets the debug flag to true in the following circumstances:
    - fast_dev_run is enabled
    - sanity check is running
    """

    @override
    def __init__(self, config: DebugFlagCallbackConfig):
        super().__init__()

        self.config = config
        del config

    @override
    def setup(self, trainer: Trainer, pl_module: LightningModule, stage: str):
        if not getattr(trainer, "fast_dev_run", False):
            return

        hparams = cast("BaseConfig", pl_module.hparams)
        if not hparams.debug:
            log.critical("Fast dev run detected, setting debug flag to True.")
        hparams.debug = True

    @override
    def on_sanity_check_start(self, trainer: Trainer, pl_module: LightningModule):
        hparams = cast("BaseConfig", pl_module.hparams)
        self._debug = hparams.debug
        if not self._debug:
            log.critical("Enabling debug flag during sanity check routine.")
        hparams.debug = True

    @override
    def on_sanity_check_end(self, trainer: Trainer, pl_module: LightningModule):
        hparams = cast("BaseConfig", pl_module.hparams)
        if not self._debug:
            log.critical("Sanity check routine complete, disabling debug flag.")
        hparams.debug = self._debug
