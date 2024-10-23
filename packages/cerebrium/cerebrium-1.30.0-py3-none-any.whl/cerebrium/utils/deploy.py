import os
import re
import sys
import time
from datetime import datetime
from typing import Any

import bugsnag
import pytz
import typer
from rich import print
from rich.live import Live
from rich.spinner import Spinner
from tzlocal import get_localzone

from cerebrium import __version__, api
from cerebrium.api import (
    cerebrium_request,
    upload_cortex_files,
)
from cerebrium.config import CerebriumConfig
from cerebrium.types import LogLevel
from cerebrium.utils.display import confirm_deployment
from cerebrium.utils.files import determine_includes
from cerebrium.utils.logging import cerebrium_log, console
from cerebrium.utils.project import get_current_project_context
from cerebrium.utils.termination import _graceful_shutdown
from cerebrium.utils.verification import run_pyflakes

CEREBRIUM_ENV = os.getenv("CEREBRIUM_ENV", "prod")


def _create_new_app_request(
    payload: dict,
) -> dict[str, Any]:
    project_id = get_current_project_context()
    setup_response = cerebrium_request("POST", f"v2/projects/{project_id}/apps", payload)
    status_code = setup_response.status_code
    if setup_response is None:
        cerebrium_log(
            level="ERROR",
            message=f"An unknown error occurred when deploying your app. Please login and try again. If the error "
            f"continues to persist, contact support. Status code: {status_code}",
            prefix="",
        )
        bugsnag.notify(Exception("Error deploying app, no response from create app"))
        raise typer.Exit(1)

    if setup_response.status_code == 401 or setup_response.status_code == 403:
        cerebrium_log(
            level="ERROR",
            message="You must log in to use this functionality. Please run 'cerebrium login'",
            prefix="",
        )
        bugsnag.notify(
            Exception(
                f"User not logged in on deploy command. {status_code} response from create app"
            )
        )
        raise typer.Exit(1)

    if setup_response.status_code != 200:
        # Safely get the error message from the response
        error_message = setup_response.json().get("message", "Unknown error")

        cerebrium_log(
            message=f"There was an error deploying your app. Status: {status_code}\n{error_message}",
            prefix="",
            level="ERROR",
        )
        bugsnag.notify(
            Exception(
                f"Error deploying app, non-200 response from create app. Status: {status_code} Error: {error_message}"
            )
        )
        raise typer.Exit(1)
    return setup_response.json()


def package_app(
    config: CerebriumConfig,
    disable_build_logs: bool,
    log_level: LogLevel,
    disable_syntax_check: bool,
    disable_animation: bool,
    disable_confirmation: bool,
) -> tuple[str, dict[str, Any]]:
    # Get the files in the users directory
    file_list = determine_includes(
        include=config.deployment.include,
        exclude=config.deployment.exclude,
    )
    if file_list == []:
        cerebrium_log(
            "No files to upload. Please ensure you have files in your project.",
            level="ERROR",
        )
        raise typer.Exit(1)

    if "./main.py" not in file_list and "main.py" not in file_list:
        cerebrium_log(
            "main.py not found. Please ensure your project has a main.py file.",
            level="ERROR",
        )
        raise typer.Exit(1)

    if not disable_syntax_check:
        run_pyflakes(files=file_list, print_warnings=True)

    if not disable_confirmation:
        if not confirm_deployment(config):
            sys.exit()

    payload = config.to_payload()
    payload["logLevel"] = log_level
    payload["disableBuildLogs"] = disable_build_logs
    payload["cliVersion"] = __version__

    setup_response = _create_new_app_request(payload)

    build_id = setup_response["buildId"]
    print(f"Build ID: {build_id}")
    build_status = str(setup_response["status"])

    if build_status == "pending":
        upload_cortex_files(
            build_id=build_id,
            cerebrium_config=config,
            upload_url=setup_response["uploadUrl"],
            zip_file_name=os.path.basename(setup_response["keyName"]),
            config=config,
            file_list=file_list,
            disable_animation=disable_animation,
        )

    build_status = poll_build_logs(
        build_id=build_id,
        cerebrium_config=config,
        build_status=build_status,
        disable_animation=disable_animation,
    )

    return build_status, setup_response


