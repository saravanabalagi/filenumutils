import os
import time
import shutil
import pytest

from filenumutils.filenum_functions import get_last_folder_number, get_last_file_number, get_next_file, get_next_folder

test_folder_path = None


def setup_function():
    global test_folder_path
    time_hash = str(time.time())[-6:]
    test_folder_path = f'_test_folder_{time_hash}'
    os.makedirs(test_folder_path)


def teardown_function():
    global test_folder_path
    shutil.rmtree(test_folder_path)


def _create_folders(parent_folder_path: str, folder_names: list) -> None:
    for folder in folder_names:
        os.makedirs(os.path.join(parent_folder_path, folder))


def _remove_folders(parent_folder_path: str, folder_names: list) -> None:
    for folder in folder_names:
        os.rmdir(os.path.join(parent_folder_path, folder))


def _create_files(parent_folder_path: str, filenames: list) -> None:
    for file in filenames:
        with open(os.path.join(parent_folder_path, file), 'w'):
            pass


def _remove_files(parent_folder_path: str, filenames: list) -> None:
    for file in filenames:
        os.remove(os.path.join(parent_folder_path, file))


folders_list = [
    [],
    ['test_01', 'tset_02'],
    ['test_001', 'test_02', 'test_2', 'test_2_4']
]

expected_numbers = [-1, 1, 2]
expected_names = ['test_0', 'test_02', 'test_03']
prefix_list = ['test_' for _ in folders_list]


@pytest.mark.parametrize("folders, prefix, expected_number", zip(folders_list, prefix_list, expected_numbers))
def test_get_last_folder_number(folders, prefix, expected_number):
    global test_folder_path
    _create_folders(test_folder_path, folders)
    output_number = get_last_folder_number(test_folder_path, prefix=prefix)
    _remove_folders(test_folder_path, folders)
    assert (output_number == expected_number)


@pytest.mark.parametrize("files, prefix, expected_number", zip(folders_list, prefix_list, expected_numbers))
def test_get_last_file_number(files, prefix, expected_number):
    global test_folder_path
    _create_files(test_folder_path, files)
    output_number = get_last_file_number(test_folder_path, prefix=prefix)
    _remove_files(test_folder_path, files)
    assert (output_number == expected_number)


@pytest.mark.parametrize("folders, prefix, expected_folder_name", zip(folders_list, prefix_list, expected_names))
def test_get_next_folder(folders, prefix, expected_folder_name):
    global test_folder_path
    _create_folders(test_folder_path, folders)
    output_folder_string = get_next_folder(test_folder_path, prefix=prefix)
    _remove_folders(test_folder_path, folders)
    assert (output_folder_string == expected_folder_name)


@pytest.mark.parametrize("files, prefix, expected_filename", zip(folders_list, prefix_list, expected_names))
def test_get_next_file(files, prefix, expected_filename):
    global test_folder_path
    _create_files(test_folder_path, files)
    output_folder_string = get_next_file(test_folder_path, prefix=prefix)
    _remove_files(test_folder_path, files)
    assert (output_folder_string == expected_filename)
