from __future__ import annotations

import typing

import requests

from digitalhub.entities.run._base.entity import Run
from digitalhub.utils.exceptions import EntityError

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.run.modelserve_run.spec import RunSpecModelserveRun
    from digitalhub_runtime_modelserve.entities.run.modelserve_run.status import RunStatusModelserveRun

    from digitalhub.entities._base.entity.metadata import Metadata


class RunModelserveRun(Run):
    """
    RunModelserveRun class.
    """

    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: RunSpecModelserveRun,
        status: RunStatusModelserveRun,
        user: str | None = None,
    ) -> None:
        super().__init__(project, uuid, kind, metadata, spec, status, user)

        self.spec: RunSpecModelserveRun
        self.status: RunStatusModelserveRun

    def invoke(
        self,
        model_name: str | None = None,
        method: str = "POST",
        url: str | None = None,
        **kwargs,
    ) -> requests.Response:
        """
        Invoke served model. By default it exposes infer v2 endpoint.

        Parameters
        ----------
        model_name : str
            Name of the model.
        method : str
            Method of the request.
        url : str
            URL of the request.
        **kwargs : dict
            Keyword arguments to pass to the request.

        Returns
        -------
        requests.Response
            Response from the request.
        """
        if self._context().local:
            raise EntityError("Invoke not supported locally.")
        if url is None:
            model_name = model_name if model_name is not None else "model"
            url = f"http://{self.status.service.get('url')}/v2/models/{model_name}/infer"
        return requests.request(method=method, url=url, **kwargs)
