"""Module containing the class file for the download site source from Tokyo Commodity Exchange
that bases on start date"""
import logging
import os
from typing import Optional

import selenium
from selenium.webdriver.support.select import Select

from judah.sources.export_site.index_based import IndexBasedExportSiteSource
from judah.utils.selenium import get_html_element_by_xpath, \
    wait_for_download_to_complete


class TokyoCEIndexBasedExportSiteSource(IndexBasedExportSiteSource):
    """Class with configurations for any resource to be downloaded from the Tokyo Commodity Exchange export site"""
    file_select_input_xpath: str
    download_button_xpath: str
    base_uri: str = os.getenv('TOKYO_COMMODITIES_FILE_DOWNLOAD_URI')
    timeout: int = 10
    number_of_indices: Optional[int] = None

    def _download_file(self, current_option_index: int, **kwargs) -> str:
        """
        Downloads csv from the site and downloading the csv
        """
        try:
            start_datetime_select_input = Select(get_html_element_by_xpath(driver=self.chrome,
                                                                           xpath=self.file_select_input_xpath))
            download_button = get_html_element_by_xpath(driver=self.chrome,
                                                        xpath=self.download_button_xpath)
            options = start_datetime_select_input.options

            if self.number_of_indices is None:
                self.number_of_indices = len(options)

            current_option = options[current_option_index]
            expected_file_name = current_option.get_attribute('value')
            current_option.click()
            download_button.click()

            expected_file_path = os.path.join(self.download_folder_path, expected_file_name)
            wait_for_download_to_complete(expected_file_path=expected_file_path, timeout=self.timeout)
        except selenium.common.exceptions.NoSuchElementException as exp:
            logging.error(exp)
            expected_file_path = None

        return expected_file_path
