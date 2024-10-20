__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.finite_checks import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.finite_checks import (
        FiniteChecksConfig as FiniteChecksConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.finite_checks"
            ).CallbackConfigBase
        if name == "FiniteChecksConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.finite_checks"
            ).FiniteChecksConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
