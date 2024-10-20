from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.nn import BaseNonlinearityConfig as BaseNonlinearityConfig
    from nshtrainer.nn import ELUNonlinearityConfig as ELUNonlinearityConfig
    from nshtrainer.nn import GELUNonlinearityConfig as GELUNonlinearityConfig
    from nshtrainer.nn import LeakyReLUNonlinearityConfig as LeakyReLUNonlinearityConfig
    from nshtrainer.nn import MishNonlinearityConfig as MishNonlinearityConfig
    from nshtrainer.nn import MLPConfig as MLPConfig
    from nshtrainer.nn import NonlinearityConfig as NonlinearityConfig
    from nshtrainer.nn import PReLUConfig as PReLUConfig
    from nshtrainer.nn import ReLUNonlinearityConfig as ReLUNonlinearityConfig
    from nshtrainer.nn import SigmoidNonlinearityConfig as SigmoidNonlinearityConfig
    from nshtrainer.nn import SiLUNonlinearityConfig as SiLUNonlinearityConfig
    from nshtrainer.nn import SoftmaxNonlinearityConfig as SoftmaxNonlinearityConfig
    from nshtrainer.nn import SoftplusNonlinearityConfig as SoftplusNonlinearityConfig
    from nshtrainer.nn import SoftsignNonlinearityConfig as SoftsignNonlinearityConfig
    from nshtrainer.nn import SwishNonlinearityConfig as SwishNonlinearityConfig
    from nshtrainer.nn import TanhNonlinearityConfig as TanhNonlinearityConfig
    from nshtrainer.nn.nonlinearity import (
        SwiGLUNonlinearityConfig as SwiGLUNonlinearityConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "BaseNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").BaseNonlinearityConfig
        if name == "MLPConfig":
            return importlib.import_module("nshtrainer.nn").MLPConfig
        if name == "PReLUConfig":
            return importlib.import_module("nshtrainer.nn").PReLUConfig
        if name == "LeakyReLUNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").LeakyReLUNonlinearityConfig
        if name == "SwiGLUNonlinearityConfig":
            return importlib.import_module(
                "nshtrainer.nn.nonlinearity"
            ).SwiGLUNonlinearityConfig
        if name == "SoftsignNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").SoftsignNonlinearityConfig
        if name == "SiLUNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").SiLUNonlinearityConfig
        if name == "SigmoidNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").SigmoidNonlinearityConfig
        if name == "SoftplusNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").SoftplusNonlinearityConfig
        if name == "ELUNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").ELUNonlinearityConfig
        if name == "SoftmaxNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").SoftmaxNonlinearityConfig
        if name == "GELUNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").GELUNonlinearityConfig
        if name == "SwishNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").SwishNonlinearityConfig
        if name == "MishNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").MishNonlinearityConfig
        if name == "TanhNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").TanhNonlinearityConfig
        if name == "ReLUNonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").ReLUNonlinearityConfig
        if name == "NonlinearityConfig":
            return importlib.import_module("nshtrainer.nn").NonlinearityConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# Submodule exports
from . import mlp as mlp
from . import nonlinearity as nonlinearity
