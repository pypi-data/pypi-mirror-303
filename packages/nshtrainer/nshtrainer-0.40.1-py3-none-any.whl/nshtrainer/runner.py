import copy
import logging
from collections.abc import Callable, Iterable, Mapping, Sequence
from pathlib import Path
from typing import Generic

import nshrunner as nr
from nshrunner._submit import screen
from typing_extensions import TypeVar, TypeVarTuple, Unpack, deprecated, override

from .model.config import BaseConfig

TConfig = TypeVar("TConfig", bound=BaseConfig, infer_variance=True)
TArguments = TypeVarTuple("TArguments", default=Unpack[tuple[()]])
TReturn = TypeVar("TReturn", infer_variance=True)


@deprecated("Use nshrunner.Runner instead.")
class Runner(
    nr.Runner[TReturn, TConfig, Unpack[TArguments]],
    Generic[TReturn, TConfig, Unpack[TArguments]],
):
    @override
    def __init__(
        self,
        run_fn: Callable[[TConfig, Unpack[TArguments]], TReturn],
        config: nr.RunnerConfig | None = None,
    ):
        if config is None:
            working_dir = Path.cwd() / "nshrunner"
            working_dir.mkdir(exist_ok=True)

            logging.warning(
                f"`config` is not provided. Using default working directory of {working_dir}."
            )
            config = nr.RunnerConfig(working_dir=working_dir)

        super().__init__(run_fn, config)

    def fast_dev_run(
        self,
        runs: Iterable[tuple[TConfig, Unpack[TArguments]]],
        n_batches: int = 1,
        *,
        env: Mapping[str, str] | None = None,
    ):
        runs_updated: list[tuple[TConfig, Unpack[TArguments]]] = []
        for args in runs:
            config = copy.deepcopy(args[0])
            config.trainer.fast_dev_run = n_batches
            runs_updated.append((config, *args[1:]))
        del runs

        return self.local(runs_updated, env=env)

    def fast_dev_run_generator(
        self,
        runs: Iterable[tuple[TConfig, Unpack[TArguments]]],
        n_batches: int = 1,
        *,
        env: Mapping[str, str] | None = None,
    ):
        runs_updated: list[tuple[TConfig, Unpack[TArguments]]] = []
        for args in runs:
            config = copy.deepcopy(args[0])
            config.trainer.fast_dev_run = n_batches
            runs_updated.append((config, *args[1:]))
        del runs

        return self.local_generator(runs_updated, env=env)

    def fast_dev_run_session(
        self,
        runs: Iterable[tuple[TConfig, Unpack[TArguments]]],
        options: screen.ScreenJobKwargs = {},
        n_batches: int = 1,
        *,
        snapshot: nr.Snapshot,
        setup_commands: Sequence[str] | None = None,
        env: Mapping[str, str] | None = None,
        activate_venv: bool = True,
        print_command: bool = True,
    ):
        runs_updated: list[tuple[TConfig, Unpack[TArguments]]] = []
        for args in runs:
            config = copy.deepcopy(args[0])
            config.trainer.fast_dev_run = n_batches
            runs_updated.append((config, *args[1:]))
        del runs

        return self.session(
            runs_updated,
            options,
            snapshot=snapshot,
            setup_commands=setup_commands,
            env=env,
            activate_venv=activate_venv,
            print_command=print_command,
        )
