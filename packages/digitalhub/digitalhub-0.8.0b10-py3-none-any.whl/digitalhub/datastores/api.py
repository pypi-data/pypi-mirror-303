from __future__ import annotations

import typing

from digitalhub.datastores.builder import builder

if typing.TYPE_CHECKING:
    from digitalhub.datastores._base.datastore import Datastore


def get_datastore(uri: str) -> Datastore:
    """
    Get a datastore instance by URI.

    Parameters
    ----------
    uri : str
        URI to parse.

    Returns
    -------
    Datastore
        The datastore instance.
    """
    return builder.get(uri)


def get_default_datastore() -> Datastore:
    """
    Get the default datastore instance.

    Returns
    -------
    Datastore
        The default datastore instance.
    """
    return builder.default()
