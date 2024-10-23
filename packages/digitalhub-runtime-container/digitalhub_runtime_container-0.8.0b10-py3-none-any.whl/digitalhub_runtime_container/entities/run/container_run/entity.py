from __future__ import annotations

import typing

import requests

from digitalhub.entities.run._base.entity import Run
from digitalhub.utils.exceptions import EntityError

if typing.TYPE_CHECKING:
    from digitalhub_runtime_container.entities.run.container_run.spec import RunSpecContainerRun
    from digitalhub_runtime_container.entities.run.container_run.status import RunStatusContainerRun

    from digitalhub.entities._base.entity.metadata import Metadata


class RunContainerRun(Run):
    """
    RunContainerRun class.
    """

    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: RunSpecContainerRun,
        status: RunStatusContainerRun,
        user: str | None = None,
    ) -> None:
        super().__init__(project, uuid, kind, metadata, spec, status, user)

        self.spec: RunSpecContainerRun
        self.status: RunStatusContainerRun

    def invoke(
        self,
        method: str = "POST",
        url: str | None = None,
        **kwargs,
    ) -> requests.Response:
        """
        Invoke run.

        Parameters
        ----------
        method : str
            Method of the request.
        url : str
            URL of the request.
        **kwargs : dict
            Keyword arguments to pass to the request.

        Returns
        -------
        requests.Response
            Response from service.
        """
        if self._context().local:
            raise EntityError("Invoke not supported locally.")
        if url is None:
            url = f"http://{self.status.service.get('url')}"
        return requests.request(method=method, url=url, **kwargs)
