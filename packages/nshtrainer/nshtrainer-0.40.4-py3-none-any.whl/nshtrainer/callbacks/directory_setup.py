import logging
import os
from pathlib import Path
from typing import Literal

from lightning.pytorch import Callback
from typing_extensions import override

from .base import CallbackConfigBase

log = logging.getLogger(__name__)


def _create_symlink_to_nshrunner(base_dir: Path):
    # Resolve the current nshrunner session directory
    if not (session_dir := os.environ.get("NSHRUNNER_SESSION_DIR")):
        log.warning("NSHRUNNER_SESSION_DIR is not set. Skipping symlink creation.")
        return
    session_dir = Path(session_dir)
    if not session_dir.exists() or not session_dir.is_dir():
        log.warning(
            f"NSHRUNNER_SESSION_DIR is not a valid directory: {session_dir}. "
            "Skipping symlink creation."
        )
        return

    # Create the symlink
    symlink_path = base_dir / "nshrunner"
    if symlink_path.exists():
        # If it already points to the correct directory, we're done
        if symlink_path.resolve() == session_dir.resolve():
            return

        # Otherwise, we should log a warning and remove the existing symlink
        log.warning(
            f"A symlink pointing to {symlink_path.resolve()} already exists at {symlink_path}. "
            "Removing the existing symlink."
        )
        symlink_path.unlink()

    symlink_path.symlink_to(session_dir)


class DirectorySetupConfig(CallbackConfigBase):
    name: Literal["directory_setup"] = "directory_setup"

    enabled: bool = True
    """Whether to enable the directory setup callback."""

    create_symlink_to_nshrunner_root: bool = True
    """Should we create a symlink to the root folder for the Runner (if we're in one)?"""

    def __bool__(self):
        return self.enabled

    def create_callbacks(self, root_config):
        if not self:
            return

        yield DirectorySetupCallback(self)


class DirectorySetupCallback(Callback):
    @override
    def __init__(self, config: DirectorySetupConfig):
        super().__init__()

        self.config = config
        del config

    @override
    def setup(self, trainer, pl_module, stage):
        super().setup(trainer, pl_module, stage)

        # Create a symlink to the root folder for the Runner
        if self.config.create_symlink_to_nshrunner_root:
            # Resolve the base dir
            from ..model.config import BaseConfig

            assert isinstance(
                config := pl_module.hparams, BaseConfig
            ), f"Expected a BaseConfig, got {type(config)}"

            base_dir = config.directory.resolve_run_root_directory(config.id)
            _create_symlink_to_nshrunner(base_dir)
