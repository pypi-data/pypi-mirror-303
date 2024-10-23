from __future__ import annotations

from digitalhub.entities.task._base.spec import TaskSpecK8s, TaskValidatorK8s


class TaskSpecPythonBuild(TaskSpecK8s):
    """TaskSpecPythonBuild specifications."""

    def __init__(
        self,
        function: str,
        node_selector: dict | None = None,
        volumes: list | None = None,
        resources: dict | None = None,
        affinity: dict | None = None,
        tolerations: list | None = None,
        envs: list | None = None,
        secrets: list | None = None,
        profile: str | None = None,
        instructions: list | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            function,
            node_selector,
            volumes,
            resources,
            affinity,
            tolerations,
            envs,
            secrets,
            profile,
            **kwargs,
        )
        self.instructions = instructions


class TaskValidatorPythonBuild(TaskValidatorK8s):
    """
    TaskValidatorPythonBuild validator.
    """

    instructions: list[str] = None
    """Build instructions."""
