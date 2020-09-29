"""Module containing configurations for the export site data source"""
from typing import Iterator, Dict, Any, List, Optional

from ..base import BaseSource
from ...utils.assets import read_file, delete_parent_folder, FileType, FileOptions


class FileDownloadSiteSource(BaseSource):
    file_type: FileType = FileType.CSV
    file_options: FileOptions = FileOptions()

    def _download_file(self, *args, **kwargs) -> str:
        """Downloads the CSV from the export site and returns the path to it"""
        raise NotImplementedError('_download_file method should be implemented')

    def _query_data_source(self, *args, **kwargs) -> Iterator[Dict[str, Any]]:
        """Queries a given start and end date and returns an iterator with data records"""
        file_path = self._download_file(*args, **kwargs)

        if file_path is None:
            yield from []
        else:
            yield from read_file(
                file_path=file_path, file_type=self.file_type, options=self.file_options)
            delete_parent_folder(file_path)
