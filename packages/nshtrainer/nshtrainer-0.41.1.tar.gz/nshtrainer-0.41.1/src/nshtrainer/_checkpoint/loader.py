import logging
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Annotated, Literal, TypeAlias, overload

import nshconfig as C
from lightning.pytorch import Trainer as LightningTrainer
from lightning.pytorch.trainer.states import TrainerFn
from typing_extensions import assert_never

from ..metrics._config import MetricConfig
from .metadata import CheckpointMetadata

if TYPE_CHECKING:
    from ..model.config import BaseConfig

log = logging.getLogger(__name__)


class BestCheckpointStrategyConfig(C.Config):
    name: Literal["best"] = "best"

    metric: MetricConfig | None = None
    """The metric to use for selecting the best checkpoint. If `None`, the primary metric will be used."""

    additional_candidates: Iterable[Path] = []
    """Additional checkpoint candidates to consider when selecting the last checkpoint."""


class UserProvidedPathCheckpointStrategyConfig(C.Config):
    name: Literal["user_provided_path"] = "user_provided_path"

    path: Path
    """The path to the checkpoint to load."""

    on_error: Literal["warn", "raise"] = "warn"
    """The behavior when the checkpoint does not belong to the current run.

    - `warn`: Log a warning and skip the checkpoint.
    - `raise`: Raise an error.
    """


class LastCheckpointStrategyConfig(C.Config):
    name: Literal["last"] = "last"

    criterion: Literal["global_step", "runtime"] = "global_step"
    """The criterion to use for selecting the last checkpoint.

    - `global_step`: The checkpoint with the highest global step will be selected.
    - `runtime`: The checkpoint with the highest runtime will be selected.
    """

    additional_candidates: Iterable[Path] = []
    """Additional checkpoint candidates to consider when selecting the last checkpoint."""


CheckpointLoadingStrategyConfig: TypeAlias = Annotated[
    BestCheckpointStrategyConfig
    | LastCheckpointStrategyConfig
    | UserProvidedPathCheckpointStrategyConfig,
    C.Field(discriminator="name"),
]


