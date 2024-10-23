from __future__ import annotations

from digitalhub_runtime_dbt.runtimes.runtime import RuntimeDbt

from digitalhub.runtimes.builder import RuntimeBuilder


class RuntimeDbtBuilder(RuntimeBuilder):
    """RuntaimeDbtBuilder class."""

    RUNTIME_CLASS = RuntimeDbt
