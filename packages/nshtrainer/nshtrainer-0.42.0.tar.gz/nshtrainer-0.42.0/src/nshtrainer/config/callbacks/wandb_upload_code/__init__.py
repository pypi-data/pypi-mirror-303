__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.wandb_upload_code import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.wandb_upload_code import (
        WandbUploadCodeConfig as WandbUploadCodeConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.wandb_upload_code"
            ).CallbackConfigBase
        if name == "WandbUploadCodeConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.wandb_upload_code"
            ).WandbUploadCodeConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
