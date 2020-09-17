from datetime import datetime
from typing import Optional, List, Iterator, Dict, Any

from app.core.sources.base.datetime_based import DatetimeBasedBaseSource
from app.core.utils.assets import read_csv_file, delete_parent_folder


class DatetimeBasedFileDownloadSiteSource(DatetimeBasedBaseSource):
    headers: Optional[List[str]] = None

    def _download_csv(self,  start_datetime: datetime, end_datetime: datetime) -> str:
        """Downloads the CSV from the export site and returns the path to it"""
        raise NotImplementedError('_download_csv method should be implemented')

    def _query_data_source(self,  start_datetime: datetime, end_datetime: datetime) -> Iterator[Dict[str, Any]]:
        """Queries a given source and returns an iterator with data records"""
        csv_file_path = self._download_csv( start_datetime=start_datetime, end_datetime=end_datetime)

        if csv_file_path is None:
            yield from []
        else:
            yield from read_csv_file(file_path=csv_file_path, headers=self.headers)
            delete_parent_folder(csv_file_path)