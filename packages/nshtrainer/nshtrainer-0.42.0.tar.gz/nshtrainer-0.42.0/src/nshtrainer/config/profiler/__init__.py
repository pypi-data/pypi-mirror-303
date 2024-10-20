__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.profiler import AdvancedProfilerConfig as AdvancedProfilerConfig
    from nshtrainer.profiler import BaseProfilerConfig as BaseProfilerConfig
    from nshtrainer.profiler import ProfilerConfig as ProfilerConfig
    from nshtrainer.profiler import PyTorchProfilerConfig as PyTorchProfilerConfig
    from nshtrainer.profiler import SimpleProfilerConfig as SimpleProfilerConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "BaseProfilerConfig":
            return importlib.import_module("nshtrainer.profiler").BaseProfilerConfig
        if name == "PyTorchProfilerConfig":
            return importlib.import_module("nshtrainer.profiler").PyTorchProfilerConfig
        if name == "AdvancedProfilerConfig":
            return importlib.import_module("nshtrainer.profiler").AdvancedProfilerConfig
        if name == "SimpleProfilerConfig":
            return importlib.import_module("nshtrainer.profiler").SimpleProfilerConfig
        if name == "ProfilerConfig":
            return importlib.import_module("nshtrainer.profiler").ProfilerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# Submodule exports
from . import _base as _base
from . import advanced as advanced
from . import pytorch as pytorch
from . import simple as simple
