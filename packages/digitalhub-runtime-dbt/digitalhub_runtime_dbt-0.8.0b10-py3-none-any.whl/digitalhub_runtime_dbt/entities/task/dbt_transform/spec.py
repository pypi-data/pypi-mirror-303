from __future__ import annotations

from digitalhub.entities.task._base.spec import TaskSpecK8s, TaskValidatorK8s


class TaskSpecDbtTransform(TaskSpecK8s):
    """TaskSpecDbtTransform specifications."""


class TaskValidatorDbtTransform(TaskValidatorK8s):
    """
    TaskValidatorDbtTransform validator.
    """
