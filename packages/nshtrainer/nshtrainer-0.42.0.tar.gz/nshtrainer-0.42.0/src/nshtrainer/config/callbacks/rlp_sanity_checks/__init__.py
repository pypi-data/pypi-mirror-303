__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.rlp_sanity_checks import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.rlp_sanity_checks import (
        RLPSanityChecksConfig as RLPSanityChecksConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.rlp_sanity_checks"
            ).CallbackConfigBase
        if name == "RLPSanityChecksConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.rlp_sanity_checks"
            ).RLPSanityChecksConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
