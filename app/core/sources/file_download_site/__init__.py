"""Module containing configurations for the export site data source"""
from typing import Iterator, Dict, Any, List, Optional

from ..base import BaseSource
from ...utils.assets import read_file, delete_parent_folder


class FileDownloadSiteSource(BaseSource):
    headers: Optional[List[str]] = None

    def _download_file(self, *args, **kwargs) -> str:
        """Downloads the file from the export site and returns the path to it"""
        raise NotImplementedError('_download_csv method should be implemented')

    def _query_data_source(self, *args, **kwargs) -> Iterator[Dict[str, Any]]:
        """Queries a given source and returns an iterator with data records"""
        file_path = self._download_file(*args, **kwargs)

        if file_path is None:
            yield from []
        else:
            yield from read_file(file_path=file_path, headers=self.headers)
            delete_parent_folder(file_path)


