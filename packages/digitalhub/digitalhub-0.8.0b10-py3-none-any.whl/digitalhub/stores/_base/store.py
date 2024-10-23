from __future__ import annotations

from abc import ABCMeta, abstractmethod
from pathlib import Path
from tempfile import mkdtemp
from typing import Literal

from pydantic import BaseModel

from digitalhub.utils.exceptions import StoreError
from digitalhub.utils.uri_utils import map_uri_scheme


class Store(metaclass=ABCMeta):
    """
    Store abstract class.
    """

    def __init__(self, name: str, store_type: str) -> None:
        """
        Constructor.

        Parameters
        ----------
        name : str
            Store name.
        store_type : str
            Store type. Used to choose the right store implementation.

        Returns
        -------
        None
        """
        self.name = name
        self.type = store_type

    ##############################
    # IO methods
    ##############################

    @abstractmethod
    def download(
        self,
        root: str,
        dst: Path,
        src: list[str],
        overwrite: bool = False,
    ) -> str:
        """
        Method to download artifact from storage.
        """

    @abstractmethod
    def upload(self, src: str | list[str], dst: str | None = None) -> list[tuple[str, str]]:
        """
        Method to upload artifact to storage.
        """

    @abstractmethod
    def get_file_info(self, paths: list[str]) -> list[dict]:
        """
        Method to get file metadata.
        """

    ##############################
    # Helpers methods
    ##############################

    def _check_local_src(self, src: str) -> None:
        """
        Check if the source path is local.

        Parameters
        ----------
        src : str
            The source path.

        Returns
        -------
        None

        Raises
        ------
        StoreError
            If the source is not a local path.
        """
        if map_uri_scheme(src) != "local":
            raise StoreError(f"Source '{src}' is not a local path.")

    def _check_local_dst(self, dst: str) -> None:
        """
        Check if the destination path is local.

        Parameters
        ----------
        dst : str
            The destination path.

        Returns
        -------
        None

        Raises
        ------
        StoreError
            If the destination is not a local path.
        """
        if map_uri_scheme(dst) != "local":
            raise StoreError(f"Destination '{dst}' is not a local path.")

    def _check_overwrite(self, dst: Path, overwrite: bool) -> None:
        """
        Check if destination path exists for overwrite.

        Parameters
        ----------
        dst : Path
            Destination path as filename.
        overwrite : bool
            Specify if overwrite an existing file.

        Returns
        -------
        None

        Raises
        ------
        StoreError
            If destination path exists and overwrite is False.
        """
        if dst.exists() and not overwrite:
            raise StoreError(f"Destination {str(dst)} already exists.")

    @staticmethod
    def _build_path(path: str | Path) -> None:
        """
        Get path from store path and path.

        Parameters
        ----------
        path : str
            The path to build.

        Returns
        -------
        None
        """
        if not isinstance(path, Path):
            path = Path(path)
        if path.suffix != "":
            path = path.parent
        path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _build_temp() -> Path:
        """
        Build a temporary path.

        Returns
        -------
        Path
            Temporary path.
        """
        tmpdir = mkdtemp()
        return Path(tmpdir)


class StoreConfig(BaseModel):
    """
    Store configuration base class.
    """


class StoreParameters(BaseModel):
    """
    Store configuration class.
    """

    name: str
    """Store id."""

    type: Literal["local", "s3", "remote", "sql"]
    """Store type to instantiate."""

    config: StoreConfig = None
    """Configuration for the store."""

    is_default: bool = False
    """Flag to determine if the store is the default one."""
