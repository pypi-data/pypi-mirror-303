from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.util.config.dtype import DTypeConfig as DTypeConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "DTypeConfig":
            return importlib.import_module("nshtrainer.util.config.dtype").DTypeConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
