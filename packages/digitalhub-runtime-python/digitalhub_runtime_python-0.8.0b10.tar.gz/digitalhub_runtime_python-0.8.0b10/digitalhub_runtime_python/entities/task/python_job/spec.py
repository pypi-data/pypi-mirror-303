from __future__ import annotations

from digitalhub.entities.task._base.spec import TaskSpecK8s, TaskValidatorK8s


class TaskSpecPythonJob(TaskSpecK8s):
    """TaskSpecPythonJob specifications."""

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
        backoff_limit: int | None = None,
        schedule: str | None = None,
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
        self.backoff_limit = backoff_limit
        self.schedule = schedule


class TaskValidatorPythonJob(TaskValidatorK8s):
    """
    TaskValidatorPythonJob validator.
    """

    backoff_limit: int = None
    """Backoff limit."""

    schedule: str = None
    """Schedule."""
