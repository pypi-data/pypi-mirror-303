from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.profiler.advanced import (
        AdvancedProfilerConfig as AdvancedProfilerConfig,
    )
    from nshtrainer.profiler.advanced import BaseProfilerConfig as BaseProfilerConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "AdvancedProfilerConfig":
            return importlib.import_module(
                "nshtrainer.profiler.advanced"
            ).AdvancedProfilerConfig
        if name == "BaseProfilerConfig":
            return importlib.import_module(
                "nshtrainer.profiler.advanced"
            ).BaseProfilerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
