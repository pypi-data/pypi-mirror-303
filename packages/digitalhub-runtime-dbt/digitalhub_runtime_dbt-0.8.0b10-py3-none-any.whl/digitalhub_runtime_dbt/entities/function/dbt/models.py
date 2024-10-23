from __future__ import annotations

from pathlib import Path

from digitalhub.entities.function._base.models import SourceCodeStruct, SourceCodeValidator
from digitalhub.utils.exceptions import EntityError
from digitalhub.utils.generic_utils import encode_string
from digitalhub.utils.uri_utils import map_uri_scheme


class SourceCodeStructDbt(SourceCodeStruct):
    """
    Source code struct for dbt.
    """

    @staticmethod
    def source_check(source: dict) -> dict:
        """
        Check source code.

        Parameters
        ----------
        source : dict
            Source.

        Returns
        -------
        dict
            Checked source.
        """
        source_path = source.get("source")
        code = source.get("code")
        base64 = source.get("base64")
        handler = source.get("handler")

        if source.get("lang") is None:
            source["lang"] = "sql"

        if source_path is None and code is None and base64 is None:
            raise EntityError("Source must be provided.")

        # Check source code

        if base64 is not None:
            return source

        if code is not None:
            source["base64"] = encode_string(code)
            return source

        if source_path is not None:
            if map_uri_scheme(source_path) == "local":
                source["code"] = Path(source_path).read_text()
                source["base64"] = encode_string(source["code"])
            else:
                if handler is None:
                    raise EntityError("Handler must be provided if source is not local.")

        return source


class SourceCodeValidatorDbt(SourceCodeValidator):
    """
    Source code params for dbt.
    """
