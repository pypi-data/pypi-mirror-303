from __future__ import annotations

import typing
from abc import ABCMeta, abstractmethod
from typing import Any

from digitalhub.readers.api import get_reader_by_engine

if typing.TYPE_CHECKING:
    from digitalhub.stores._base.store import Store


class Datastore(metaclass=ABCMeta):
    """
    Datastore abstract class.
    """

    def __init__(self, store: Store, **kwargs) -> None:
        self.store = store

    ##############################
    # IO methods
    ##############################

    @abstractmethod
    def write_df(self, df: Any, dst: str, extension: str | None = None, **kwargs) -> str:
        """
        Write DataFrame as parquet or csv.
        """

    def read_df(
        self,
        path: str | list[str],
        extension: str,
        engine: str | None = None,
        **kwargs,
    ) -> Any:
        """
        Read DataFrame from path.

        Parameters
        ----------
        path : str | list[str]
            Path(s) to read DataFrame from.
        extension : str
            Extension of the file.
        engine : str
            Dataframe engine (pandas, polars, etc.).
        **kwargs : dict
            Keyword arguments.

        Returns
        -------
        Any
            DataFrame.
        """
        reader = get_reader_by_engine(engine)
        self._validate_extension(extension)
        return reader.read_df(path, extension, **kwargs)

    ##############################
    # Helper methods
    ##############################

    @staticmethod
    def _validate_extension(extension: str) -> None:
        """
        Validate extension.

        Parameters
        ----------
        extension : str
            Extension of the file.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If extension is not supported.
        """
        if extension not in ["csv", "parquet", "file"]:
            raise ValueError(f"Extension {extension} not supported.")
