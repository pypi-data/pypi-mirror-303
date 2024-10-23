from __future__ import annotations

import typing

from digitalhub.entities.function._base.entity import Function

if typing.TYPE_CHECKING:
    from digitalhub_runtime_dbt.entities.function.dbt.spec import FunctionSpecDbt
    from digitalhub_runtime_dbt.entities.function.dbt.status import FunctionStatusDbt

    from digitalhub.entities._base.entity.metadata import Metadata


class FunctionDbt(Function):
    """
    FunctionDbt class.
    """

    def __init__(
        self,
        project: str,
        name: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: FunctionSpecDbt,
        status: FunctionStatusDbt,
        user: str | None = None,
    ) -> None:
        super().__init__(project, name, uuid, kind, metadata, spec, status, user)

        self.spec: FunctionSpecDbt
        self.status: FunctionStatusDbt
