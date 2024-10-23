from __future__ import annotations

import typing
from typing import Any

from digitalhub.datastores._base.datastore import Datastore

if typing.TYPE_CHECKING:
    from digitalhub.stores.remote.store import RemoteStore


class RemoteDatastore(Datastore):
    """
    Remote Datastore class.
    """

    def __init__(self, store: RemoteStore, **kwargs) -> None:
        super().__init__(store, **kwargs)
        self.store: RemoteStore

    def write_df(self, df: Any, dst: str, extension: str | None = None, **kwargs) -> str:
        """
        Method to write a dataframe to a file. Note that this method is not implemented
        since the remote store is not meant to write dataframes.

        Raises
        ------
        NotImplementedError
            This method is not implemented.
        """
        raise NotImplementedError("Remote store does not support write_df.")
