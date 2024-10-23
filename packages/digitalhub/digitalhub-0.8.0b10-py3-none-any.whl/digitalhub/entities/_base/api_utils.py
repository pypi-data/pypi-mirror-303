from __future__ import annotations

import typing

from digitalhub.context.api import get_context
from digitalhub.entities.utils.api import (
    api_base_create,
    api_base_delete,
    api_base_list,
    api_base_read,
    api_base_update,
    api_ctx_create,
    api_ctx_data,
    api_ctx_delete,
    api_ctx_files,
    api_ctx_list,
    api_ctx_logs,
    api_ctx_read,
    api_ctx_resume,
    api_ctx_stop,
    api_ctx_update,
)
from digitalhub.entities.utils.utils import parse_entity_key

if typing.TYPE_CHECKING:
    from digitalhub.client._base.client import Client


##############################
# CRUD base entity
##############################


def create_entity_api_base(
    client: Client,
    entity_type: str,
    entity_dict: dict,
    **kwargs,
) -> dict:
    """
    Create object in backend.

    Parameters
    ----------
    client : Client
        Client instance.
    entity_type : str
        Entity type.
    entity_dict : dict
        Object instance.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Object instance.
    """
    api = api_base_create(entity_type)
    return client.create_object(api, entity_dict, **kwargs)


def read_entity_api_base(
    client: Client,
    entity_type: str,
    entity_name: str,
    **kwargs,
) -> dict:
    """
    Read object from backend.

    Parameters
    ----------
    client : Client
        Client instance.
    entity_type : str
        Entity type.
    entity_name : str
        Entity name.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Object instance.
    """
    api = api_base_read(entity_type, entity_name)
    return client.read_object(api, **kwargs)


def list_entity_api_base(
    client: Client,
    entity_type: str,
    **kwargs,
) -> list[dict]:
    """
    List objects from backend.

    Parameters
    ----------
    entity_type : str
        Entity type.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    list[dict]
        List of objects.
    """
    api = api_base_list(entity_type)
    return client.list_objects(api, **kwargs)


def update_entity_api_base(
    client: Client,
    entity_type: str,
    entity_name: str,
    entity_dict: dict,
    **kwargs,
) -> dict:
    """
    Update object. Note that object spec are immutable.

    Parameters
    ----------
    client : Client
        Client instance.
    entity_type : str
        Entity type.
    entity_name : str
        Entity name.
    entity_dict : dict
        Object instance.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Object instance.
    """
    api = api_base_update(entity_type, entity_name)
    return client.update_object(api, entity_dict, **kwargs)


def delete_entity_api_base(
    client: Client,
    entity_type: str,
    entity_name: str,
    **kwargs,
) -> dict:
    """
    Delete object from backend.

    Parameters
    ----------
    client : Client
        Client instance.
    entity_type : str
        Entity type.
    entity_name : str
        Entity name.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Object instance.
    """
    if "params" not in kwargs:
        kwargs["params"] = {}
    if "cascade" in kwargs["params"]:
        kwargs["params"]["cascade"] = str(kwargs["cascade"]).lower()
    if "cascade" in kwargs:
        kwargs["params"]["cascade"] = str(kwargs.pop("cascade")).lower()
    api = api_base_delete(entity_type, entity_name)
    return client.delete_object(api, **kwargs)


##############################
# CRUD context entity
##############################


def create_entity_api_ctx(
    project: str,
    entity_type: str,
    entity_dict: dict,
    **kwargs,
) -> dict:
    """
    Create object in backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_type : str
        Entity type.
    entity_dict : dict
        Object instance.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Object instance.
    """
    api = api_ctx_create(project, entity_type)
    return get_context(project).create_object(api, entity_dict, **kwargs)


def read_entity_api_ctx(
    identifier: str,
    entity_type: str | None = None,
    project: str | None = None,
    entity_id: str | None = None,
    **kwargs,
) -> dict:
    """
    Get object from backend.

    Parameters
    ----------
    identifier : str
        Entity key (store://...) or entity name.
    entity_type : str
        Entity type.
    project : str
        Project name.
    entity_id : str
        Entity ID.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Object instance.
    """

    if identifier.startswith("store://"):
        project, entity_type, _, _, entity_id = parse_entity_key(identifier)
        api = api_ctx_read(project, entity_type, entity_id)
        return get_context(project).read_object(api, **kwargs)

    if project is None or entity_type is None:
        raise ValueError("Project and entity type must be specified.")

    if "params" not in kwargs:
        kwargs["params"] = {}

    if entity_id is None:
        kwargs["params"]["name"] = identifier
        api = api_ctx_list(project, entity_type)
        return get_context(project).list_first_object(api, **kwargs)

    api = api_ctx_read(project, entity_type, entity_id)
    return get_context(project).read_object(api, **kwargs)


def read_entity_api_ctx_versions(
    identifier: str,
    entity_type: str | None = None,
    project: str | None = None,
    **kwargs,
) -> list[dict]:
    """
    Get all versions object from backend.

    Parameters
    ----------
    identifier : str
        Entity key (store://...) or entity name.
    entity_type : str
        Entity type.
    project : str
        Project name.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    list[dict]
        Object instances.
    """
    if not identifier.startswith("store://"):
        if project is None or entity_type is None:
            raise ValueError("Project and entity type must be specified.")
        entity_name = identifier
    else:
        project, entity_type, _, entity_name, _ = parse_entity_key(identifier)

    if "params" not in kwargs:
        kwargs["params"] = {}
    kwargs["params"]["name"] = entity_name
    kwargs["params"]["versions"] = "all"

    api = api_ctx_list(project, entity_type)
    return get_context(project).list_objects(api, **kwargs)