class CheckpointLoadingConfig(C.Config):
    strategies: Sequence[CheckpointLoadingStrategyConfig]
    """The strategies to use for loading checkpoints.

    The order of the strategies determines the priority of the strategies.
    The first strategy that resolves a checkpoint will be used.
    """

    include_hpc: bool
    """Whether to include checkpoints from HPC pre-emption."""

    @classmethod
    def none(cls, include_hpc: bool = False):
        return cls(strategies=[], include_hpc=include_hpc)

    @classmethod
    def _auto_train(cls, ckpt: Literal["best", "last", "none"] | str | Path | None):
        if ckpt is None:
            ckpt = "last"
        match ckpt:
            case "best":
                return cls(
                    strategies=[BestCheckpointStrategyConfig()],
                    include_hpc=True,
                )
            case "last":
                return cls(
                    strategies=[LastCheckpointStrategyConfig()],
                    include_hpc=True,
                )
            case "none":
                return cls.none()
            case Path() | str():
                ckpt = Path(ckpt)
                return cls(
                    strategies=[
                        LastCheckpointStrategyConfig(additional_candidates=[ckpt]),
                        UserProvidedPathCheckpointStrategyConfig(path=ckpt),
                    ],
                    include_hpc=True,
                )
            case _:
                assert_never(ckpt)

    @classmethod
    def _auto_eval(cls, ckpt: Literal["best", "last", "none"] | str | Path | None):
        if ckpt is None:
            log.warn("No checkpoint specified for evaluation. Defaulting to `last`.")
            ckpt = "last"

        match ckpt:
            case "best":
                return cls(
                    strategies=[BestCheckpointStrategyConfig()],
                    include_hpc=False,
                )
            case "last":
                return cls(
                    strategies=[LastCheckpointStrategyConfig()],
                    include_hpc=False,
                )
            case "none":
                return cls.none(include_hpc=False)
            case Path() | str():
                ckpt = Path(ckpt)
                return cls(
                    strategies=[UserProvidedPathCheckpointStrategyConfig(path=ckpt)],
                    include_hpc=False,
                )
            case _:
                assert_never(ckpt)

    @classmethod
    def auto(
        cls,
        ckpt: Literal["best", "last", "none"] | str | Path | None,
        trainer_mode: TrainerFn,
    ):
        """
        Automatically create a CheckpointLoadingConfig based on the provided checkpoint option and trainer mode.

        This method provides a convenient way to generate a checkpoint loading configuration
        tailored to different training and evaluation scenarios.

        Parameters:
        -----------
        ckpt : Literal["best", "last", "none"] | str | Path | None
            Specifies the checkpoint loading preference:
            - "best": Use the best checkpoint based on the primary metric.
            - "last": Use the most recent checkpoint.
            - str or Path: Path to a specific checkpoint file.
            - None: Defaults to "last" for training, raises an error for evaluation.

        trainer_mode : TrainerFn
            The mode in which the trainer is operating. This affects how the configuration is created.
            - TrainerFn.FITTING: Used for training scenarios.
            - TrainerFn.VALIDATING, TrainerFn.TESTING, TrainerFn.PREDICTING: Used for evaluation scenarios.

        Returns:
        --------
        CheckpointLoadingConfig
            A configuration object for checkpoint loading based on the given parameters.

        Behavior:
        ---------
        1. For training (TrainerFn.FITTING):
        - Includes HPC pre-emption checkpoints.
        - If ckpt is None, defaults to "last".
        - For "best" or "last", creates a single-strategy configuration that loads the best or last checkpoint.
        - For a specific path, creates a two-strategy configuration:
            a) Tries to load the checkpoint as the last checkpoint.
            b) Falls back to loading it as a user-provided path.

        2. For evaluation (VALIDATING, TESTING, PREDICTING):
        - Does not include HPC pre-emption checkpoints.
        - Requires ckpt to be specified (raises ValueError if None).
        - Creates a single-strategy configuration based on the ckpt value.

        Raises:
        -------
        ValueError
            If ckpt is None during evaluation modes.

        Examples:
        ---------
        # Training mode, use last checkpoint
        config = CheckpointLoadingConfig.auto("last", TrainerFn.FITTING)

        # Evaluation mode, use best checkpoint
        config = CheckpointLoadingConfig.auto("best", TrainerFn.TESTING)

        # Training mode, use specific checkpoint
        config = CheckpointLoadingConfig.auto("/path/to/checkpoint.ckpt", TrainerFn.FITTING)

        Notes:
        ------
        - The method internally calls _auto_train or _auto_eval based on the trainer_mode.
        - The resulting configuration always includes strategies as a sequence, even if there's only one strategy.
        """
        # Implementation remains the same...
        match trainer_mode:
            case TrainerFn.FITTING:
                return cls._auto_train(ckpt)
            case TrainerFn.VALIDATING | TrainerFn.TESTING | TrainerFn.PREDICTING:
                return cls._auto_eval(ckpt)
            case _:
                assert_never(trainer_mode)


@dataclass
class _CkptCandidate:
    meta: CheckpointMetadata
    meta_path: Path

    @property
    def ckpt_path(self):
        return self.meta_path.with_name(self.meta.checkpoint_filename)


@overload
def _load_ckpt_meta(
    path: Path,
    root_config: "BaseConfig",
    on_error: Literal["warn"] = "warn",
) -> _CkptCandidate | None: ...
@overload
def _load_ckpt_meta(
    path: Path,
    root_config: "BaseConfig",
    on_error: Literal["raise"],
) -> _CkptCandidate: ...
def _load_ckpt_meta(
    path: Path,
    root_config: "BaseConfig",
    on_error: Literal["warn", "raise"] = "warn",
):
    meta = CheckpointMetadata.from_file(path)
    if root_config.id != meta.run_id:
        error_msg = f"Skipping checkpoint {path} because it belongs to a different run"
        match on_error:
            case "warn":
                log.warning(error_msg)
            case "raise":
                raise ValueError(error_msg)
            case _:
                assert_never(on_error)
        return None
    return _CkptCandidate(meta, path)


