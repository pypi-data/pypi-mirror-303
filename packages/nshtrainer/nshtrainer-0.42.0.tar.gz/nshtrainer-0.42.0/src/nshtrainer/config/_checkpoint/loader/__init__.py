__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer._checkpoint.loader import (
        BestCheckpointStrategyConfig as BestCheckpointStrategyConfig,
    )
    from nshtrainer._checkpoint.loader import (
        CheckpointLoadingConfig as CheckpointLoadingConfig,
    )
    from nshtrainer._checkpoint.loader import (
        CheckpointLoadingStrategyConfig as CheckpointLoadingStrategyConfig,
    )
    from nshtrainer._checkpoint.loader import CheckpointMetadata as CheckpointMetadata
    from nshtrainer._checkpoint.loader import (
        LastCheckpointStrategyConfig as LastCheckpointStrategyConfig,
    )
    from nshtrainer._checkpoint.loader import MetricConfig as MetricConfig
    from nshtrainer._checkpoint.loader import (
        UserProvidedPathCheckpointStrategyConfig as UserProvidedPathCheckpointStrategyConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CheckpointLoadingConfig":
            return importlib.import_module(
                "nshtrainer._checkpoint.loader"
            ).CheckpointLoadingConfig
        if name == "CheckpointMetadata":
            return importlib.import_module(
                "nshtrainer._checkpoint.loader"
            ).CheckpointMetadata
        if name == "MetricConfig":
            return importlib.import_module("nshtrainer._checkpoint.loader").MetricConfig
        if name == "BestCheckpointStrategyConfig":
            return importlib.import_module(
                "nshtrainer._checkpoint.loader"
            ).BestCheckpointStrategyConfig
        if name == "LastCheckpointStrategyConfig":
            return importlib.import_module(
                "nshtrainer._checkpoint.loader"
            ).LastCheckpointStrategyConfig
        if name == "UserProvidedPathCheckpointStrategyConfig":
            return importlib.import_module(
                "nshtrainer._checkpoint.loader"
            ).UserProvidedPathCheckpointStrategyConfig
        if name == "CheckpointLoadingStrategyConfig":
            return importlib.import_module(
                "nshtrainer._checkpoint.loader"
            ).CheckpointLoadingStrategyConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
