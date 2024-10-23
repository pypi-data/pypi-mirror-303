from __future__ import annotations

import typing

from digitalhub.context.api import check_context
from digitalhub.entities._base.api_utils import (
    delete_entity_api_ctx,
    list_entity_api_ctx,
    read_entity_api_ctx,
    read_entity_api_ctx_versions,
)
from digitalhub.factory.api import build_entity_from_dict, build_entity_from_params
from digitalhub.utils.exceptions import EntityAlreadyExistsError, EntityError
from digitalhub.utils.io_utils import read_yaml

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.context.entity import ContextEntity
    from digitalhub.entities._base.executable.entity import ExecutableEntity
    from digitalhub.entities._base.material.entity import MaterialEntity
    from digitalhub.entities._base.unversioned.entity import UnversionedEntity
    from digitalhub.entities._base.versioned.entity import VersionedEntity


def new_context_entity(**kwargs) -> ContextEntity:
    """
    Create a new object.

    Parameters
    ----------
    project : str
        Project name.
    kind : str
        Kind the object.
    uuid : str
        ID of the object.
    description : str
        Description of the object (human readable).
    labels : list[str]
        List of labels.
    embedded : bool
        Flag to determine if object spec must be embedded in project spec.

    Returns
    -------
    ContextEntity
        Object instance.
    """
    check_context(kwargs["project"])
    obj = build_entity_from_params(**kwargs)
    obj.save()
    return obj


def get_versioned_entity(
    identifier: str,
    entity_type: str | None = None,
    project: str | None = None,
    entity_id: str | None = None,
    **kwargs,
) -> VersionedEntity:
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
    VersionedEntity
        Object instance.
    """
    obj = read_entity_api_ctx(
        identifier,
        entity_type=entity_type,
        project=project,
        entity_id=entity_id,
        **kwargs,
    )
    return build_entity_from_dict(obj)


def get_unversioned_entity(
    identifier: str,
    entity_type: str | None = None,
    project: str | None = None,
    **kwargs,
) -> UnversionedEntity:
    """
    Get object from backend.

    Parameters
    ----------
    entity_type : str
        Entity type.
    identifier : str
        Entity key (store://...) or entity name.
    project : str
        Project name.
    entity_id : str
        Entity ID.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    UnversionedEntity
        Object instance.
    """
    if not identifier.startswith("store://") and project is None:
        raise EntityError("Specify entity key or entity ID combined with project")
    obj = read_entity_api_ctx(
        identifier,
        entity_type=entity_type,
        project=project,
        **kwargs,
    )
    return build_entity_from_dict(obj)


def get_material_entity(
    identifier: str,
    entity_type: str | None = None,
    project: str | None = None,
    entity_id: str | None = None,
    **kwargs,
) -> MaterialEntity:
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
    MaterialEntity
        Object instance.
    """
    obj: MaterialEntity = get_versioned_entity(
        identifier,
        entity_type=entity_type,
        project=project,
        entity_id=entity_id,
        **kwargs,
    )
    obj._get_files_info()
    return obj


def get_context_entity_versions(
    identifier: str,
    entity_type: str | None = None,
    project: str | None = None,
    **kwargs,
) -> list[ContextEntity]:
    """
    Get object versions from backend.

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
    list[ContextEntity]
        List of object instances.
    """
    obj = read_entity_api_ctx_versions(
        identifier,
        entity_type=entity_type,
        project=project,
        **kwargs,
    )
    return [build_entity_from_dict(o) for o in obj]


def get_material_entity_versions(
    identifier: str,
    entity_type: str | None = None,
    project: str | None = None,
    **kwargs,
) -> list[MaterialEntity]:
    """
    Get object versions from backend.

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
    list[MaterialEntity]
        List of object instances.
    """
    objs = read_entity_api_ctx_versions(
        identifier,
        entity_type=entity_type,
        project=project,
        **kwargs,
    )
    objects = []
    for o in objs:
        entity: MaterialEntity = build_entity_from_dict(o)
        entity._get_files_info()
        objects.append(entity)
    return objects


def list_context_entities(project: str, entity_type: str, **kwargs) -> list[ContextEntity]:
    """
    List all latest version objects from backend.

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
    list[ContextEntity]
        List of object instances.
    """
    objs = list_entity_api_ctx(
        project=project,
        entity_type=entity_type,
        **kwargs,
    )
    return [build_entity_from_dict(obj) for obj in objs]


def list_material_entities(
    project: str,
    entity_type: str,
    **kwargs,
) -> list[MaterialEntity]:
    """
    List all latest version objects from backend.

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
    list[MaterialEntity]
        List of object instances.
    """
    objs = list_entity_api_ctx(
        project=project,
        entity_type=entity_type,
        **kwargs,
    )
    objects = []
    for o in objs:
        entity: MaterialEntity = build_entity_from_dict(o)
        entity._get_files_info()
        objects.append(entity)
    return objects


def import_context_entity(file: str) -> ContextEntity:
    """
    Get object from file.

    Parameters
    ----------
    file : str
        Path to YAML file.

    Returns
    -------
    ContextEntity
        Object instance.
    """
    dict_obj: dict = read_yaml(file)

    check_context(dict_obj["project"])

    obj = build_entity_from_dict(dict_obj)
    try:
        obj.save()
    except EntityAlreadyExistsError:
        pass
    return obj


def import_executable_entity(file: str) -> ExecutableEntity:
    """
    Get object from file.

    Parameters
    ----------
    file : str
        Path to YAML file.

    Returns
    -------
    ExecutableEntity
        Object instance.
    """
    dict_obj: dict | list[dict] = read_yaml(file)
    if isinstance(dict_obj, list):
        exec_dict = dict_obj[0]
        tsk_dicts = dict_obj[1:]
    else:
        exec_dict = dict_obj
        tsk_dicts = []

    check_context(exec_dict["project"])

    obj: ExecutableEntity = build_entity_from_dict(exec_dict)

    obj.import_tasks(tsk_dicts)

    try:
        obj.save()
    except EntityAlreadyExistsError:
        pass
    return obj


def delete_entity(
    identifier: str,
    entity_type: str | None = None,
    project: str | None = None,
    entity_id: str | None = None,
    delete_all_versions: bool = False,
    cascade: bool = True,
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
    delete_all_versions : bool
        Delete all versions of the named entity. If True, use entity name instead of entity key as identifier.
    cascade : bool
        Cascade delete.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Response from backend.
    """
    return delete_entity_api_ctx(
        identifier=identifier,
        entity_type=entity_type,
        project=project,
        entity_id=entity_id,
        delete_all_versions=delete_all_versions,
        cascade=cascade,
        **kwargs,
    )
