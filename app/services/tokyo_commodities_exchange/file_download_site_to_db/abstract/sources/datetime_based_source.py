"""Module containing the class file for the download site source from Tokyo Commodity Exchange
that bases on start date"""
import logging
import os
from datetime import date, datetime

import selenium
from selenium.webdriver.support.select import Select

from app.core.sources.file_download_site.datetime_based import DatetimeBasedFileDownloadSiteSource
from app.core.utils.assets import get_csv_download_location
from app.core.utils.selenium import get_web_driver, WebDriverOptions, visit_website, get_html_element_by_xpath, \
    wait_for_download_to_complete


class TokyoCEDatetimeBasedFileDownloadSiteSource(DatetimeBasedFileDownloadSiteSource):
    """Class with configurations for any resource to be downloaded from the Tokyo Commodity Exchange export site"""
    start_datetime_select_input_xpath: str
    download_button_xpath: str
    base_uri: str = os.getenv('TOKYO_COMMODITIES_FILE_DOWNLOAD_URI')
    file_prefix: str = ''
    timeout: int = 10

    def _download_csv(self, start_datetime: datetime, end_datetime: datetime) -> str:
        """
        Downloads csv from the site by feeding in the start datetime and downloading the csv
        """
        downloads_folder = get_csv_download_location(dataset_name=self.name.replace(' ', '_'))
        expected_file_name = f'{self.file_prefix}{start_datetime.strftime("%Y%m%d_%Y%m%d_%H%M")}.csv'
        expected_file_path = os.path.join(downloads_folder, expected_file_name)

        tokyo_c_e_driver = get_web_driver(
            WebDriverOptions(downloads_folder_location=downloads_folder))

        try:
            visit_website(driver=tokyo_c_e_driver, website_url=self.base_uri)

            start_datetime_select_input = Select(get_html_element_by_xpath(driver=tokyo_c_e_driver,
                                                                           xpath=self.start_datetime_select_input_xpath))
            download_button = get_html_element_by_xpath(driver=tokyo_c_e_driver,
                                                        xpath=self.download_button_xpath)

            start_datetime_select_input.select_by_value(expected_file_name)

            download_button.click()

            wait_for_download_to_complete(expected_file_path=expected_file_path, timeout=self.timeout)
        except selenium.common.exceptions.NoSuchElementException as exp:
            logging.error(exp)
            expected_file_path = None
        finally:
            tokyo_c_e_driver.close()

        return expected_file_path
