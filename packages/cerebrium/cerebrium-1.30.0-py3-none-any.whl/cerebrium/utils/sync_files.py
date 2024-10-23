import datetime
import hashlib
import io
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import TypedDict

import requests
from rich import print
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper

from cerebrium.config import CerebriumConfig
from cerebrium.files import (
    PIP_REQUIREMENTS_FILE,
    CONDA_REQUIREMENTS_FILE,
    APT_REQUIREMENTS_FILE,
    SHELL_COMMANDS_FILE,
)
from cerebrium.types import FileData
from cerebrium.utils.requirements import requirements_to_file, shell_commands_to_file

debug = os.environ.get("LOG_LEVEL", "INFO") == "DEBUG"


class UploadURLsResponse(TypedDict):
    uploadUrls: dict[str, str]
    deleteKeys: list[str]
    markerFile: str


def get_md5(file_path: str, max_size_mb: int = 100) -> str:
    """Return MD5 hash of a file if smaller than threshold. Else, hash the os.stat info"""
    hasher = hashlib.md5()
    if os.stat(file_path).st_size > max_size_mb * 1024 * 1024:
        file_stats = os.stat(file_path)
        large_file_info = f"{file_path}-{file_stats.st_mtime}-{file_stats.st_size}"
        hasher.update(str(large_file_info).encode())
        return hasher.hexdigest()

    with open(file_path, "rb") as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()


def gather_hashes(file_list: list[str], base_dir: str = "") -> list[FileData]:
    """Gather the MD5 hashes of the local files including subdirectories."""
    local_files_payload: list[FileData] = []

    for file in file_list:
        if file.startswith("./"):
            file = file[2:]
        if base_dir and file.startswith(base_dir):
            file_name = os.path.relpath(file, base_dir)
        else:
            file_name = file
        if os.path.islink(file):
            file = os.readlink(file)
        if os.path.isfile(file):
            file_hash = get_md5(file)
            local_files_payload.append(
                {
                    "fileName": file_name,
                    "hash": file_hash,
                    "dateModified": os.stat(file).st_mtime,
                    "size": os.stat(file).st_size,
                }
            )

    return local_files_payload


def upload_file(upload_url: str, file_name: str, file_path: str, pbar: tqdm | None) -> int:
    """Function to upload a single file."""

    try:
        if os.stat(file_path).st_size == 0:
            upload_response = requests.put(upload_url, data=b"")
        else:
            with open(file_path, "rb") as file:
                # file.seek(0)  # reset file to beginning for each read
                wrapped_file = CallbackIOWrapper(pbar.update, file, "read") if pbar else file
                upload_response = requests.put(
                    upload_url,
                    data=wrapped_file,  # type: ignore
                    timeout=60,
                    stream=True,
                )
                # file.seek(0)  # reset file to beginning for next read
        if upload_response.status_code != 200:
            raise Exception(
                f"Failed to upload {file_name}. Status code: {upload_response.status_code}"
            )
        return 1
    except Exception as e:
        print(f"Error uploading {file_name}: {e}")
        return 0


def upload_files_to_s3(
    upload_urls: dict[str, str],
    base_dir: str = "",
    workers: int = 5,
    quiet: bool = False,
) -> int:
    try:
        workers = max(os.cpu_count() or workers, 10)
    except (KeyError, TypeError):
        pass
    file_keys = list(upload_urls.keys())
    if len(file_keys) == 0:
        return 0

    workers = min(workers, len(file_keys) or 1)  # don't want more workers than files
    working_dir = base_dir or os.getcwd()
    if working_dir[-1] != "/":
        working_dir = working_dir + "/"

    for path in file_keys:
        if not quiet:
            print(f"➕ Adding {path}")
    print(f"Uploading {len(upload_urls)} files...")
    # Get the working paths in the tempfile dir.
    # Necessary because the file paths in the upload_urls are relative to the working directory
    # Skipping "upload.complete" files - this is uploaded after all other files
    working_paths = [
        os.path.join(working_dir, file)
        for file in file_keys
        if file in upload_urls and file != "upload.complete"
    ]

    # Need to follow links so that we stat the actual file, not the symlink.
    real_paths = {
        path.replace(working_dir, ""): (path if not os.path.islink(path) else os.readlink(path))
        for path in working_paths
    }

    # Calculate total size of all files
    total_size = sum(os.path.getsize(path) for path in real_paths if os.path.isfile(path))

    if quiet:
        uploaded_count = _parallel_upload(workers, upload_urls, real_paths, None)
    else:
        with tqdm(
            total=total_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            desc="Upload Progress",
        ) as pbar:
            uploaded_count = _parallel_upload(workers, upload_urls, real_paths, pbar)

    return uploaded_count


def _parallel_upload(
    workers: int,
    upload_urls: dict[str, str],
    real_paths: dict[str, str],
    pbar: tqdm | None,
) -> int:
    """Upload files in parallel for faster uploads"""
    uploaded_count = 0
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(
                upload_file,
                upload_urls[key],
                key,
                real_path,
                pbar,
            )
            for key, real_path in real_paths.items()
            if key in upload_urls
        ]
        for future in as_completed(futures):
            uploaded_count += future.result()

    return uploaded_count


def upload_marker_file_and_delete(
    url: str,
    uploaded_count: int,
    build_id: str,
    files_and_hashes: list[FileData],
) -> None:
    """Upload the marker file with JSON content without actually writing anything to disk."""

    # Construct the marker file content
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    marker_content = {
        "date": current_date,
        "filesUploaded": uploaded_count,
        "buildId": build_id,
        "fileList": files_and_hashes,
    }

    # Convert the dictionary to a JSON formatted string
    json_content = json.dumps(marker_content)

    # Simulate the marker file in memory
    marker_file_content = json_content.encode()  # Convert to bytes
    marker_file = io.BytesIO(marker_file_content)

    upload_response = requests.put(url, data=marker_file)
    if upload_response.status_code != 200:
        marker_file_name = "upload.complete"

        raise Exception(
            f"Failed to upload {marker_file_name}. Status code: {upload_response.status_code}"
        )
    print("Upload complete.")


def make_cortex_dep_files(
    working_dir: str,
    config: CerebriumConfig,
):
    # Create files temporarily for upload
    requirements_files = [
        (PIP_REQUIREMENTS_FILE, config.dependencies.pip),
        (APT_REQUIREMENTS_FILE, config.dependencies.apt),
        (CONDA_REQUIREMENTS_FILE, config.dependencies.conda),
    ]
    for file_name, reqs in requirements_files:
        if reqs:
            requirements_to_file(
                reqs,
                os.path.join(working_dir, file_name),
                is_conda=file_name == CONDA_REQUIREMENTS_FILE,
            )

    shell_commands = (SHELL_COMMANDS_FILE, config.deployment.shell_commands)
    if shell_commands[1]:
        shell_commands_to_file(
            shell_commands[1],
            os.path.join(working_dir, shell_commands[0]),
        )
