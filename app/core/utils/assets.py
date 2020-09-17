"""Utility functions for handling assets"""
import logging
import os
import shutil
from csv import DictReader
from datetime import datetime
from typing import Iterator, Dict, Any, List, Optional

ASSET_FOLDER_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'assets')


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


def read_csv_file(file_path: str, headers: Optional[List[str]] = None) -> Iterator[Dict[str, Any]]:
    """Reads the Downloaded file and returns the rows in the file as an iterator"""
    with open(file_path, 'r') as csv_file:
        csv_dict_reader = DictReader(csv_file, fieldnames=headers)
        yield from csv_dict_reader


def delete_parent_folder(file_path: str):
    """Deletes the parent folder when given a file path"""
    parent_folder = os.path.dirname(file_path)

    try:
        shutil.rmtree(parent_folder)
    except OSError as exp:
        logging.error(exp)
