from __future__ import annotations

from pathlib import Path

from digitalhub.entities.function._base.models import SourceCodeStruct, SourceCodeValidator
from digitalhub.utils.exceptions import EntityError
from digitalhub.utils.generic_utils import encode_source, encode_string
from digitalhub.utils.uri_utils import map_uri_scheme


class SourceCodeStructPython(SourceCodeStruct):
    """
    Source code struct for python.
    """

    def __init__(
        self,
        source: str | None = None,
        handler: str | None = None,
        code: str | None = None,
        base64: str | None = None,
        lang: str | None = None,
        init_function: str | None = None,
    ) -> None:
        super().__init__(
            source=source,
            handler=handler,
            code=code,
            base64=base64,
            lang=lang,
        )
        self.init_function = init_function

    @staticmethod
    def source_check(source: dict) -> dict:
        """
        Check source. Overrides SourceCodeStruct.source_check.

        Parameters
        ----------
        source : dict
            Source.

        Returns
        -------
        dict
            Checked source.
        """
        # Source check
        source_path = source.get("source")
        code = source.get("code")
        base64 = source.get("base64")
        handler = source.get("handler")
        source["lang"] = "python"

        if handler is None:
            raise EntityError("Handler must be provided.")

        if source_path is None and code is None and base64 is None:
            raise EntityError("Source must be provided.")

        if base64 is not None:
            return source

        if code is not None:
            source["base64"] = encode_string(code)
            return source

        if source_path is not None:
            if map_uri_scheme(source_path) == "local":
                if not (Path(source_path).suffix == ".py" and Path(source_path).is_file()):
                    raise EntityError("Source is not a valid python file.")
                source["base64"] = encode_source(source_path)
            else:
                if handler is None:
                    raise EntityError("Handler must be provided if source is not local.")

        return source

    def to_dict(self) -> dict:
        """
        Convert to dictionary.

        Returns
        -------
        dict
            Dictionary representation of the object.
        """
        dict_ = super().to_dict()
        if self.init_function is not None:
            dict_["init_function"] = self.init_function
        return dict_


class SourceCodeValidatorPython(SourceCodeValidator):
    """
    SourceCodeValidatorPython validator.
    """

    init_function: str = None
    """Handler for init function."""
