__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.optimizer import AdamWConfig as AdamWConfig
    from nshtrainer.optimizer import OptimizerConfig as OptimizerConfig
    from nshtrainer.optimizer import OptimizerConfigBase as OptimizerConfigBase
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "OptimizerConfigBase":
            return importlib.import_module("nshtrainer.optimizer").OptimizerConfigBase
        if name == "AdamWConfig":
            return importlib.import_module("nshtrainer.optimizer").AdamWConfig
        if name == "OptimizerConfig":
            return importlib.import_module("nshtrainer.optimizer").OptimizerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
