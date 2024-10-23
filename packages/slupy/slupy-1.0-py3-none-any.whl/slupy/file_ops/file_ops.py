from typing import List, Optional
import ntpath
import os
import shutil


def get_extension_from_filepath(filepath: str, /) -> str:
    """Returns the extension of the given filepath"""
    return os.path.splitext(filepath)[-1][1:]


def get_basename_from_filepath(filepath: str, /) -> str:
    """Returns base-name of the file/folder from the given `filepath` (along with the extension, if any)"""
    head, tail = ntpath.split(p=filepath)
    return tail or ntpath.basename(head)


def get_absolute_filepath(filepath: str, /) -> str:
    """Returns absolute filepath of the file/folder from the given `filepath` (along with the extension, if any)"""
    absolute_filepath = os.path.realpath(path=filepath)
    return absolute_filepath


def filter_filepaths_by_extensions(
        *,
        filepaths: List[str],
        extensions: List[str],
    ) -> List[str]:
    """
    Filters given filepaths by the desired extensions.

    >>> filter_filepaths_by_extensions(
        filepaths=['one.js', 'two.py', 'three.css', 'four.go', 'five.html', 'six.py', 'seven.js'],
        extensions=['css', 'js'],
    )
    """
    extensions = list(
        map(lambda extension: extension.strip().lower(), extensions)
    )
    filepaths_needed = list(
        filter(lambda filepath: get_extension_from_filepath(filepath).strip().lower() in extensions, filepaths)
    )
    return filepaths_needed


def get_unique_extensions(*, filepaths: List[str]) -> List[str]:
    """Returns all unique extensions available in the list of filepaths given"""
    all_extensions = list(map(get_extension_from_filepath, filepaths))
    unique_extensions = sorted(list(set(all_extensions)))
    return unique_extensions


def _get_filepaths_at_first_level(src_dir: str) -> List[str]:
    folders_and_files_in_directory = os.listdir(src_dir)
    folders_and_files_in_directory = list(
        map(lambda folder_or_file: os.path.join(src_dir, folder_or_file), folders_and_files_in_directory)
    )
    files_in_directory = list(
        filter(lambda folder_or_file: os.path.isfile(folder_or_file), folders_and_files_in_directory)
    )
    return files_in_directory


def _get_filepaths_at_all_levels(src_dir: str) -> List[str]:
    filepaths = []
    for path, _, filenames in os.walk(src_dir):
        for filename in filenames:
            filepath = os.path.join(path, filename)
            filepaths.append(filepath)
    return filepaths


def get_filepaths(
        *,
        src_dir: str,
        depth: str,
        extensions: Optional[List[str]] = None,
    ) -> List[str]:
    """
    Gets list of all filepaths (of files) from source directory.
    
    Parameters:
        - src_dir (str): Filepath to the source directory. Can be absolute or relative.
        - depth (str): Options: ['all_levels', 'first_level'].
        Set to 'all_levels' if you want to get filepaths from all sub-directories (if any) in the given source directory.
        Set to 'first_level' if you want to get filepaths only from the first directory given.
        - extensions (list): List of extensions to filter the filepaths by (optional).
    
    >>> get_filepaths(
            src_dir="SOME_SOURCE_DIR",
            depth='all_levels',
            extensions=['csv', 'xlsx'],
        )
    """
    depth_options = ['all_levels', 'first_level']
    if depth not in depth_options:
        raise ValueError(f"Expected `depth` to be in {depth_options}, but got '{depth}'")
    
    if depth == 'all_levels':
        filepaths = _get_filepaths_at_all_levels(src_dir=src_dir)
    elif depth == 'first_level':
        filepaths = _get_filepaths_at_first_level(src_dir=src_dir)
    if extensions is not None:
        filepaths = filter_filepaths_by_extensions(filepaths=filepaths, extensions=extensions)
    return filepaths


def create_archive_file(
        *,
        src_dir: str,
        archive_format: str,
    ) -> None:
    """
    Creates archive file of the given source directory.
    Options for `archive_format` are: ['zip', 'tar', 'gztar', 'bztar', 'xztar'].
    """
    absolute_path_to_src_dir = get_absolute_filepath(src_dir)
    basename_of_src_dir = get_basename_from_filepath(src_dir)
    shutil.make_archive(
        base_name=basename_of_src_dir,
        format=archive_format,
        root_dir=absolute_path_to_src_dir,
    )

