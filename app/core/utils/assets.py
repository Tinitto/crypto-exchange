"""Utility functions for handling assets"""
import logging
import os
import shutil
import xlrd
from csv import DictReader
from datetime import datetime
from typing import Iterator, Dict, Any, List, Optional
from enum import Enum

from xml_stream import read_xml_file

ASSET_FOLDER_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'assets')


class FileType(Enum):
    CSV = 'csv'
    XLS = 'xls'
    XML = 'xml'


def get_asset_path(asset_name: str):
    """Returns the path of a given asset"""
    return os.path.join(ASSET_FOLDER_PATH, asset_name)


def get_timestamped_folder_name(
        prefix: str = '', suffix: str = '', date_format: str = '%m_%d_%Y_%H_%M_%S'):
    """Returns a folder name of format name"""
    now = datetime.utcnow()
    return f"{prefix}{now.strftime(date_format)}{suffix}"


def get_timestamped_folder(root_path: str, prefix: str = '', suffix: str = '', ):
    """Returns a folder path with the given folder created if it did not exist"""
    timestamped_folder_name = get_timestamped_folder_name(prefix=prefix, suffix=suffix)
    timestamped_folder = os.path.join(root_path, timestamped_folder_name)

    if not os.path.exists(timestamped_folder):
        os.makedirs(timestamped_folder)

    return timestamped_folder


def get_csv_download_location(dataset_name: str = ''):
    """Returns the path to the csv folder asset"""
    csv_folder_path = get_asset_path(asset_name='csv')
    return get_timestamped_folder(root_path=csv_folder_path, prefix=dataset_name)


def read_csv_file(file_path: str, headers: Optional[List[str]] = None, **kwargs) -> Iterator[Dict[str, Any]]:
    """Reads the CSV file and returns the rows in the file as an iterator"""
    with open(file_path, 'r') as csv_file:
        csv_dict_reader = DictReader(csv_file, fieldnames=headers)
        yield from csv_dict_reader


def read_xls_file(file_path: str,
                  headers: Optional[List[str]] = None,
                  sheet_name: Optional[str] = None,
                  sheet_index: Optional[int] = 1, **kwargs) -> Iterator[Dict[str, Any]]:
    """Reads the XLS file and returns the rows in the file as an iterator"""
    with xlrd.open_workbook(file_path, on_demand=True) as xls_file:
        if isinstance(sheet_name, str):
            sheet = xls_file.sheet_by_name(sheet_name)
        elif isinstance(sheet_index, int):
            sheet = xls_file.sheet_by_index(sheet_index)
        else:
            raise ValueError('A sheet_name or sheet_index should be provided')

        for row in sheet.get_rows():
            row_values = sheet.row_values(rowx=row)

            # should run once on the first row
            if headers is None:
                headers = row_values
                continue

            yield dict(zip(headers, row_values))


def read_file(file_path: str,
              headers: Optional[List[str]] = None,
              file_type: FileType = FileType.CSV,
              xml_records_tag: Optional[str] = None, **kwargs) -> Iterator[Dict[str, Any]]:
    """Reads the Downloaded file and returns the rows in the file as an iterator"""
    with open(file_path, 'r') as file:
        if file_type == FileType.CSV:
            yield from read_csv_file(file_path=file_path, headers=headers)

        elif file_type == FileType.XLS:
            yield from read_xls_file(file_path=file_path, headers=headers, **kwargs)

        elif file_type == FileType.XML:
            yield from read_xml_file(
                file_path=file_path, to_dict=True, records_tag=xml_records_tag, **kwargs)

        else:
            raise ValueError('The given file_type cannot be handled by program')


def delete_parent_folder(file_path: str):
    """Deletes the parent folder when given a file path"""
    parent_folder = os.path.dirname(file_path)

    try:
        shutil.rmtree(parent_folder)
    except OSError as exp:
        logging.error(exp)
