from __future__ import annotations

from digitalhub_runtime_kfp.runtimes.runtime import RuntimeKfp

from digitalhub.runtimes.builder import RuntimeBuilder


class RuntimeKfpBuilder(RuntimeBuilder):
    """RuntaimeKfpBuilder class."""

    RUNTIME_CLASS = RuntimeKfp
