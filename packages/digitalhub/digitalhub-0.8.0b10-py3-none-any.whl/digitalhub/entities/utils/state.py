from __future__ import annotations

from enum import Enum


class State(Enum):
    """
    State enumeration.
    """

    BUILT = "BUILT"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    CREATED = "CREATED"
    CREATING = "CREATING"
    DELETED = "DELETED"
    DELETING = "DELETING"
    ERROR = "ERROR"
    FSM_ERROR = "FSM_ERROR"
    IDLE = "IDLE"
    NONE = "NONE"
    ONLINE = "ONLINE"
    PENDING = "PENDING"
    READY = "READY"
    RESUME = "RESUME"
    RUN_ERROR = "RUN_ERROR"
    RUNNING = "RUNNING"
    STOP = "STOP"
    STOPPED = "STOPPED"
    SUCCESS = "SUCCESS"
    UNKNOWN = "UNKNOWN"
