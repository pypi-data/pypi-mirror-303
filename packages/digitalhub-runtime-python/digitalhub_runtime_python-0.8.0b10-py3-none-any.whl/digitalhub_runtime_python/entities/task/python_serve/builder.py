from __future__ import annotations

from digitalhub_runtime_python.entities._base.runtime_entity.builder import RuntimeEntityBuilderPython
from digitalhub_runtime_python.entities.task.python_serve.entity import TaskPythonServe
from digitalhub_runtime_python.entities.task.python_serve.spec import TaskSpecPythonServe, TaskValidatorPythonServe
from digitalhub_runtime_python.entities.task.python_serve.status import TaskStatusPythonServe

from digitalhub.entities.task._base.builder import TaskBuilder


class TaskPythonServeBuilder(TaskBuilder, RuntimeEntityBuilderPython):
    """
    TaskPythonServeBuilder serveer.
    """

    ENTITY_CLASS = TaskPythonServe
    ENTITY_SPEC_CLASS = TaskSpecPythonServe
    ENTITY_SPEC_VALIDATOR = TaskValidatorPythonServe
    ENTITY_STATUS_CLASS = TaskStatusPythonServe
    ENTITY_KIND = "python+serve"
