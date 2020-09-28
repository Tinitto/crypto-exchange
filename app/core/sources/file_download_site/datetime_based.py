from datetime import datetime
from typing import Optional, List, Iterator, Dict, Any

from app.core.sources.base.datetime_based import DatetimeBasedBaseSource
from app.core.utils.assets import read_file, delete_parent_folder, FileType, FileOptions


class DatetimeBasedFileDownloadSiteSource(DatetimeBasedBaseSource):
    file_type: FileType = FileType.CSV
    file_options: FileOptions = FileOptions()

    def _download_file(self, start_datetime: datetime, end_datetime: datetime) -> str:
        """Downloads the CSV from the export site and returns the path to it"""
        raise NotImplementedError('_download_file method should be implemented')

    def _query_data_source(self,  start_datetime: datetime, end_datetime: datetime) -> Iterator[Dict[str, Any]]:
        """Queries a given source and returns an iterator with data records"""
        file_path = self._download_file(start_datetime=start_datetime, end_datetime=end_datetime)

        if file_path is None:
            yield from []
        else:
            yield from read_file(
                file_path=file_path, file_type=self.file_type, options=self.file_options)
            delete_parent_folder(file_path)
