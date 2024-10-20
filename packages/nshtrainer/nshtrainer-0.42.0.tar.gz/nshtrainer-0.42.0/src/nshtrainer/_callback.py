from pathlib import Path
from typing import TYPE_CHECKING

from lightning.pytorch.callbacks import Callback as _LightningCallback

if TYPE_CHECKING:
    from .model import LightningModuleBase
    from .trainer import Trainer


class NTCallbackBase(_LightningCallback):
    def on_checkpoint_saved(
        self,
        ckpt_path: Path,
        metadata_path: Path | None,
        trainer: "Trainer",
        pl_module: "LightningModuleBase",
    ) -> None:
        """Called after a checkpoint is saved."""
        pass


def _call_on_checkpoint_saved(
    trainer: "Trainer",
    ckpt_path: str | Path,
    metadata_path: str | Path | None,
):
    ckpt_path = Path(ckpt_path)
    metadata_path = Path(metadata_path) if metadata_path else None

    for callback in trainer.callbacks:
        if not isinstance(callback, NTCallbackBase):
            continue

        callback.on_checkpoint_saved(
            ckpt_path,
            metadata_path,
            trainer,
            trainer._base_module,
        )
