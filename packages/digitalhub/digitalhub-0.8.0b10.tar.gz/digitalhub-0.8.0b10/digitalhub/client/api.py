from __future__ import annotations

import typing

from digitalhub.client.builder import client_builder

if typing.TYPE_CHECKING:
    from digitalhub.client._base.client import Client


def check_client_exists(local: bool = False) -> bool:
    """
    Check if client exists.

    Parameters
    ----------
    local : bool
        Check client existence by local.

    Returns
    -------
    bool
        True if client exists, False otherwise.
    """
    if local:
        return client_builder._local is not None
    return client_builder._dhcore is not None


def build_client(local: bool = False, config: dict | None = None) -> None:
    """
    Wrapper around ClientBuilder.build.

    Parameters
    ----------
    local : bool
        Whether to create a local client or not.
    config : dict
        DHCore environment configuration.

    Returns
    -------
    Client
        The client instance.
    """
    client_builder.build(local, config)


def get_client(local: bool = False) -> Client:
    """
    Wrapper around ClientBuilder.build.

    Parameters
    ----------
    local : bool
        Whether to create a local client or not.

    Returns
    -------
    Client
        The client instance.
    """
    return client_builder.build(local)
