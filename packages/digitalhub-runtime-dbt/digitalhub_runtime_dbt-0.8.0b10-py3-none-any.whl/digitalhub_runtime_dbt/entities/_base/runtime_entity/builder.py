from __future__ import annotations

from digitalhub.entities._base.runtime_entity.builder import RuntimeEntityBuilder


class RuntimeEntityBuilderDbt(RuntimeEntityBuilder):
    EXECUTABLE_KIND = "dbt"
    TASKS_KINDS = [
        {
            "kind": "dbt+transform",
            "action": "transform",
        },
    ]
    RUN_KIND = "dbt+run"
