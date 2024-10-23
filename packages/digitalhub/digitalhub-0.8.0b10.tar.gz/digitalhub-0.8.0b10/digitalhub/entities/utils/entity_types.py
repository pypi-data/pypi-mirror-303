from __future__ import annotations

from enum import Enum


class EntityTypes(Enum):
    """
    Entity types.
    """

    PROJECT = "project"
    ARTIFACT = "artifact"
    DATAITEM = "dataitem"
    MODEL = "model"
    SECRET = "secret"
    FUNCTION = "function"
    WORKFLOW = "workflow"
    TASK = "task"
    RUN = "run"
