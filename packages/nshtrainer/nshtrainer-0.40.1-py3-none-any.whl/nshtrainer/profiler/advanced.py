import logging
from typing import Literal

from typing_extensions import override

from ._base import BaseProfilerConfig

log = logging.getLogger(__name__)


class AdvancedProfilerConfig(BaseProfilerConfig):
    name: Literal["advanced"] = "advanced"

    line_count_restriction: float = 1.0
    """
    This can be used to limit the number of functions
        reported for each action. either an integer (to select a count of lines),
        or a decimal fraction between 0.0 and 1.0 inclusive (to select a percentage of lines)
    """

    @override
    def create_profiler(self, root_config):
        from lightning.pytorch.profilers.advanced import AdvancedProfiler

        if (dirpath := self.dirpath) is None:
            dirpath = root_config.directory.resolve_subdirectory(
                root_config.id, "profile"
            )

        if (filename := self.filename) is None:
            filename = f"{root_config.id}_profile.txt"

        return AdvancedProfiler(
            line_count_restriction=self.line_count_restriction,
            dirpath=dirpath,
            filename=filename,
        )
