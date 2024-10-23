from __future__ import annotations

import typing

from digitalhub.entities.function._base.entity import Function

if typing.TYPE_CHECKING:
    from digitalhub_runtime_python.entities.function.python.spec import FunctionSpecPython
    from digitalhub_runtime_python.entities.function.python.status import FunctionStatusPython

    from digitalhub.entities._base.entity.metadata import Metadata


class FunctionPython(Function):
    """
    FunctionPython class.
    """

    def __init__(
        self,
        project: str,
        name: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: FunctionSpecPython,
        status: FunctionStatusPython,
        user: str | None = None,
    ) -> None:
        super().__init__(project, name, uuid, kind, metadata, spec, status, user)

        self.spec: FunctionSpecPython
        self.status: FunctionStatusPython