def _checkpoint_candidates(
    root_config: "BaseConfig",
    trainer: LightningTrainer,
    *,
    include_hpc: bool = True,
):
    # Load the checkpoint directory, and throw if it doesn't exist.
    # This indicates a non-standard setup, and we don't want to guess
    # where the checkpoints are.
    ckpt_dir = root_config.directory.resolve_subdirectory(root_config.id, "checkpoint")
    if not ckpt_dir.is_dir():
        raise FileNotFoundError(
            f"Checkpoint directory {ckpt_dir} not found. "
            "Please ensure that the checkpoint directory exists."
        )

    # Load all checkpoints in the directory.
    # We can do this by looking for metadata files.
    for path in ckpt_dir.glob(f"*{CheckpointMetadata.PATH_SUFFIX}"):
        if (meta := _load_ckpt_meta(path, root_config)) is not None:
            yield meta

    # If we have a pre-empted checkpoint, load it
    if include_hpc and (hpc_path := trainer._checkpoint_connector._hpc_resume_path):
        hpc_meta_path = Path(hpc_path).with_suffix(CheckpointMetadata.PATH_SUFFIX)
        if (meta := _load_ckpt_meta(hpc_meta_path, root_config)) is not None:
            yield meta


def _additional_candidates(
    additional_candidates: Iterable[Path], root_config: "BaseConfig"
):
    for path in additional_candidates:
        if (
            meta := _load_ckpt_meta(
                path.with_suffix(CheckpointMetadata.PATH_SUFFIX), root_config
            )
        ) is None:
            continue
        yield meta


def _resolve_checkpoint(
    config: CheckpointLoadingConfig,
    root_config: "BaseConfig",
    trainer: LightningTrainer,
):
    # We lazily load the checkpoint candidates to avoid loading them
    # if they are not needed.
    _ckpt_candidates: list[_CkptCandidate] | None = None

    def ckpt_candidates():
        nonlocal _ckpt_candidates, root_config, trainer

        if _ckpt_candidates is None:
            _ckpt_candidates = list(
                _checkpoint_candidates(
                    root_config, trainer, include_hpc=config.include_hpc
                )
            )
        return _ckpt_candidates

    # Iterate over the strategies and try to resolve the checkpoint.
    for strategy in config.strategies:
        match strategy:
            case UserProvidedPathCheckpointStrategyConfig():
                meta = _load_ckpt_meta(
                    strategy.path.with_suffix(CheckpointMetadata.PATH_SUFFIX),
                    root_config,
                    on_error=strategy.on_error,
                )
                if meta is None:
                    continue
                return meta.ckpt_path
            case BestCheckpointStrategyConfig():
                candidates = [
                    *ckpt_candidates(),
                    *_additional_candidates(
                        strategy.additional_candidates, root_config
                    ),
                ]
                if not candidates:
                    log.warning(
                        "No checkpoint candidates found for `best` checkpoint strategy."
                    )
                    continue

                if (metric := strategy.metric or root_config.primary_metric) is None:
                    log.warning(
                        "No metric specified for `best` checkpoint strategy, "
                        "and no primary metric is set in the configuration. "
                        "Skipping strategy."
                    )
                    continue

                # Find the best checkpoint based on the metric.
                def metric_value(ckpt: _CkptCandidate):
                    assert metric is not None
                    if (
                        value := ckpt.meta.metrics.get(metric.validation_monitor)
                    ) is None:
                        raise ValueError(
                            f"Metric {metric.validation_monitor} not found in checkpoint metadata. "
                            f"Available metrics: {ckpt.meta.metrics.keys()}"
                        )
                    return value

                best_candidate = metric.best(candidates, key=metric_value)
                return best_candidate.ckpt_path
            case LastCheckpointStrategyConfig():
                candidates = [
                    *ckpt_candidates(),
                    *_additional_candidates(
                        strategy.additional_candidates, root_config
                    ),
                ]
                if not candidates:
                    log.warning(
                        "No checkpoint candidates found for `last` checkpoint strategy."
                    )
                    continue

                # Find the last checkpoint based on the criterion.
                def criterion_value(ckpt: _CkptCandidate):
                    match strategy.criterion:
                        case "global_step":
                            return ckpt.meta.global_step
                        case "runtime":
                            return ckpt.meta.training_time.total_seconds()
                        case _:
                            assert_never(strategy.criterion)

                last_candidate = max(candidates, key=criterion_value)
                return last_candidate.ckpt_path
            case _:
                assert_never(strategy)
