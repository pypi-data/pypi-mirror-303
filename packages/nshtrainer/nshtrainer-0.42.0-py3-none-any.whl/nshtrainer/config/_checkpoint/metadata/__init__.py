__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer._checkpoint.metadata import CheckpointMetadata as CheckpointMetadata
    from nshtrainer._checkpoint.metadata import EnvironmentConfig as EnvironmentConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "EnvironmentConfig":
            return importlib.import_module(
                "nshtrainer._checkpoint.metadata"
            ).EnvironmentConfig
        if name == "CheckpointMetadata":
            return importlib.import_module(
                "nshtrainer._checkpoint.metadata"
            ).CheckpointMetadata
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
