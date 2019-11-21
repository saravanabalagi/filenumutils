import os
from filenumutils.helper_functions import _get_pattern, _get_str_number_list, _get_number_list


def get_last_file_number(path: str = os.getcwd(), prefix: str = '', extension: str = '', folder: bool = False) -> int:
    root, folders, files = next(os.walk(path))
    pattern = _get_pattern(prefix, extension)
    number_list = _get_number_list(pattern, folders if folder else files)
    return max(number_list) if len(number_list) > 0 else -1


def get_last_folder_number(path: str = os.getcwd(), prefix: str = '', suffix: str = '') -> int:
    return get_last_file_number(path=path, prefix=prefix, extension=suffix, folder=True)


def get_next_file(path: str = os.getcwd(), prefix: str = '', extension: str = '', folder: bool = False) -> str:
    root, folders, files = next(os.walk(path))
    pattern = _get_pattern(prefix, extension)

    # find last file number but also get str number list
    # hence get_last_file_number is not used
    str_number_list = _get_str_number_list(pattern, folders if folder else files)
    number_list = [int(number) for number in str_number_list]
    max_number = max(number_list) if len(number_list) > 0 else -1

    # find last file number length for padding zeros
    strings_of_max_number = [len(str_number) for str_number in str_number_list if int(str_number) == max_number]
    number_length = max([0] + strings_of_max_number)

    return ('{}{:0' + str(number_length) + 'd}{}').format(prefix, max_number+1, extension)


def get_next_folder(path: str = os.getcwd(), prefix: str = '', suffix: str = '') -> str:
    return get_next_file(path, prefix, suffix, folder=True)
