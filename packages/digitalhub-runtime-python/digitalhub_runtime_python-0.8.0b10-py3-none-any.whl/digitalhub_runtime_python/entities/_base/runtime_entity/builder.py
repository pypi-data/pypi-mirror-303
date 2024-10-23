from __future__ import annotations

from digitalhub.entities._base.runtime_entity.builder import RuntimeEntityBuilder


class RuntimeEntityBuilderPython(RuntimeEntityBuilder):
    EXECUTABLE_KIND = "python"
    TASKS_KINDS = [
        {
            "kind": "python+job",
            "action": "job",
        },
        {
            "kind": "python+build",
            "action": "build",
        },
        {
            "kind": "python+serve",
            "action": "serve",
        },
    ]
    RUN_KIND = "python+run"
