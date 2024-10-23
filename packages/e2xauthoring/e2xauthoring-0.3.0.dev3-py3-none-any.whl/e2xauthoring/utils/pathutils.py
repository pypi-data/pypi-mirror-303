import os


def is_parent_path(parent_path: str, child_path: str) -> bool:
    """Check if a path is a parent of another path

    Args:
        parent_path (str): The potential parent path
        child_path (str): The path to test
    Returns:
        bool: True if child_path is a sub directory of parent_path
    """
    parent_path = os.path.abspath(parent_path)
    child_path = os.path.abspath(child_path)
    return os.path.commonpath([parent_path]) == os.path.commonpath(
        [parent_path, child_path]
    )


def list_files(path: str) -> dict:
    """List all files in all subdirectories recursively

    Args:
        path (str): The path to list files from
    Returns:
        dict: A dictionary of files and their last modified time
    """
    files = [
        os.path.relpath(os.path.join(root, file), start=path)
        for root, _, files in os.walk(path)
        for file in files
        if ".ipynb_checkpoints" not in root
    ]
    file_dict = dict()
    for file in files:
        file_dict[file] = os.path.getmtime(os.path.join(path, file))
    return file_dict