def list_entity_api_ctx(
    project: str,
    entity_type: str,
    **kwargs,
) -> list[dict]:
    """
    List objects from backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_type : str
        Entity type.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    list[dict]
        List of objects.
    """
    api = api_ctx_list(project, entity_type)
    return get_context(project).list_objects(api, **kwargs)


def update_entity_api_ctx(
    project: str,
    entity_type: str,
    entity_id: str,
    entity_dict: dict,
    **kwargs,
) -> dict:
    """
    Update object. Note that object spec are immutable.

    Parameters
    ----------
    project : str
        Project name.
    entity_type : str
        Entity type.
    entity_id : str
        Entity ID.
    entity_dict : dict
        Entity dictionary.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_update(project, entity_type, entity_id=entity_id)
    return get_context(project).update_object(api, entity_dict, **kwargs)


def delete_entity_api_ctx(
    identifier: str,
    entity_type: str,
    project: str | None = None,
    entity_id: str | None = None,
    **kwargs,
) -> dict:
    """
    Delete object from backend.

    Parameters
    ----------
    identifier : str
        Entity key (store://...) or entity name.
    entity_type : str
        Entity type.
    project : str
        Project name.
    entity_id : str
        Entity ID.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Response from backend.
    """
    if "params" not in kwargs:
        kwargs["params"] = {}
    if "cascade" in kwargs["params"]:
        kwargs["params"]["cascade"] = str(kwargs["cascade"]).lower()
    if "cascade" in kwargs:
        kwargs["params"]["cascade"] = str(kwargs.pop("cascade")).lower()

    delete_all_versions: bool = kwargs.pop("delete_all_versions", False)

    if identifier.startswith("store://"):
        project, _, _, _, entity_id = parse_entity_key(identifier)
        api = api_ctx_delete(project, entity_type, entity_id)
        return get_context(project).delete_object(api, **kwargs)

    if project is None:
        raise ValueError("Project must be provided.")

    if entity_id is not None:
        api = api_ctx_delete(project, entity_type, entity_id)
    else:
        kwargs["params"]["name"] = identifier
        api = api_ctx_list(project, entity_type)
        if delete_all_versions:
            return get_context(project).delete_object(api, **kwargs)
        obj = get_context(project).list_first_object(api, **kwargs)
        entity_id = obj["id"]

    api = api_ctx_delete(project, entity_type, entity_id)
    return get_context(project).delete_object(api, **kwargs)


def set_data_api(
    project: str,
    entity_type: str,
    data: dict,
    **kwargs,
) -> None:
    """
    Set data in backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_type : str
        Entity type.
    data : dict
        Data dictionary.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    None
    """
    api = api_ctx_data(project, entity_type)
    get_context(project).update_object(api, data, **kwargs)


def get_data_api(
    project: str,
    entity_type: str,
    **kwargs,
) -> dict:
    """
    Read data from backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_type : str
        Entity type.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_data(project, entity_type)
    return get_context(project).read_object(api, **kwargs)


def logs_api(
    project: str,
    entity_type: str,
    entity_id: str,
    **kwargs,
) -> dict:
    """
    Read logs from backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_type : str
        Entity type.
    entity_id : str
        Entity ID.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_logs(project, entity_type, entity_id)
    return get_context(project).read_object(api, **kwargs)


def stop_api(
    project: str,
    entity_type: str,
    entity_id: str,
    **kwargs,
) -> None:
    """
    Stop object in backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_type : str
        Entity type.
    entity_id : str
        Entity ID.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    None
    """
    api = api_ctx_stop(project, entity_type, entity_id)
    get_context(project).create_object(api, obj={}, **kwargs)


def resume_api(
    project: str,
    entity_type: str,
    entity_id: str,
    **kwargs,
) -> None:
    """
    Resume object in backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_type : str
        Entity type.
    entity_id : str
        Entity ID.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    None
    """
    api = api_ctx_resume(project, entity_type, entity_id)
    get_context(project).create_object(api, obj={}, **kwargs)


def files_info_get_api(
    project: str,
    entity_type: str,
    entity_id: str,
    **kwargs,
) -> list[dict]:
    """
    Get files info from backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_type : str
        Entity type.
    entity_id : str
        Entity ID.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    list[dict]
        Response from backend.
    """
    api = api_ctx_files(project, entity_type, entity_id)
    return get_context(project).read_object(api, **kwargs)


def files_info_put_api(
    project: str,
    entity_type: str,
    entity_id: str,
    entity_list: list[dict],
    **kwargs,
) -> None:
    """
    Get files info from backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_type : str
        Entity type.
    entity_id : str
        Entity ID.
    entity_list : list[dict]
        Entity list.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    None
    """
    api = api_ctx_files(project, entity_type, entity_id)
    get_context(project).update_object(api, entity_list, **kwargs)
