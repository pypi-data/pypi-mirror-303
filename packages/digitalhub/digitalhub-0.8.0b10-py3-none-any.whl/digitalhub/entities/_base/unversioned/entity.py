from __future__ import annotations

import typing

from digitalhub.entities._base.context.entity import ContextEntity
from digitalhub.utils.io_utils import write_yaml

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata
    from digitalhub.entities._base.entity.spec import Spec
    from digitalhub.entities._base.entity.status import Status


class UnversionedEntity(ContextEntity):
    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: Spec,
        status: Status,
        user: str | None = None,
    ) -> None:
        super().__init__(project, kind, metadata, spec, status, user)
        self.id = uuid
        self.key = f"store://{project}/{self.ENTITY_TYPE}/{kind}/{uuid}"
        self._obj_attr.extend(["id"])

    def export(self, filename: str | None = None) -> str:
        """
        Export object as a YAML file.

        Parameters
        ----------
        filename : str
            Name of the export YAML file. If not specified, the default value is used.

        Returns
        -------
        str
            Exported file.
        """
        obj = self.to_dict()
        if filename is None:
            filename = f"{self.ENTITY_TYPE}-{self.id}.yml"
        pth = self._context().root / filename
        write_yaml(pth, obj)
        return str(pth)
