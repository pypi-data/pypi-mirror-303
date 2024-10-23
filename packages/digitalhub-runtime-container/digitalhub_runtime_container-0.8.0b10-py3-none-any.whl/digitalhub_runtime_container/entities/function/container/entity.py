from __future__ import annotations

import typing

from digitalhub.entities.function._base.entity import Function

if typing.TYPE_CHECKING:
    from digitalhub_runtime_container.entities.function.container.spec import FunctionSpecContainer
    from digitalhub_runtime_container.entities.function.container.status import FunctionStatusContainer

    from digitalhub.entities._base.entity.metadata import Metadata


class FunctionContainer(Function):
    """
    FunctionContainer class.
    """

    def __init__(
        self,
        project: str,
        name: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: FunctionSpecContainer,
        status: FunctionStatusContainer,
        user: str | None = None,
    ) -> None:
        super().__init__(project, name, uuid, kind, metadata, spec, status, user)

        self.spec: FunctionSpecContainer
        self.status: FunctionStatusContainer
