from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.wandb_upload_code import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.wandb_upload_code import (
        WandbUploadCodeCallbackConfig as WandbUploadCodeCallbackConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "WandbUploadCodeCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.wandb_upload_code"
            ).WandbUploadCodeCallbackConfig
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.wandb_upload_code"
            ).CallbackConfigBase
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
