from __future__ import annotations

import typing
from abc import ABCMeta, abstractmethod

from digitalhub.entities._base._base.entity import Base
from digitalhub.factory.api import build_entity_from_dict

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata
    from digitalhub.entities._base.entity.spec import Spec
    from digitalhub.entities._base.entity.status import Status


class Entity(Base, metaclass=ABCMeta):
    """
    Abstract class for entities.

    An entity is a collection of metadata, specifications.and status
    representing a variety of objects handled by Digitalhub.
    """

    # Entity type
    # Need to be set in subclasses
    ENTITY_TYPE: str

    # Attributes to render as dict. Need to be expanded in subclasses.
    _obj_attr = ["kind", "metadata", "spec", "status", "user", "key"]

    def __init__(
        self,
        kind: str,
        metadata: Metadata,
        spec: Spec,
        status: Status,
        user: str | None = None,
    ) -> None:
        self.kind = kind
        self.metadata = metadata
        self.spec = spec
        self.status = status
        self.user = user

        # Need to be set in subclasses
        self.key: str

    @abstractmethod
    def save(self, update: bool = False) -> Entity:
        """
        Abstract save method.
        """

    @abstractmethod
    def refresh(self) -> Entity:
        """
        Abstract refresh method.
        """

    def _update_attributes(self, obj: dict) -> None:
        """
        Update attributes.

        Parameters
        ----------
        obj : dict
            Mapping representation of object.

        Returns
        -------
        None
        """
        new_obj = build_entity_from_dict(obj)
        self.metadata = new_obj.metadata
        self.spec = new_obj.spec
        self.status = new_obj.status
        self.user = new_obj.user

    @abstractmethod
    def export(self, filename: str | None = None) -> str:
        """
        Abstract export method.
        """

    def to_dict(self) -> dict:
        """
        Override default to_dict method to add the possibility to exclude
        some attributes. This requires to set a list of _obj_attr
        attributes in the subclass.

        Returns
        -------
        dict
            A dictionary containing the attributes of the entity instance.
        """
        return {k: v for k, v in super().to_dict().items() if k in self._obj_attr}

    def __repr__(self) -> str:
        """
        Return string representation of the entity object.

        Returns
        -------
        str
            A string representing the entity instance.
        """
        return str(self.to_dict())
