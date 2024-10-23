from __future__ import annotations

import typing

from digitalhub.entities.task._base.entity import Task

if typing.TYPE_CHECKING:
    from digitalhub_runtime_container.entities.task.container_serve.spec import TaskSpecContainerServe
    from digitalhub_runtime_container.entities.task.container_serve.status import TaskStatusContainerServe

    from digitalhub.entities._base.entity.metadata import Metadata


class TaskContainerServe(Task):
    """
    TaskContainerServe class.
    """

    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: TaskSpecContainerServe,
        status: TaskStatusContainerServe,
        user: str | None = None,
    ) -> None:
        super().__init__(project, uuid, kind, metadata, spec, status, user)

        self.spec: TaskSpecContainerServe
        self.status: TaskStatusContainerServe
