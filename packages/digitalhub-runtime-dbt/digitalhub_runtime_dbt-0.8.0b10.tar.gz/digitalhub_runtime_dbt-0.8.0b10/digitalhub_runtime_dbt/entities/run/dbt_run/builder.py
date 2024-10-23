from __future__ import annotations

from digitalhub_runtime_dbt.entities._base.runtime_entity.builder import RuntimeEntityBuilderDbt
from digitalhub_runtime_dbt.entities.run.dbt_run.entity import RunDbtRun
from digitalhub_runtime_dbt.entities.run.dbt_run.spec import RunSpecDbtRun, RunValidatorDbtRun
from digitalhub_runtime_dbt.entities.run.dbt_run.status import RunStatusDbtRun

from digitalhub.entities.run._base.builder import RunBuilder


class RunDbtRunBuilder(RunBuilder, RuntimeEntityBuilderDbt):
    """
    RunDbtRunBuilder runer.
    """

    ENTITY_CLASS = RunDbtRun
    ENTITY_SPEC_CLASS = RunSpecDbtRun
    ENTITY_SPEC_VALIDATOR = RunValidatorDbtRun
    ENTITY_STATUS_CLASS = RunStatusDbtRun
    ENTITY_KIND = "dbt+run"
