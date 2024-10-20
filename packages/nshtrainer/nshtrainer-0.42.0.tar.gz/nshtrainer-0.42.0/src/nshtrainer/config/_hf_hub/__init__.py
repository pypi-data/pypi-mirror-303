__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from nshtrainer._hf_hub import CallbackConfigBase as CallbackConfigBase
    from nshtrainer._hf_hub import (
        HuggingFaceHubAutoCreateConfig as HuggingFaceHubAutoCreateConfig,
    )
    from nshtrainer._hf_hub import HuggingFaceHubConfig as HuggingFaceHubConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "CallbackConfigBase":
            return importlib.import_module("nshtrainer._hf_hub").CallbackConfigBase
        if name == "HuggingFaceHubConfig":
            return importlib.import_module("nshtrainer._hf_hub").HuggingFaceHubConfig
        if name == "HuggingFaceHubAutoCreateConfig":
            return importlib.import_module(
                "nshtrainer._hf_hub"
            ).HuggingFaceHubAutoCreateConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
