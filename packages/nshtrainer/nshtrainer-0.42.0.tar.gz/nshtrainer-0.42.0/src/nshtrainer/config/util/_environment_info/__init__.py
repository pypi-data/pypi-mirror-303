__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer.util._environment_info import (
        EnvironmentClassInformationConfig as EnvironmentClassInformationConfig,
    )
    from nshtrainer.util._environment_info import EnvironmentConfig as EnvironmentConfig
    from nshtrainer.util._environment_info import (
        EnvironmentCUDAConfig as EnvironmentCUDAConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentGPUConfig as EnvironmentGPUConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentHardwareConfig as EnvironmentHardwareConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentLinuxEnvironmentConfig as EnvironmentLinuxEnvironmentConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentLSFInformationConfig as EnvironmentLSFInformationConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentPackageConfig as EnvironmentPackageConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentSLURMInformationConfig as EnvironmentSLURMInformationConfig,
    )
    from nshtrainer.util._environment_info import (
        EnvironmentSnapshotConfig as EnvironmentSnapshotConfig,
    )
    from nshtrainer.util._environment_info import (
        GitRepositoryConfig as GitRepositoryConfig,
    )
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "EnvironmentPackageConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentPackageConfig
        if name == "EnvironmentSnapshotConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentSnapshotConfig
        if name == "EnvironmentLSFInformationConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentLSFInformationConfig
        if name == "EnvironmentLinuxEnvironmentConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentLinuxEnvironmentConfig
        if name == "EnvironmentSLURMInformationConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentSLURMInformationConfig
        if name == "EnvironmentConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentConfig
        if name == "EnvironmentClassInformationConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentClassInformationConfig
        if name == "GitRepositoryConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).GitRepositoryConfig
        if name == "EnvironmentCUDAConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentCUDAConfig
        if name == "EnvironmentGPUConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentGPUConfig
        if name == "EnvironmentHardwareConfig":
            return importlib.import_module(
                "nshtrainer.util._environment_info"
            ).EnvironmentHardwareConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
