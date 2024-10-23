from __future__ import annotations

from digitalhub_runtime_python.entities.function.python.builder import FunctionPythonBuilder
from digitalhub_runtime_python.entities.run.python_run.builder import RunPythonRunBuilder
from digitalhub_runtime_python.entities.task.python_build.builder import TaskPythonBuildBuilder
from digitalhub_runtime_python.entities.task.python_job.builder import TaskPythonJobBuilder
from digitalhub_runtime_python.entities.task.python_serve.builder import TaskPythonServeBuilder
from digitalhub_runtime_python.utils.utils import handler

entity_builders = (
    (FunctionPythonBuilder.ENTITY_KIND, FunctionPythonBuilder),
    (TaskPythonBuildBuilder.ENTITY_KIND, TaskPythonBuildBuilder),
    (TaskPythonJobBuilder.ENTITY_KIND, TaskPythonJobBuilder),
    (TaskPythonServeBuilder.ENTITY_KIND, TaskPythonServeBuilder),
    (RunPythonRunBuilder.ENTITY_KIND, RunPythonRunBuilder),
)

try:
    from digitalhub_runtime_python.runtimes.builder import RuntimePythonBuilder

    runtime_builders = ((kind, RuntimePythonBuilder) for kind in FunctionPythonBuilder().get_all_kinds())
except ImportError:
    runtime_builders = tuple()
