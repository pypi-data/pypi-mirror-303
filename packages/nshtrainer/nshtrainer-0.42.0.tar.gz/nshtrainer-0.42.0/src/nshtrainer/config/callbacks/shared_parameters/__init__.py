__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.shared_parameters import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.shared_parameters import (
        SharedParametersConfig as SharedParametersConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.shared_parameters"
            ).CallbackConfigBase
        if name == "SharedParametersConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.shared_parameters"
            ).SharedParametersConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
