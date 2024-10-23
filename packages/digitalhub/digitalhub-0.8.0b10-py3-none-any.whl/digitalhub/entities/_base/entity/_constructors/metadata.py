from __future__ import annotations

from digitalhub.entities._base.entity.metadata import Metadata
from digitalhub.utils.generic_utils import get_timestamp


def build_metadata(**kwargs) -> Metadata:
    """
    Build entity metadata object. This method is used to build entity
    metadata.

    Parameters
    ----------
    **kwargs : dict
        Keyword arguments for the constructor.

    Returns
    -------
    Metadata
        Metadata object.
    """
    kwargs = parse_arguments(**kwargs)
    return Metadata(**kwargs)


def parse_arguments(**kwargs) -> dict:
    """
    Parse keyword arguments and add default values if necessary.

    Parameters
    ----------
    **kwargs : dict
        Keyword arguments.

    Returns
    -------
    dict
        A dictionary containing the entity metadata attributes.
    """
    if "created" not in kwargs or kwargs["created"] is None:
        kwargs["created"] = get_timestamp()
    if "updated" not in kwargs or kwargs["updated"] is None:
        kwargs["updated"] = kwargs["created"]
    return kwargs
