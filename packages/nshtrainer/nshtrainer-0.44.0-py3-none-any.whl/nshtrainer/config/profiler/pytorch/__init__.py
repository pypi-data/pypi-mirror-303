from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.profiler.pytorch import BaseProfilerConfig as BaseProfilerConfig
    from nshtrainer.profiler.pytorch import (
        PyTorchProfilerConfig as PyTorchProfilerConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "PyTorchProfilerConfig":
            return importlib.import_module(
                "nshtrainer.profiler.pytorch"
            ).PyTorchProfilerConfig
        if name == "BaseProfilerConfig":
            return importlib.import_module(
                "nshtrainer.profiler.pytorch"
            ).BaseProfilerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
