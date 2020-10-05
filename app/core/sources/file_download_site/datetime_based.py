from datetime import datetime
from typing import Iterator, Dict, Any, Optional

from selenium import webdriver

from app.core.sources.base.datetime_based import DatetimeBasedBaseSource
from app.core.utils.assets import read_file, delete_parent_folder, FileType, FileOptions, get_csv_download_location, \
    get_xml_download_location, get_asset_path
from app.core.utils.selenium import get_web_driver, WebDriverOptions, visit_website


class DatetimeBasedFileDownloadSiteSource(DatetimeBasedBaseSource):
    file_type: FileType = FileType.CSV
    file_options: FileOptions = FileOptions()

    chrome: Optional[webdriver.Chrome] = None
    download_folder_path: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True

    def _initialize_chrome(self):
        """Initializes Chrome in case it is not yet initialized"""
        if isinstance(self.chrome, webdriver.Chrome):
            return

        if self.file_type == FileType.CSV:
            self.download_folder_path = get_csv_download_location(dataset_name=self.name.replace(' ', '_'))
        elif self.file_type == FileType.XML:
            self.download_folder_path = get_xml_download_location(dataset_name=self.name.replace(' ', '_'))
        else:
            self.download_folder_path = get_asset_path()

        self.chrome = get_web_driver(
            WebDriverOptions(downloads_folder_location=self.download_folder_path))

        visit_website(driver=self.chrome, website_url=self.base_uri)

    def _download_file(self, start_datetime: datetime, end_datetime: datetime) -> str:
        """Downloads the CSV from the export site and returns the path to it"""
        raise NotImplementedError('_download_file method should be implemented')

    def _query_data_source(self,  start_datetime: datetime, end_datetime: datetime) -> Iterator[Dict[str, Any]]:
        """Queries a given source and returns an iterator with data records"""
        self._initialize_chrome()
        file_path = self._download_file(start_datetime=start_datetime, end_datetime=end_datetime)

        if file_path is None:
            yield from []
        else:
            yield from read_file(
                file_path=file_path, file_type=self.file_type, options=self.file_options)
            delete_parent_folder(file_path)

    def __del__(self):
        """Clean up"""
        if isinstance(self.chrome, webdriver.Chrome):
            self.chrome.quit()
