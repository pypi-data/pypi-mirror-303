from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.directory_setup import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.directory_setup import (
        DirectorySetupCallbackConfig as DirectorySetupCallbackConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "DirectorySetupCallbackConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.directory_setup"
            ).DirectorySetupCallbackConfig
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.directory_setup"
            ).CallbackConfigBase
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
