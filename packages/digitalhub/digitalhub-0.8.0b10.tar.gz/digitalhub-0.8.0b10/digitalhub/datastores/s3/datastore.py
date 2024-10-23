from __future__ import annotations

import typing
from io import BytesIO
from typing import Any

from digitalhub.datastores._base.datastore import Datastore
from digitalhub.readers.api import get_reader_by_object

if typing.TYPE_CHECKING:
    from digitalhub.stores.s3.store import S3Store


class S3Datastore(Datastore):
    """
    S3 Datastore class.
    """

    def __init__(self, store: S3Store, **kwargs) -> None:
        super().__init__(store, **kwargs)
        self.store: S3Store

    def write_df(self, df: Any, dst: str, extension: str | None = None, **kwargs) -> str:
        """
        Write a dataframe to S3 based storage. Kwargs are passed to df.to_parquet().

        Parameters
        ----------
        df : Any
            The dataframe.
        dst : str
            The destination path on S3 based storage.
        **kwargs : dict
            Keyword arguments.

        Returns
        -------
        str
            The S3 path where the dataframe was saved.
        """
        fileobj = BytesIO()
        reader = get_reader_by_object(df)
        reader.write_df(df, fileobj, extension=extension, **kwargs)

        key = self.store._get_key(dst)
        return self.store.upload_fileobject(fileobj, key)
