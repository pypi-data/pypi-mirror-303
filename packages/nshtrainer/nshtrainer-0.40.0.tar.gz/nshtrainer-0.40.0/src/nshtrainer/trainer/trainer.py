import logging
import os
from collections.abc import Sequence
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

import torch
from lightning.fabric.plugins.environments.lsf import LSFEnvironment
from lightning.fabric.plugins.environments.slurm import SLURMEnvironment
from lightning.fabric.plugins.precision.precision import _PRECISION_INPUT
from lightning.pytorch import LightningModule
from lightning.pytorch import Trainer as LightningTrainer
from lightning.pytorch.callbacks import Callback
from lightning.pytorch.profilers import Profiler
from lightning.pytorch.trainer.states import TrainerFn
from lightning.pytorch.utilities.types import _EVALUATE_OUTPUT, _PREDICT_OUTPUT
from typing_extensions import Unpack, assert_never, override

from .._checkpoint.metadata import _write_checkpoint_metadata
from ..callbacks.base import resolve_all_callbacks
from ..util.bf16 import is_bf16_supported_no_emulation
from ._config import (
    AcceleratorConfigProtocol,
    LightningTrainerKwargs,
    StrategyConfigProtocol,
)
from ._runtime_callback import RuntimeTrackerCallback, Stage
from .checkpoint_connector import _CheckpointConnector
from .signal_connector import _SignalConnector

if TYPE_CHECKING:
    from ..model.config import BaseConfig

log = logging.getLogger(__name__)


