from __future__ import annotations

import typing

from digitalhub.context.builder import context_builder

if typing.TYPE_CHECKING:
    from digitalhub.context.context import Context
    from digitalhub.entities.project._base.entity import Project


def check_context(project: str) -> None:
    """
    Check if the given project is in the context.

    Parameters
    ----------
    project : str
        Project name.

    Returns
    -------
    bool
        True if the project is in the context, False otherwise.
    """
    if project not in context_builder._instances:
        msg = f"Context missing. Set context by creating or importing a project named '{project}'."
        raise RuntimeError(msg)


def set_context(project: Project) -> None:
    """
    Wrapper for ContextBuilder.build().

    Parameters
    ----------
    project : Project
        The project object used to set the current context.

    Returns
    -------
    None
    """
    context_builder.build(project)


def get_context(project: str) -> Context:
    """
    Wrapper for ContextBuilder.get().

    Parameters
    ----------
    project : str
        Project name.

    Returns
    -------
    Context
        The context for the given project name.
    """
    return context_builder.get(project)


def set_context_object(context: Context) -> None:
    """
    Wrapper for ContextBuilder.set().

    Parameters
    ----------
    context : Context
        The context to set.

    Returns
    -------
    None
    """
    context_builder.set(context)


def delete_context(project: str) -> None:
    """
    Wrapper for ContextBuilder.remove().

    Parameters
    ----------
    project : str
        Project name.

    Returns
    -------
    None
    """
    context_builder.remove(project)
