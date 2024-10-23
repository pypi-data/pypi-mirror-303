from __future__ import annotations

from digitalhub.entities.task._base.models import CorePort
from digitalhub.entities.task._base.spec import TaskSpecK8s, TaskValidatorK8s


class TaskSpecContainerServe(TaskSpecK8s):
    """
    TaskSpecContainerServe specifications.
    """

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
        service_ports: list | None = None,
        service_type: str | None = None,
        fsGroup: int | None = None,
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
        self.service_ports = service_ports
        self.service_type = service_type
        self.fsGroup = fsGroup


class TaskValidatorContainerServe(TaskValidatorK8s):
    """
    TaskValidatorContainerServe validator.
    """

    replicas: int = None
    """Replicas."""

    service_ports: list[CorePort] = None
    """Service ports mapper."""

    service_type: str = None
    """Service type."""

    fsGroup: int = None
    """FSGroup."""
