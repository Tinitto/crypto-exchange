import asyncio
from typing import Iterator, Dict, Any, Optional

from app.core.sources.base import BaseSource
from app.core.utils.assets import read_file, delete_parent_folder, FileType, FileOptions


class IndexBasedFileDownloadSiteSource(BaseSource):
    file_type: FileType = FileType.CSV
    file_options: FileOptions = FileOptions()
    number_of_indices: Optional[int] = None
    seconds_between_downloads: int = 3

    def _download_file(self, current_option_index: int) -> str:
        """Downloads the CSV from the export site and returns the path to it"""
        raise NotImplementedError('_download_file method should be implemented')

    def _query_data_source(self, **kwargs) -> Iterator[Dict[str, Any]]:
        """Queries a given source and returns an iterator with data records"""
        current_option_index = 0

        while True:
            file_path = self._download_file(current_option_index=current_option_index)

            if file_path is None:
                yield from []
            else:
                yield from read_file(
                    file_path=file_path, file_type=self.file_type, options=self.file_options)
                delete_parent_folder(file_path)

            current_option_index += 1

            if self.number_of_indices is None:
                raise Exception('self.number_of_indices should be set in the _download_file method')

            if current_option_index >= self.number_of_indices:
                self.number_of_indices = None
                break

            # to avoid Denial of Service (DOS) on the server
            asyncio.sleep(self.seconds_between_downloads)
