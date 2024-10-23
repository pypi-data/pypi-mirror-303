from __future__ import annotations

import typing
from typing import Any

import requests
from digitalhub_runtime_python.entities.run.python_run.utils import get_getter_for_material

from digitalhub.entities.run._base.entity import Run
from digitalhub.entities.utils.utils import get_entity_type_from_key
from digitalhub.utils.exceptions import EntityError

if typing.TYPE_CHECKING:
    from digitalhub_runtime_python.entities.run.python_run.spec import RunSpecPythonRun
    from digitalhub_runtime_python.entities.run.python_run.status import RunStatusPythonRun

    from digitalhub.entities._base.entity.metadata import Metadata
    from digitalhub.entities._base.material.entity import MaterialEntity


class RunPythonRun(Run):
    """
    RunPythonRun class.
    """

    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: RunSpecPythonRun,
        status: RunStatusPythonRun,
        user: str | None = None,
    ) -> None:
        super().__init__(project, uuid, kind, metadata, spec, status, user)

        self.spec: RunSpecPythonRun
        self.status: RunStatusPythonRun

    def _setup_execution(self) -> None:
        """
        Setup run execution.

        Returns
        -------
        None
        """
        self.refresh()
        self.spec.inputs = self.inputs(as_dict=True)

    def inputs(self, as_dict: bool = False) -> dict:
        """
        Get inputs passed in spec as objects or as dictionaries.

        Parameters
        ----------
        as_dict : bool
            If True, return inputs as dictionaries.

        Returns
        -------
        dict
            Inputs.
        """
        inputs = {}
        if self.inputs is None:
            return inputs

        for parameter, key in self.spec.inputs.items():
            entity_type = get_entity_type_from_key(key)
            entity = get_getter_for_material(entity_type)(key)
            if as_dict:
                entity = entity.to_dict()
            inputs[parameter] = entity

        return inputs

    def output(
        self,
        output_name: str,
        as_key: bool = False,
        as_dict: bool = False,
    ) -> MaterialEntity | dict | str | None:
        """
        Get run's output by name.

        Parameters
        ----------
        output_name : str
            Key of the result.
        as_key : bool
            If True, return result as key.
        as_dict : bool
            If True, return result as dictionary.

        Returns
        -------
        Entity | dict | str | None
            Result.
        """
        return self.outputs(as_key=as_key, as_dict=as_dict).get(output_name)

    def outputs(
        self,
        as_key: bool = False,
        as_dict: bool = False,
    ) -> MaterialEntity | dict | str | None:
        """
        Get run's outputs.

        Parameters
        ----------
        as_key : bool
            If True, return results as keys.
        as_dict : bool
            If True, return results as dictionaries.

        Returns
        -------
        dict
            List of output objects.
        """
        outputs = {}
        if self.status.outputs is None:
            return outputs

        for parameter, key in self.status.outputs.items():
            entity_type = get_entity_type_from_key(key)
            entity = get_getter_for_material(entity_type)(key)
            if as_key:
                entity = entity.key
            if as_dict:
                entity = entity.to_dict()
            outputs[parameter] = entity

        return outputs

    def result(self, result_name: str) -> Any:
        """
        Get result by name.

        Parameters
        ----------
        result_name : str
            Name of the result.

        Returns
        -------
        Any
            The result.
        """
        return self.results().get(result_name)

    def results(self) -> dict:
        """
        Get results.

        Returns
        -------
        dict
            The results.
        """
        if self.status.results is None:
            return {}
        return self.status.results

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
