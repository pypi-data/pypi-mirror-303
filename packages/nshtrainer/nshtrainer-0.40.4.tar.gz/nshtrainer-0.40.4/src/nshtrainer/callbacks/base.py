from abc import ABC, abstractmethod
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, TypeAlias

import nshconfig as C
from lightning.pytorch import Callback
from typing_extensions import TypedDict, Unpack

if TYPE_CHECKING:
    from ..model.config import BaseConfig


class CallbackMetadataConfig(TypedDict, total=False):
    ignore_if_exists: bool
    """If `True`, the callback will not be added if another callback with the same class already exists.
    Default is `False`."""

    priority: int
    """Priority of the callback. Callbacks with higher priority will be loaded first.
    Default is `0`."""


@dataclass(frozen=True)
class CallbackWithMetadata:
    callback: Callback
    metadata: CallbackMetadataConfig


ConstructedCallback: TypeAlias = Callback | CallbackWithMetadata


class CallbackConfigBase(C.Config, ABC):
    metadata: ClassVar[CallbackMetadataConfig] = CallbackMetadataConfig()
    """Metadata for the callback."""

    @classmethod
    def with_metadata(
        cls, callback: Callback, **kwargs: Unpack[CallbackMetadataConfig]
    ):
        metadata: CallbackMetadataConfig = {}
        metadata.update(cls.metadata)
        metadata.update(kwargs)

        return CallbackWithMetadata(callback=callback, metadata=metadata)

    @abstractmethod
    def create_callbacks(
        self, root_config: "BaseConfig"
    ) -> Iterable[Callback | CallbackWithMetadata]: ...


# region Config resolution helpers
def _create_callbacks_with_metadata(
    config: CallbackConfigBase, root_config: "BaseConfig"
) -> Iterable[CallbackWithMetadata]:
    for callback in config.create_callbacks(root_config):
        if isinstance(callback, CallbackWithMetadata):
            yield callback
            continue

        callback = config.with_metadata(callback)
        yield callback


def _filter_ignore_if_exists(callbacks: list[CallbackWithMetadata]):
    # First, let's do a pass over all callbacks to hold the count of each callback class
    callback_classes = Counter(callback.callback.__class__ for callback in callbacks)

    # Remove non-duplicates
    callbacks_filtered: list[CallbackWithMetadata] = []
    for callback in callbacks:
        # If `ignore_if_exists` is `True` and there is already a callback of the same class, skip this callback
        if (
            callback.metadata.get("ignore_if_exists", False)
            and callback_classes[callback.callback.__class__] > 1
        ):
            continue

        callbacks_filtered.append(callback)

    return callbacks_filtered


def _process_and_filter_callbacks(
    callbacks: Iterable[CallbackWithMetadata],
) -> list[Callback]:
    callbacks = list(callbacks)

    # Sort by priority (higher priority first)
    callbacks.sort(
        key=lambda callback: callback.metadata.get("priority", 0),
        reverse=True,
    )

    # Process `ignore_if_exists`
    callbacks = _filter_ignore_if_exists(callbacks)

    return [callback.callback for callback in callbacks]


def resolve_all_callbacks(root_config: "BaseConfig"):
    callback_configs = [
        config
        for config in root_config._nshtrainer_all_callback_configs()
        if config is not None
    ]
    callbacks = _process_and_filter_callbacks(
        callback
        for callback_config in callback_configs
        for callback in _create_callbacks_with_metadata(callback_config, root_config)
    )
    return callbacks


# endregion
