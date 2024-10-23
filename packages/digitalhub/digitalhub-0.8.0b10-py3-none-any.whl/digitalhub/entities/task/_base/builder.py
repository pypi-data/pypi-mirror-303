from __future__ import annotations

import typing

from digitalhub.entities._base.runtime_entity.builder import RuntimeEntityBuilder
from digitalhub.entities._base.unversioned.builder import UnversionedBuilder
from digitalhub.entities.utils.entity_types import EntityTypes

if typing.TYPE_CHECKING:
    from digitalhub.entities.task._base.entity import Task


class TaskBuilder(UnversionedBuilder, RuntimeEntityBuilder):
    """
    Task builder.
    """

    ENTITY_TYPE = EntityTypes.TASK.value

    def build(
        self,
        project: str,
        kind: str,
        uuid: str | None = None,
        labels: list[str] | None = None,
        function: str | None = None,
        **kwargs,
    ) -> Task:
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
        function : str
            Name of the executable associated with the task.
        **kwargs : dict
            Spec keyword arguments.

        Returns
        -------
        Task
            Object instance.
        """
        uuid = self.build_uuid(uuid)
        metadata = self.build_metadata(
            project=project,
            name=uuid,
            labels=labels,
        )
        spec = self.build_spec(
            function=function,
            **kwargs,
        )
        status = self.build_status()
        return self.build_entity(
            project=project,
            uuid=uuid,
            kind=kind,
            metadata=metadata,
            spec=spec,
            status=status,
        )
