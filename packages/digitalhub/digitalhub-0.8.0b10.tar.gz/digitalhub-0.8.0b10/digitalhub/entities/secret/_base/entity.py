from __future__ import annotations

import typing

from digitalhub.entities._base.api_utils import get_data_api, set_data_api
from digitalhub.entities._base.versioned.entity import VersionedEntity
from digitalhub.entities.utils.entity_types import EntityTypes

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata
    from digitalhub.entities.secret._base.spec import SecretSpec
    from digitalhub.entities.secret._base.status import SecretStatus


class Secret(VersionedEntity):
    """
    A class representing a secret.
    """

    ENTITY_TYPE = EntityTypes.SECRET.value

    def __init__(
        self,
        project: str,
        name: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: SecretSpec,
        status: SecretStatus,
        user: str | None = None,
    ) -> None:
        super().__init__(project, name, uuid, kind, metadata, spec, status, user)
        self.spec: SecretSpec
        self.status: SecretStatus

    ##############################
    #  Secret methods
    ##############################

    def set_secret_value(self, value: str) -> None:
        """
        Update the secret value with a new one.

        Parameters
        ----------
        value : str
            Value of the secret.

        Returns
        -------
        None
        """
        if self._context().local:
            raise NotImplementedError("set_secret() is not implemented for local projects.")

        obj = {self.name: value}
        set_data_api(self.project, self.ENTITY_TYPE, obj)

    def read_secret_value(self) -> dict:
        """
        Read the secret value from backend.

        Returns
        -------
        str
            Value of the secret.
        """
        if self._context().local:
            raise NotImplementedError("read_secret() is not implemented for local projects.")

        params = {"keys": self.name}
        data = get_data_api(self.project, self.ENTITY_TYPE, params=params)
        return data[self.name]
