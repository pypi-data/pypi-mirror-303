__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.directory_setup import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.directory_setup import (
        DirectorySetupConfig as DirectorySetupConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.directory_setup"
            ).CallbackConfigBase
        if name == "DirectorySetupConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.directory_setup"
            ).DirectorySetupConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
