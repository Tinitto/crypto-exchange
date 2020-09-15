"""Module containing configurations for the export site data source"""

from datetime import date
from typing import Iterator, Dict, Any

from ..base import BaseSource
from ...utils.assets import read_csv_file, delete_parent_folder


class FileDownloadSiteSource(BaseSource):
    default_file_name: str = 'export.csv'

    def _download_csv(self, start_date: date, end_date: date) -> str:
        """Downloads the CSV from the export site and returns the path to it"""
        raise NotImplementedError('_download_csv method should be implemented')

    def _query_data_source(self, start_date: date, end_date: date) -> Iterator[Dict[str, Any]]:
        """Queries a given start and end date and returns an iterator with data records"""
        csv_file_path = self._download_csv(start_date=start_date, end_date=end_date)
        yield from read_csv_file(file_path=csv_file_path)
        delete_parent_folder(csv_file_path)
