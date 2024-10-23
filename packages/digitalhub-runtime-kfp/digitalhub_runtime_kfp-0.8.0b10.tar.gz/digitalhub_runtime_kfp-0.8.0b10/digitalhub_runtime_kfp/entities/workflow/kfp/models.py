from __future__ import annotations

from pathlib import Path

from digitalhub.entities.function._base.models import SourceCodeStruct, SourceCodeValidator
from digitalhub.utils.exceptions import EntityError
from digitalhub.utils.generic_utils import encode_source, encode_string
from digitalhub.utils.uri_utils import map_uri_scheme


class SourceCodeStructKfp(SourceCodeStruct):
    """
    Source code struct for kfp.
    """

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


class SourceCodeValidatorKfp(SourceCodeValidator):
    """
    Source code params for kfp.
    """
