from __future__ import annotations

from digitalhub_runtime_modelserve.runtimes.runtime import RuntimeModelserve

from digitalhub.runtimes.builder import RuntimeBuilder


class RuntimeModelserveBuilder(RuntimeBuilder):
    """RuntaimeModelserveBuilder class."""

    RUNTIME_CLASS = RuntimeModelserve
