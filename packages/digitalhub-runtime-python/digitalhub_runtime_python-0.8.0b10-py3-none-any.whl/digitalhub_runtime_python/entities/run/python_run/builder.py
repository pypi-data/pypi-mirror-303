from __future__ import annotations

from digitalhub_runtime_python.entities._base.runtime_entity.builder import RuntimeEntityBuilderPython
from digitalhub_runtime_python.entities.run.python_run.entity import RunPythonRun
from digitalhub_runtime_python.entities.run.python_run.spec import RunSpecPythonRun, RunValidatorPythonRun
from digitalhub_runtime_python.entities.run.python_run.status import RunStatusPythonRun

from digitalhub.entities.run._base.builder import RunBuilder


class RunPythonRunBuilder(RunBuilder, RuntimeEntityBuilderPython):
    """
    RunPythonRunBuilder runer.
    """

    ENTITY_CLASS = RunPythonRun
    ENTITY_SPEC_CLASS = RunSpecPythonRun
    ENTITY_SPEC_VALIDATOR = RunValidatorPythonRun
    ENTITY_STATUS_CLASS = RunStatusPythonRun
    ENTITY_KIND = "python+run"
