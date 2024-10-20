from __future__ import annotations

__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.profiler.simple import BaseProfilerConfig as BaseProfilerConfig
    from nshtrainer.profiler.simple import SimpleProfilerConfig as SimpleProfilerConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "SimpleProfilerConfig":
            return importlib.import_module(
                "nshtrainer.profiler.simple"
            ).SimpleProfilerConfig
        if name == "BaseProfilerConfig":
            return importlib.import_module(
                "nshtrainer.profiler.simple"
            ).BaseProfilerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
