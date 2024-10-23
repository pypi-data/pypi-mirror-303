from __future__ import annotations

from digitalhub_runtime_container.runtimes.runtime import RuntimeContainer

from digitalhub.runtimes.builder import RuntimeBuilder


class RuntimeContainerBuilder(RuntimeBuilder):
    """RuntaimeContainerBuilder class."""

    RUNTIME_CLASS = RuntimeContainer
