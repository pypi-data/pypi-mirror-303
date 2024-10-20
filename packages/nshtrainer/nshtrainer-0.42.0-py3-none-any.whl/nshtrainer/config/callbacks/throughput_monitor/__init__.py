__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.throughput_monitor import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.throughput_monitor import (
        ThroughputMonitorConfig as ThroughputMonitorConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.throughput_monitor"
            ).CallbackConfigBase
        if name == "ThroughputMonitorConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.throughput_monitor"
            ).ThroughputMonitorConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
