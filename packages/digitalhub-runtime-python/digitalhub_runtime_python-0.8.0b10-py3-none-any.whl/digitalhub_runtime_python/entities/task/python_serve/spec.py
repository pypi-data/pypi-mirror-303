from __future__ import annotations

from typing import Literal

from digitalhub.entities.task._base.spec import TaskSpecK8s, TaskValidatorK8s


class TaskSpecPythonServe(TaskSpecK8s):
    """TaskSpecPythonServe specifications."""

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
        replicas: int | None = None,
        service_type: str | None = None,
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
        self.replicas = replicas
        self.service_type = service_type


class TaskValidatorPythonServe(TaskValidatorK8s):
    """
    TaskValidatorPythonServe validator.
    """

    replicas: int = None
    service_type: Literal["ClusterIP", "NodePort", "LoadBalancer"] = "NodePort"
