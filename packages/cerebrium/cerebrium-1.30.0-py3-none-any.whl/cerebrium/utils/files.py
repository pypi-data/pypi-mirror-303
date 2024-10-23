import fnmatch
import hashlib
import os
import zipfile
from pathlib import Path

from rich import print

from cerebrium.files import INTERNAL_FILES
from cerebrium.utils.logging import cerebrium_log


def ensure_pattern_format(pattern: str):
    if not pattern:
        return pattern
    sep = os.path.sep
    if pattern.startswith(f"{sep}"):  # Starts with /
        cerebrium_log(
            prefix="ValueError",
            level="ERROR",
            message="Pattern cannot start with a forward slash. Please use a relative path.",
        )
        raise ValueError(
            "Pattern cannot start with a forward slash. Please use a relative path."
        )
    if pattern.endswith(sep):
        pattern = os.path.join(pattern, "*")
    elif os.path.isdir(pattern) and not pattern.endswith(sep):
        pattern = os.path.join(pattern, "*")

    pattern = str(Path(pattern))
    return pattern


def determine_includes(include: list[str], exclude: list[str]):
    include_set = [i.strip() for i in include]
    include_set = set(map(ensure_pattern_format, include_set))

    exclude_set = [e.strip() for e in exclude]
    exclude_set = set(map(ensure_pattern_format, exclude_set))

    file_list: list[str] = []
    for root, _, files in os.walk("."):
        for file in files:
            full_path = str(Path(root) / file)
            if any(fnmatch.fnmatch(full_path, pattern) for pattern in include_set) and not any(
                fnmatch.fnmatch(full_path, pattern) for pattern in exclude_set
            ):
                file_list.append(full_path)
    return file_list


def file_hash(
    files: list[str] | str,
) -> str:
    """
    Hash the content of each file, avoiding metadata.
    """
    h = hashlib.sha256()
    files = files if isinstance(files, list) else [files]

    for file in sorted(files):
        if os.path.exists(file):
            with open(file, "rb") as f:
                h.update(f.read())
    return h.hexdigest()


def string_hash(strings: list[str] | str) -> str:
    """
    Hash the content of each string, avoiding metadata.
    """
    h = hashlib.sha256()
    strings = strings if isinstance(strings, list) else [strings]

    # Sort ensures the hash is deterministic
    for string in sorted(strings):
        h.update(string.encode())
    return h.hexdigest()


def check_deployment_size(files: str | list[str], max_size_mb: int = 100):
    """
    Check if the sum of all files is less than max_size MB
    """
    files = files if isinstance(files, list) else [files]
    total_size = 0
    for file in files:
        if os.path.exists(file):
            total_size += os.path.getsize(file)

    return total_size > max_size_mb * 1024 * 1024


def get_all_file_hashes() -> dict[str, str]:
    """Get the hashes of all the files in the current directory"""
    file_hashes = {}
    for root, _, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = file_hash(file_path)
    return file_hashes


def create_zip_file(
    zip_file_name: str,
    file_list: list[str],
    temp_dir: str,
):
    """
    Create a zip file with the given files

    Args:
        zip_file_name (str): Name of the zip file to be created
        file_list (List[str]): List of files to be added to the zip file
        temp_dir (str): Temporary directory to store the zip file
    """

    tmp_dir_files = os.listdir(temp_dir)

    for f in INTERNAL_FILES:
        if f in tmp_dir_files and f in file_list:
            file_list.remove(f)

    with zipfile.ZipFile(zip_file_name, "w") as zip_file:
        print("Zipping files...")
        for f in file_list:
            if os.path.isfile(f):
                zip_file.write(f)

        for f in INTERNAL_FILES:
            if f in tmp_dir_files:
                zip_file.write(os.path.join(temp_dir, f), arcname=os.path.basename(f))
