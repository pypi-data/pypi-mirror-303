__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.callbacks.print_table import (
        CallbackConfigBase as CallbackConfigBase,
    )
    from nshtrainer.callbacks.print_table import (
        PrintTableMetricsConfig as PrintTableMetricsConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module(
                "nshtrainer.callbacks.print_table"
            ).CallbackConfigBase
        if name == "PrintTableMetricsConfig":
            return importlib.import_module(
                "nshtrainer.callbacks.print_table"
            ).PrintTableMetricsConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
