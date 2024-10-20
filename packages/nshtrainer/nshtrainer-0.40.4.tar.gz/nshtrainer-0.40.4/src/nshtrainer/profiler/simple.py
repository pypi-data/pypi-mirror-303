import logging
from typing import Literal

from typing_extensions import override

from ._base import BaseProfilerConfig

log = logging.getLogger(__name__)


class SimpleProfilerConfig(BaseProfilerConfig):
    name: Literal["simple"] = "simple"

    extended: bool = True
    """
    If ``True``, adds extra columns representing number of calls and percentage of
        total time spent onrespective action.
    """

    @override
    def create_profiler(self, root_config):
        from lightning.pytorch.profilers.simple import SimpleProfiler

        if (dirpath := self.dirpath) is None:
            dirpath = root_config.directory.resolve_subdirectory(
                root_config.id, "profile"
            )

        if (filename := self.filename) is None:
            filename = f"{root_config.id}_profile.txt"

        return SimpleProfiler(
            extended=self.extended,
            dirpath=dirpath,
            filename=filename,
        )
