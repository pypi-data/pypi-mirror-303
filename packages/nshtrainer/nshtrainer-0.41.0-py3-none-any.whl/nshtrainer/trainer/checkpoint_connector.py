import logging
from pathlib import Path
from typing import TYPE_CHECKING, cast

from lightning.pytorch.trainer.connectors.checkpoint_connector import (
    _CheckpointConnector as _LightningCheckpointConnector,
)
from lightning.pytorch.trainer.states import TrainerFn
from typing_extensions import override

from .._checkpoint.loader import CheckpointLoadingConfig, _resolve_checkpoint

if TYPE_CHECKING:
    from ..model.config import BaseConfig
log = logging.getLogger(__name__)


class _CheckpointConnector(_LightningCheckpointConnector):
    def __resolve_auto_ckpt_path(
        self,
        ckpt_path: str | Path | None,
        state_fn: TrainerFn,
    ):
        from .trainer import Trainer

        # If this isn't an `nshtrainer` trainer (which I don't know why it wouldn't be),
        # then we just default to the parent class's implementation of `_parse_ckpt_path`.
        trainer = self.trainer
        if not isinstance(trainer, Trainer):
            return None

        # Now, resolve the checkpoint loader config.
        root_config = cast("BaseConfig", trainer._base_module.config)
        ckpt_loader_config = root_config.trainer.checkpoint_loading
        match ckpt_loader_config:
            case "auto":
                ckpt_loader_config = CheckpointLoadingConfig.auto(ckpt_path, state_fn)
            case "none":
                ckpt_loader_config = CheckpointLoadingConfig.none()
            case _:
                pass
        log.debug(f"Checkpoint loader config: {ckpt_loader_config}")

        # Use the config to resolve the checkpoint.
        if (
            ckpt_path := _resolve_checkpoint(ckpt_loader_config, root_config, trainer)
        ) is None:
            log.info(
                "No checkpoint found for the current trainer state. "
                "Training will start from scratch."
            )

        log.info(f"Loading checkpoint from: {ckpt_path}")
        return ckpt_path

    @override
    def _parse_ckpt_path(
        self,
        state_fn: TrainerFn,
        ckpt_path: str | Path | None,
        model_provided: bool,
        model_connected: bool,
    ):
        if (p := self.__resolve_auto_ckpt_path(ckpt_path, state_fn)) is not None:
            return p

        return super()._parse_ckpt_path(
            state_fn, ckpt_path, model_provided, model_connected
        )
