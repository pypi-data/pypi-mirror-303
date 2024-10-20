__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer._directory import DirectoryConfig as DirectoryConfig
    from nshtrainer._directory import DirectorySetupConfig as DirectorySetupConfig
    from nshtrainer._directory import LoggerConfig as LoggerConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "DirectoryConfig":
            return importlib.import_module("nshtrainer._directory").DirectoryConfig
        if name == "DirectorySetupConfig":
            return importlib.import_module("nshtrainer._directory").DirectorySetupConfig
        if name == "LoggerConfig":
            return importlib.import_module("nshtrainer._directory").LoggerConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
