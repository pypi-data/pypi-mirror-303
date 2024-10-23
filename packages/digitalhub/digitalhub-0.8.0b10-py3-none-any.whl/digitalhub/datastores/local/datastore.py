from __future__ import annotations

import typing
from pathlib import Path
from typing import Any

from digitalhub.datastores._base.datastore import Datastore
from digitalhub.readers.api import get_reader_by_object

if typing.TYPE_CHECKING:
    from digitalhub.stores.local.store import LocalStore


class LocalDatastore(Datastore):
    """
    Local Datastore class.
    """

    def __init__(self, store: LocalStore, **kwargs) -> None:
        super().__init__(store, **kwargs)
        self.store: LocalStore

    def write_df(self, df: Any, dst: str, extension: str | None = None, **kwargs) -> str:
        """
        Method to write a dataframe to a file. Kwargs are passed to df.to_parquet().
        If destination is not provided, the dataframe is written to the default
        store path with generated name.

        Parameters
        ----------
        df : Any
            The dataframe to write.
        dst : str
            The destination of the dataframe.
        **kwargs : dict
            Keyword arguments.

        Returns
        -------
        str
            Path of written dataframe.
        """
        self.store._check_local_dst(dst)
        self._validate_extension(Path(dst).suffix.removeprefix("."))

        # Write dataframe
        reader = get_reader_by_object(df)
        reader.write_df(df, dst, extension=extension, **kwargs)

        return dst
