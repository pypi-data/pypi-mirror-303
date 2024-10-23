from __future__ import annotations

from digitalhub_runtime_dbt.entities._base.runtime_entity.builder import RuntimeEntityBuilderDbt
from digitalhub_runtime_dbt.entities.function.dbt.entity import FunctionDbt
from digitalhub_runtime_dbt.entities.function.dbt.spec import FunctionSpecDbt, FunctionValidatorDbt
from digitalhub_runtime_dbt.entities.function.dbt.status import FunctionStatusDbt

from digitalhub.entities.function._base.builder import FunctionBuilder


class FunctionDbtBuilder(FunctionBuilder, RuntimeEntityBuilderDbt):
    """
    FunctionDbt builder.
    """

    ENTITY_CLASS = FunctionDbt
    ENTITY_SPEC_CLASS = FunctionSpecDbt
    ENTITY_SPEC_VALIDATOR = FunctionValidatorDbt
    ENTITY_STATUS_CLASS = FunctionStatusDbt
    ENTITY_KIND = "dbt"
