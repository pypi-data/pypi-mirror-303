from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.base import CallbackConfigBase as CallbackConfigBase
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.base"
            ).CallbackConfigBase
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
