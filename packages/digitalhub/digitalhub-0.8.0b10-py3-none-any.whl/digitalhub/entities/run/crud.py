from __future__ import annotations

import typing

from digitalhub.entities._base.crud import (
    delete_entity,
    get_unversioned_entity,
    import_context_entity,
    list_context_entities,
    new_context_entity,
)
from digitalhub.entities.utils.entity_types import EntityTypes
from digitalhub.utils.exceptions import EntityError

if typing.TYPE_CHECKING:
    from digitalhub.entities.run._base.entity import Run


ENTITY_TYPE = EntityTypes.RUN.value


def new_run(
    project: str,
    kind: str,
    uuid: str | None = None,
    labels: list[str] | None = None,
    task: str | None = None,
    local_execution: bool = False,
    **kwargs,
) -> Run:
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
    labels : list[str]
        List of labels.
    task : str
        Name of the task associated with the run.
    local_execution : bool
        Flag to determine if object has local execution.
    **kwargs : dict
        Spec keyword arguments.

    Returns
    -------
    Run
        Object instance.

    Examples
    --------
    >>> obj = new_run(project="my-project",
    >>>               kind="python+run",
    >>>               task="task-string")
    """
    return new_context_entity(
        project=project,
        kind=kind,
        uuid=uuid,
        labels=labels,
        task=task,
        local_execution=local_execution,
        **kwargs,
    )


def get_run(
    identifier: str,
    project: str | None = None,
    **kwargs,
) -> Run:
    """
    Get object from backend.

    Parameters
    ----------
    identifier : str
        Entity key (store://...) or entity ID.
    project : str
        Project name.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    Run
        Object instance.

    Examples
    --------
    Using entity key:
    >>> obj = get_run("store://my-run-key")

    Using entity ID:
    >>> obj = get_run("my-run-id"
    >>>               project="my-project")
    """
    return get_unversioned_entity(
        identifier,
        entity_type=ENTITY_TYPE,
        project=project,
        **kwargs,
    )


def list_runs(project: str, **kwargs) -> list[Run]:
    """
    List all latest version objects from backend.

    Parameters
    ----------
    project : str
        Project name.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    list[Run]
        List of object instances.

    Examples
    --------
    >>> objs = list_runs(project="my-project")
    """
    # TODO more examples: search by function, latest for task and function
    return list_context_entities(
        project=project,
        entity_type=ENTITY_TYPE,
        **kwargs,
    )


def import_run(file: str) -> Run:
    """
    Get object from file.

    Parameters
    ----------
    file : str
        Path to YAML file.

    Returns
    -------
    Run
        Object instance.

    Example
    -------
    >>> obj = import_run("my-run.yaml")
    """
    return import_context_entity(file)


def update_run(entity: Run) -> Run:
    """
    Update object. Note that object spec are immutable.

    Parameters
    ----------
    entity : Run
        Object to update.

    Returns
    -------
    Run
        Entity updated.

    Examples
    --------
    >>> obj = update_run(obj)
    """
    return entity.save(update=True)


def delete_run(
    identifier: str,
    project: str | None = None,
    **kwargs,
) -> dict:
    """
    Delete object from backend.

    Parameters
    ----------
    identifier : str
        Entity key (store://...) or entity ID.
    project : str
        Project name.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Response from backend.

    Examples
    --------
    >>> obj = delete_run("store://my-run-key")
    >>> obj = delete_run("my-run-id", project="my-project")
    """
    if not identifier.startswith("store://") and project is None:
        raise EntityError("Specify entity key or entity ID combined with project")
    return delete_entity(
        identifier=identifier,
        entity_type=ENTITY_TYPE,
        project=project,
        entity_id=identifier,
        **kwargs,
    )

    # TODO read logs
