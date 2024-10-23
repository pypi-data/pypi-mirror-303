from __future__ import annotations

import typing
from pathlib import Path

from digitalhub.entities._base.api_utils import files_info_get_api, files_info_put_api
from digitalhub.entities._base.versioned.entity import VersionedEntity
from digitalhub.stores.api import get_store

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata
    from digitalhub.entities._base.material.spec import MaterialSpec
    from digitalhub.entities._base.material.status import MaterialStatus


class MaterialEntity(VersionedEntity):
    """
    A class representing an entity that can be materialized
    as file(s).
    """

    def __init__(
        self,
        project: str,
        name: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: MaterialSpec,
        status: MaterialStatus,
        user: str | None = None,
    ) -> None:
        super().__init__(project, name, uuid, kind, metadata, spec, status, user)
        self.spec: MaterialSpec
        self.status: MaterialStatus

    def save(self, update: bool = False) -> MaterialEntity:
        """
        Save entity into backend.

        Parameters
        ----------
        update : bool
            Flag to indicate update.

        Returns
        -------
        MaterialEntity
            Entity saved.
        """
        obj = self.to_dict()

        files = None
        if self.status.files is not None and len(self.status.files) > 5 and not self._context().local:
            files = obj["status"].pop("files")

        if not update:
            new_obj: MaterialEntity = self._save(obj)
        else:
            new_obj: MaterialEntity = self._update(obj)

        # Handle files info
        if files is not None:
            files_info_put_api(self.project, self.ENTITY_TYPE, self.id, files)
            self.status.add_files_info(files)

        return new_obj

    ##############################
    # I/O Methods
    ##############################

    def as_file(self) -> list[str]:
        """
        Get object as file(s). It downloads the object from storage in
        a temporary folder and returns the list of downloaded files paths.

        Returns
        -------
        list[str]
            List of file paths.
        """
        store = get_store(self.spec.path)
        paths = self.status.get_file_paths()
        dst = store._build_temp()
        return store.download(self.spec.path, dst=dst, src=paths)

    def download(
        self,
        destination: str | None = None,
        overwrite: bool = False,
    ) -> str:
        """
        This function downloads one or more file from storage on local
        machine.
        It looks inside the object's status for the file(s) path under
        files attribute. If it does not find it, it will try to download
        what it can from spec.path.
        The files are downloaded into a destination folder. If the destination
        is not specified, it will set by default under the context path
        as '<ctx-root>/<entity_type>', e.g. './dataitem'.
        The overwrite flag allows to overwrite existing file(s) in the
        destination folder.

        Parameters
        ----------
        destination : str
            Destination path as filename or directory.
        overwrite : bool
            Specify if overwrite existing file(s). If file(s) already
            exist and overwrite is False, it will raise an error.

        Returns
        -------
        str
            Downloaded path.

        Examples
        --------
        Download a single file:

        >>> entity.status.files[0]
        {
            "path ": "data.csv",
            "name ": "data.csv",
            "content_type ": "text/csv;charset=utf-8 "
        }
        >>> path = entity.download()
        >>> print(path)
        dataitem/data.csv
        """
        store = get_store(self.spec.path)
        paths = self.status.get_file_paths()

        if destination is None:
            dst = self._context().root / self.ENTITY_TYPE
        else:
            dst = Path(destination)

        return store.download(self.spec.path, dst=dst, src=paths, overwrite=overwrite)

    def upload(self, source: str | list[str]) -> None:
        """
        Upload object from given local path to spec path destination.
        Source must be a local path. If the path is a folder, destination
        path (object's spec path) must be a folder or a partition ending
        with '/' (s3).

        Parameters
        ----------
        source : str | list[str]
            Local filepath, directory or list of filepaths.

        Returns
        -------
        None

        Examples
        --------
        Upload a single file:

        >>> entity.spec.path = 's3://bucket/data.csv'
        >>> entity.upload('./data.csv')

        Upload a folder:
        >>> entity.spec.path = 's3://bucket/data/'
        >>> entity.upload('./data')
        """
        # Get store and upload object
        store = get_store(self.spec.path)
        paths = store.upload(source, self.spec.path)

        # Update files info
        files_info = store.get_file_info(paths)
        self._update_files_info(files_info)

    ##############################
    #  Private Helpers
    ##############################

    def _update_files_info(self, files_info: list[dict] | None = None) -> None:
        """
        Update files info.

        Parameters
        ----------
        files_info : list[dict] | None
            Files info.

        Returns
        -------
        None
        """
        if files_info is None:
            return
        self.refresh()
        self.status.add_files_info(files_info)
        self.save(update=True)

    def _get_files_info(self) -> None:
        """
        Get files info from backend.

        Returns
        -------
        None
        """
        if not self._context().local and not self.status.files:
            files = files_info_get_api(
                project=self.project,
                entity_type=self.ENTITY_TYPE,
                entity_id=self.id,
            )
            self.status.add_files_info(files)
