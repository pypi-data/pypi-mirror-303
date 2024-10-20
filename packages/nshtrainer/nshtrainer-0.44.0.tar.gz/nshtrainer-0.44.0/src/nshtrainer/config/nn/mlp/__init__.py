from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.nn.mlp import BaseNonlinearityConfig as BaseNonlinearityConfig
    from nshtrainer.nn.mlp import MLPConfig as MLPConfig
    from nshtrainer.nn.mlp import NonlinearityConfig as NonlinearityConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "BaseNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn.mlp").BaseNonlinearityConfig
        if name == "MLPConfig":
            return importlib.import_module("nshtrainer.nn.mlp").MLPConfig
        if name == "NonlinearityConfig":
            return importlib.import_module("nshtrainer.nn.mlp").NonlinearityConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
