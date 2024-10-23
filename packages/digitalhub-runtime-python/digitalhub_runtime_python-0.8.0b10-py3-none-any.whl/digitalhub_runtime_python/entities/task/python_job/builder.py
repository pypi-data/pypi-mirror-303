from __future__ import annotations

from digitalhub_runtime_python.entities._base.runtime_entity.builder import RuntimeEntityBuilderPython
from digitalhub_runtime_python.entities.task.python_job.entity import TaskPythonJob
from digitalhub_runtime_python.entities.task.python_job.spec import TaskSpecPythonJob, TaskValidatorPythonJob
from digitalhub_runtime_python.entities.task.python_job.status import TaskStatusPythonJob

from digitalhub.entities.task._base.builder import TaskBuilder


class TaskPythonJobBuilder(TaskBuilder, RuntimeEntityBuilderPython):
    """
    TaskPythonJobBuilder jober.
    """

    ENTITY_CLASS = TaskPythonJob
    ENTITY_SPEC_CLASS = TaskSpecPythonJob
    ENTITY_SPEC_VALIDATOR = TaskValidatorPythonJob
    ENTITY_STATUS_CLASS = TaskStatusPythonJob
    ENTITY_KIND = "python+job"
