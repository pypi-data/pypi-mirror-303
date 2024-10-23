from __future__ import annotations

from abc import abstractmethod
from pathlib import Path

from pydantic import BaseModel

from digitalhub.utils.exceptions import EntityError
from digitalhub.utils.generic_utils import decode_string
from digitalhub.utils.uri_utils import map_uri_scheme


class SourceCodeStruct:
    """
    Source code struct.
    """

    def __init__(
        self,
        source: str | None = None,
        code: str | None = None,
        base64: str | None = None,
        handler: str | None = None,
        lang: str | None = None,
    ) -> None:
        self.source = source
        self.code = code
        self.base64 = base64
        self.handler = handler
        self.lang = lang

    @staticmethod
    @abstractmethod
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

    def show_source_code(self) -> str:
        """
        Show source code.

        Returns
        -------
        str
            Source code.
        """
        if self.code is not None:
            return self.code
        if self.base64 is not None:
            try:
                return decode_string(self.base64)
            except Exception:
                raise EntityError("Something got wrong during source code decoding.")
        if (self.source is not None) and (map_uri_scheme(self.source) == "local"):
            try:
                return Path(self.source).read_text()
            except Exception:
                raise EntityError("Cannot access source code.")
        return ""

    def to_dict(self) -> dict:
        """
        Convert to dictionary.

        Returns
        -------
        dict
            Dictionary representation of the object.
        """
        dict_ = {}
        if self.source is not None:
            dict_["source"] = self.source
        if self.base64 is not None:
            dict_["base64"] = self.base64
        if self.handler is not None:
            dict_["handler"] = self.handler
        if self.lang is not None:
            dict_["lang"] = self.lang

        return dict_

    def __repr__(self) -> str:
        return str(self.to_dict())


class SourceCodeValidator(BaseModel):
    """
    Source code params.
    """

    source: dict = None
    "Source code details as dictionary"

    code_src: str = None
    "Pointer to source code"

    handler: str = None
    "Function entrypoint"

    code: str = None
    "Source code (plain text)"

    base64: str = None
    "Source code (base64 encoded)"

    lang: str = None
    "Source code language (hint)"
