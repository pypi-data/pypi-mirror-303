from __future__ import annotations

from digitalhub_runtime_dbt.entities.function.dbt.builder import FunctionDbtBuilder
from digitalhub_runtime_dbt.entities.run.dbt_run.builder import RunDbtRunBuilder
from digitalhub_runtime_dbt.entities.task.dbt_transform.builder import TaskDbtTransformBuilder

entity_builders = (
    (FunctionDbtBuilder.ENTITY_KIND, FunctionDbtBuilder),
    (RunDbtRunBuilder.ENTITY_KIND, RunDbtRunBuilder),
    (TaskDbtTransformBuilder.ENTITY_KIND, TaskDbtTransformBuilder),
)

try:
    from digitalhub_runtime_dbt.runtimes.builder import RuntimeDbtBuilder

    runtime_builders = ((kind, RuntimeDbtBuilder) for kind in FunctionDbtBuilder().get_all_kinds())
except ImportError:
    runtime_builders = tuple()