def format_created_at(created_at: str) -> str:
    """
    Formats the created_at timestamp to a nice local time format.

    Args:
        created_at (str): The original timestamp.

    Returns:
        str: The formatted local time string.
    """
    utc_time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ")
    local_tz = get_localzone()
    local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_time.strftime("%H:%M:%S")


idle_intervals = [20, 60, 120, 180]
idle_messages = [
    "Hang in there, still building!",
    "Still building, thanks for your patience!",
    "Almost there, please hold on!",
    "Thank you for waiting, we're nearly done!",
]


def poll_build_logs(
    build_id: str,
    cerebrium_config: CerebriumConfig,
    build_status: str,
    disable_animation: bool = False,
    interval: int = 2,
) -> str:
    """
    Polls logs at specified intervals and prints only new log lines. Handles the polling of logs with optional spinner and status handling.

    Args:
        build_id (str): The unique identifier of the build.
        cerebrium_config (CerebriumConfig): The Cerebrium configuration object.
        build_status (str): The current build status.
        disable_animation (bool): Flag to disable the spinner animation.
        interval (int): The interval in seconds between polls. Defaults to 2 seconds.

    Returns:
        str: The final build status.
    """
    seen_logs: set[tuple[str, str]] = set()
    spinner = None
    last_log_time = datetime.now()
    next_idle_update_index = 0

    if build_status == "pending":
        spinner = (
            None if disable_animation else Spinner("dots", "Building App...", style="gray")
        )

        live = Live(spinner, console=console, refresh_per_second=10)
        live.start()
        try:
            while build_status not in ["success", "build_failure", "init_failure"]:
                logs_response = api.fetch_build_logs(cerebrium_config.deployment.name, build_id)
                build_status = logs_response["status"]
                current_log_lines = logs_response["logs"]

                for log_entry in current_log_lines:
                    created_at = format_created_at(log_entry.get("createdAt"))
                    log_text = log_entry.get("log")
                    log_key = (created_at, log_text)  # Create a hashable key

                    if log_key not in seen_logs:
                        if "error" in log_text.lower():
                            cerebrium_log(f"{created_at} {log_text}", level="ERROR")
                        else:
                            cerebrium_log(f"{created_at} {log_text}")
                        seen_logs.add(log_key)
                        last_log_time = datetime.now()
                        next_idle_update_index = 0
                        if spinner:
                            spinner.text = "Building App..."

                # Check idle time and update spinner message if necessary
                idle_time = (datetime.now() - last_log_time).total_seconds()
                if (
                    spinner
                    and next_idle_update_index < len(idle_intervals)
                    and idle_time >= idle_intervals[next_idle_update_index]
                ):
                    spinner.text = (
                        idle_messages[next_idle_update_index % len(idle_messages)]
                        or "Building App..."
                    )
                    next_idle_update_index += 1

                time.sleep(interval)
        except KeyboardInterrupt:
            live.stop()
            _graceful_shutdown(
                app_name=cerebrium_config.deployment.name,
                build_id=build_id,
                is_interrupt=True,
            )
        finally:
            live.stop()
    else:
        if spinner:
            spinner.stop(text="Build failed")
        cerebrium_log("ERROR", "Build failed.")

    return build_status


def get_function_names() -> list[str]:
    try:
        # Read the content of the main.py file
        with open("main.py", "r") as file:
            python_file_content = file.read()

        # Regular expression to match both 'def' and 'async def' function definitions
        function_pattern = r"(?:async\s+)?def\s+([a-zA-Z_]\w*)\s*\(.*?\):"

        # Find all function definitions
        function_names = re.findall(function_pattern, python_file_content)

        if len(function_names) == 0:
            return ["{function_name}"]

        # Output the list of function names
        return function_names

    except Exception:
        return ["{function_name}"]