class Trainer(LightningTrainer):
    @classmethod
    def _pre_init(cls, config: "BaseConfig"):
        if (precision := config.trainer.set_float32_matmul_precision) is not None:
            torch.set_float32_matmul_precision(precision)

    @classmethod
    def _update_kwargs(
        cls,
        config: "BaseConfig",
        kwargs_ctor: LightningTrainerKwargs,
    ):
        kwargs: LightningTrainerKwargs = {
            "deterministic": config.trainer.reproducibility.deterministic,
            "fast_dev_run": config.trainer.fast_dev_run,
            "max_epochs": config.trainer.max_epochs,
            "min_epochs": config.trainer.min_epochs,
            "max_steps": config.trainer.max_steps,
            "min_steps": config.trainer.min_steps,
            "max_time": config.trainer.max_time,
            "limit_train_batches": config.trainer.limit_train_batches,
            "limit_val_batches": config.trainer.limit_val_batches,
            "limit_test_batches": config.trainer.limit_test_batches,
            "limit_predict_batches": config.trainer.limit_predict_batches,
            "overfit_batches": config.trainer.overfit_batches,
            "val_check_interval": config.trainer.val_check_interval,
            "num_sanity_val_steps": config.trainer.num_sanity_val_steps,
            "log_every_n_steps": config.trainer.log_every_n_steps,
            "inference_mode": config.trainer.inference_mode,
            "callbacks": [],
            "plugins": [],
            "logger": [],
            # Moved to `lightning_kwargs`:
            # "enable_checkpointing": config.trainer.enable_checkpointing,
            # "accelerator": config.trainer.accelerator,
            # "strategy": config.trainer.strategy,
            # "num_nodes": config.trainer.num_nodes,
            # "precision": config.trainer.precision,
            # "logger": config.trainer.logging.enabled,
            # "log_every_n_steps": config.trainer.log_every_n_steps,
            # "enable_progress_bar": config.trainer.enable_progress_bar,
            # "enable_model_summary": config.trainer.enable_model_summary,
            # "accumulate_grad_batches": config.trainer.accumulate_grad_batches,
            # "benchmark": config.trainer.benchmark,
            # "use_distributed_sampler": config.trainer.use_distributed_sampler,
            # "detect_anomaly": config.trainer.detect_anomaly,
            # "barebones": config.trainer.barebones,
            # "plugins": config.trainer.plugins,
            # "sync_batchnorm": config.trainer.sync_batchnorm,
            # "reload_dataloaders_every_n_epochs": config.trainer.reload_dataloaders_every_n_epochs,
        }

        def _update_key(key: str, new_value: Any):
            # First, check to see if the key is already in the kwargs.
            if key not in kwargs:
                kwargs[key] = new_value
                return

            # If the key is already in the kwargs, then we check the type:
            # - If the type is a sequence, then we extend the sequence.
            # - Otherwise, we just update the value but warn the user.

            match existing_value := kwargs[key]:
                case Sequence() as existing_value:
                    # Make sure value is a sequence too
                    if not isinstance(new_value, Sequence):
                        new_value = [new_value]
                    kwargs[key] = [*existing_value, *new_value]
                case _:
                    log.warning(
                        f"Trainer.__init__: Overwriting existing value {existing_value=} with {new_value=} for key {key=}."
                    )
                    kwargs[key] = new_value

        def _update_kwargs(**update: Unpack[LightningTrainerKwargs]):
            for key, value in update.items():
                _update_key(key, value)

        # Set `default_root_dir` if `auto_set_default_root_dir` is enabled.
        if config.trainer.auto_set_default_root_dir:
            if kwargs.get("default_root_dir"):
                raise ValueError(
                    "You have set `config.trainer.default_root_dir`. "
                    "But we are trying to set it automatically. "
                    "Please use `config.directory.base` rather than `config.trainer.default_root_dir`. "
                    "If you want to set it manually, please set `config.trainer.auto_set_default_root_dir=False`."
                )

            _update_kwargs(
                default_root_dir=config.directory.resolve_run_root_directory(config.id)
            )

        if (devices_input := config.trainer.devices) is not None:
            match devices_input:
                case "all":
                    devices = -1
                case "auto":
                    devices = "auto"
                case Sequence():
                    devices = list(devices_input)
                case _:
                    raise ValueError(f"Invalid value for devices={devices_input}.")

            _update_kwargs(devices=devices)

        if (
            use_distributed_sampler := config.trainer.use_distributed_sampler
        ) is not None:
            _update_kwargs(use_distributed_sampler=use_distributed_sampler)

        if (accelerator := config.trainer.accelerator) is not None:
            if isinstance(accelerator, AcceleratorConfigProtocol):
                accelerator = accelerator.create_accelerator()
            _update_kwargs(accelerator=accelerator)

        if (strategy := config.trainer.strategy) is not None:
            if isinstance(strategy, StrategyConfigProtocol):
                strategy = strategy.create_strategy()
            _update_kwargs(strategy=strategy)

        if (precision := config.trainer.precision) is not None:
            resolved_precision: _PRECISION_INPUT
            match precision:
                case "64-true" | "32-true" | "bf16-mixed":
                    resolved_precision = precision
                case "fp16-mixed":
                    resolved_precision = "16-mixed"
                case "16-mixed-auto":
                    try:
                        resolved_precision = (
                            "bf16-mixed"
                            if is_bf16_supported_no_emulation()
                            else "16-mixed"
                        )
                    except BaseException:
                        resolved_precision = "16-mixed"
                        log.warning(
                            "Failed to detect bfloat16 support. Falling back to 16-mixed."
                        )

                    log.critical(
                        f"Auto-resolving {precision=} to {resolved_precision=}."
                    )
                case _:
                    assert_never(precision)

            _update_kwargs(precision=resolved_precision)

        if (detect_anomaly := config.trainer.detect_anomaly) is not None:
            _update_kwargs(detect_anomaly=detect_anomaly)

        if (
            grad_clip_config := config.trainer.optimizer.gradient_clipping
        ) is not None and grad_clip_config.enabled:
            # kwargs["gradient_clip_algorithm"] = grad_clip_config.algorithm
            # kwargs["gradient_clip_val"] = grad_clip_config.value
            _update_kwargs(
                gradient_clip_algorithm=grad_clip_config.algorithm,
                gradient_clip_val=grad_clip_config.value,
            )

        if profiler_config := config.trainer.profiler:
            if (profiler := profiler_config.create_profiler(config)) is None:
                log.warning(f"Profiler config {profiler_config=} returned None.")
            # Make sure that the profiler is an instance of `Profiler`.
            elif not isinstance(profiler, Profiler):
                raise ValueError(f"{profiler=} is not an instance of `{Profiler}`.")
            # Otherwise, if the profiler is a string (e.g., "simpe", "advanced", "pytorch"),
            #   then we just pass it through.
            else:
                _update_kwargs(profiler=profiler)

        if callbacks := resolve_all_callbacks(config):
            _update_kwargs(callbacks=callbacks)

        if plugin_configs := config.trainer.plugins:
            _update_kwargs(
                plugins=[
                    plugin_config.create_plugin() for plugin_config in plugin_configs
                ]
            )

        if not config.trainer.logging.enabled:
            log.critical(f"Disabling logger because {config.trainer.logging.enabled=}.")
            kwargs["logger"] = False
        else:
            _update_kwargs(logger=list(config.trainer.logging.create_loggers(config)))

        if config.trainer.auto_determine_num_nodes:
            # When num_nodes is auto, we need to detect the number of nodes.
            if SLURMEnvironment.detect():
                if (num_nodes := os.environ.get("SLURM_NNODES")) is not None:
                    num_nodes = int(num_nodes)
                    log.critical(f"SLURM detected with {num_nodes=}.")
                    _update_kwargs(num_nodes=num_nodes)
                else:
                    log.critical(
                        "SLURM detected, but SLURM_NNODES not found. "
                        "We'll continue without setting num_nodes, but this may cause issues."
                    )

            elif LSFEnvironment.detect():
                num_nodes = LSFEnvironment().world_size()
                log.critical(f"LSF detected with {num_nodes=}.")
                _update_kwargs(num_nodes=num_nodes)
            else:
                log.info(
                    "config.trainer.auto_determine_num_nodes ignored because no SLURM or LSF detected."
                )

        # Update the kwargs with the additional trainer kwargs
        _update_kwargs(**cast(Any, config.trainer.additional_lightning_kwargs))
        _update_kwargs(**config.trainer.lightning_kwargs)
        _update_kwargs(**kwargs_ctor)

        return kwargs

    if TYPE_CHECKING:
        callbacks: list[Callback]

    @override
    def __init__(
        self,
        config: "BaseConfig",
        /,
        **kwargs: Unpack[LightningTrainerKwargs],
    ):
        self._pre_init(config)

        kwargs = self._update_kwargs(config, kwargs)
        log.critical(f"LightningTrainer.__init__ with {kwargs=}.")

        super().__init__(**kwargs)

        # Add our own start time callback to measure the start time.
        self.callbacks.append(RuntimeTrackerCallback())

        # Replace the signal connector with our own.
        self._signal_connector = _SignalConnector(self)

        # Replace the checkpoint connector with our own.
        self._checkpoint_connector = _CheckpointConnector(self)

        # Print out the log dir, so that we can easily find it in the logs.
        if log_dir := self.log_dir:
            log_dir = str(Path(log_dir).resolve())
        log.critical(f"LightningTrainer log directory: {self.log_dir}.")

        # Set the checkpoint
        if (ckpt_path := config.trainer.ckpt_path) is not None:
            self.ckpt_path = str(Path(ckpt_path).resolve().absolute())

    def __runtime_tracker(self):
        return next(
            (
                callback
                for callback in self.callbacks
                if isinstance(callback, RuntimeTrackerCallback)
            ),
            None,
        )

    def __current_stage(self) -> Stage:
        match self.state.fn:
            case None:
                raise ValueError(
                    "Trainer state function is not set. "
                    "You must call `fit`, `validate`, `test`, or `predict`, "
                    "or explicitly provide a stage."
                )
            case TrainerFn.FITTING:
                return "train"
            case TrainerFn.VALIDATING:
                return "validate"
            case TrainerFn.TESTING:
                return "test"
            case TrainerFn.PREDICTING:
                return "predict"
            case _:
                assert_never(self.state.fn)

    def start_time(self, stage: Stage | None = None):
        """Return the start time of the run"""
        if (tracker := self.__runtime_tracker()) is None:
            raise ValueError(
                "RuntimeTrackerCallback is not set. Cannot get start time."
            )
        if stage is None:
            stage = self.__current_stage()

        return tracker.start_time(stage)

    def end_time(self, stage: Stage | None = None):
        """Return the end time of the run"""
        if (tracker := self.__runtime_tracker()) is None:
            raise ValueError(
                "RuntimeTrackerCallback is not set. Cannot get start time."
            )
        if stage is None:
            stage = self.__current_stage()

        return tracker.end_time(stage)

    def time_elapsed(self, stage: Stage | None = None):
        """Return the time elapsed for the run"""
        if (tracker := self.__runtime_tracker()) is None:
            raise ValueError(
                "RuntimeTrackerCallback is not set. Cannot get start time."
            )
        if stage is None:
            stage = self.__current_stage()

        return tracker.time_elapsed(stage)

    @property
    def _base_module(self):
        if self.lightning_module is None:
            raise ValueError("LightningModule is not set.")

        from ..model.base import LightningModuleBase

        if not isinstance(self.lightning_module, LightningModuleBase):
            raise ValueError(
                f"LightningModule is not an instance of {LightningModuleBase}."
            )

        return self.lightning_module

    @override
    def _run(
        self, model: LightningModule, ckpt_path: str | Path | None = None
    ) -> _EVALUATE_OUTPUT | _PREDICT_OUTPUT | None:
        """Lightning doesn't support gradient clipping with manual optimization.
        We patch the `Trainer._run` method to throw if gradient clipping is enabled
        and `model.automatic_optimization` is False.
        """

        if not model.automatic_optimization and (
            self.gradient_clip_val is not None
            or self.gradient_clip_algorithm is not None
        ):
            raise ValueError(
                "Automatic gradient clipping is not supported with manual optimization. "
                f"Please set {model.__class__.__name__}.automatic_optimization to True "
                "or disable automatic gradient clipping. "
            )

        return super()._run(model, ckpt_path)

    @override
    def save_checkpoint(
        self,
        filepath: str | Path,
        weights_only: bool = False,
        storage_options: Any | None = None,
    ):
        filepath = Path(filepath)

        # List of files that we should upload to HF
        written_files: list[Path] = [filepath]

        super().save_checkpoint(filepath, weights_only, storage_options)

        # Save the checkpoint metadata
        metadata_path = None
        lm = self._base_module
        root_config = cast("BaseConfig", lm.hparams)
        if root_config.trainer.save_checkpoint_metadata and self.is_global_zero:
            # Generate the metadata and write to disk
            if (
                metadata_path := _write_checkpoint_metadata(self, lm, filepath)
            ) is not None:
                written_files.append(metadata_path)

        # Call the `on_checkpoint_saved` method on all callbacks
        from .. import _callback

        _callback._call_on_checkpoint_saved(self, filepath, metadata_path)
