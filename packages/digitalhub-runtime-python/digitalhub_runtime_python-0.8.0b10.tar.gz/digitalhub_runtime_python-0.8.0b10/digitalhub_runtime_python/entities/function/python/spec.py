from __future__ import annotations

from typing import Literal

from digitalhub_runtime_python.entities.function.python.models import SourceCodeStructPython, SourceCodeValidatorPython

from digitalhub.entities.function._base.spec import FunctionSpec, FunctionValidator


class FunctionSpecPython(FunctionSpec):
    """
    FunctionSpecPython specifications.
    """

    def __init__(
        self,
        source: dict | None = None,
        code_src: str | None = None,
        handler: str | None = None,
        code: str | None = None,
        base64: str | None = None,
        init_function: str | None = None,
        lang: str | None = None,
        image: str | None = None,
        base_image: str | None = None,
        python_version: str | None = None,
        requirements: list | None = None,
    ) -> None:
        super().__init__()

        self.image = image
        self.base_image = base_image
        self.python_version = python_version
        self.requirements = requirements

        # Give source precedence
        if source is not None:
            source_dict = source
        else:
            source_dict = {
                "source": code_src,
                "handler": handler,
                "code": code,
                "base64": base64,
                "lang": lang,
                "init_function": init_function,
            }

        source_checked = self.source_check(source_dict)
        self.source = SourceCodeStructPython(**source_checked)

    @staticmethod
    def source_check(source: dict) -> dict:
        """
        Check source.

        Parameters
        ----------
        source : dict
            Source.

        Returns
        -------
        dict
            Checked source.
        """
        return SourceCodeStructPython.source_check(source)

    def show_source_code(self) -> str:
        """
        Show source code.

        Returns
        -------
        str
            Source code.
        """
        return self.source.show_source_code()

    def to_dict(self) -> dict:
        """
        Override to_dict to exclude code from source.

        Returns
        -------
        dict
            Dictionary representation of the object.
        """
        dict_ = super().to_dict()
        dict_["source"] = self.source.to_dict()
        return dict_


class FunctionValidatorPython(FunctionValidator, SourceCodeValidatorPython):
    """
    FunctionValidatorPython validator.
    """

    python_version: Literal["PYTHON3_9", "PYTHON3_10", "PYTHON3_11"]
    "Python version"

    image: str = None
    "Image where the function will be executed"

    base_image: str = None
    "Base image used to build the image where the function will be executed"

    requirements: list = None
    "Requirements list to be installed in the image where the function will be executed"
