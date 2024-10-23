from __future__ import annotations

from digitalhub.entities._base.entity.status import Status


class MaterialStatus(Status):
    """
    Material Status class.
    """

    def __init__(
        self,
        state: str,
        message: str | None = None,
        files: list[dict] | None = None,
    ) -> None:
        super().__init__(state, message)
        if files is None:
            files = []
        self.files = files

    def add_files_info(self, files: list[dict]) -> None:
        """
        Add a file to the status.

        Parameters
        ----------
        files : list[dict]
            Files to add.

        Returns
        -------
        None
        """
        path_list = self.get_file_paths()
        for f in files:
            if f.get("path") not in path_list:
                self.files.append(f)

    def get_file_paths(self) -> list[str]:
        """
        Get the paths of the files in the status.

        Returns
        -------
        list[str]
            Paths of the files in the status.
        """
        return [f.get("path") for f in self.files]
