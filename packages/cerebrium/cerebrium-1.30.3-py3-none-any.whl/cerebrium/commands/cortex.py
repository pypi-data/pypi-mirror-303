import cProfile
import os
from pstats import Stats
from typing import Annotated, Optional, Union

import bugsnag
import toml
import typer
from rich.console import Group
from rich.panel import Panel
from rich.text import Text

from cerebrium import api
from cerebrium import defaults
from cerebrium.config import (
    CerebriumConfig,
    ScalingConfig,
    HardwareConfig,
    DeploymentConfig,
    DependencyConfig,
    CustomRuntimeConfig,
)
from cerebrium.core import cli
from cerebrium.utils.check_cli_version import print_update_cli_message
from cerebrium.utils.deploy import package_app, get_function_names
from cerebrium.utils.logging import cerebrium_log, console
from cerebrium.utils.project import get_current_project_context
from cerebrium.utils.requirements import strip_delimiters

_EXAMPLE_MAIN = """
def run(param_1: str, param_2: str, run_id):  # run_id is optional, injected by Cerebrium at runtime
    my_results = {"1": param_1, "2": param_2}
    my_status_code = 200 # if you want to return a specific status code

    return {"my_result": my_results, "status_code": my_status_code} # return your results
"""


@cli.command("init")
def init(
    name: Annotated[str, typer.Argument(help="Name of the Cortex deployment.")],
    pip: Annotated[
        list[str],
        typer.Option(
            help=(
                "Optional list of pip requirements. "
                "Example: ['transformers', 'torch==1.31.1']"
            ),
        ),
    ] = [],
    apt: Annotated[
        list[str],
        typer.Option(
            help="Optional list of apt packages. Example: ['git', 'ffmpeg' ]",
        ),
    ] = [],
    conda: Annotated[list[str], typer.Option(help="Optional list of conda packages.")] = [],
    cpu: Annotated[
        int,
        typer.Option(
            help=(
                f"Number of vCPUs (cores) to use for the Cortex deployment. Defaults to {defaults.CPU}."
            ),
        ),
    ] = defaults.CPU,
    memory: Annotated[
        float,
        typer.Option(
            help=(
                f"Amount of memory (in GB) to use for the Cortex deployment. Defaults to {defaults.MEMORY}GB. "
            ),
        ),
    ] = defaults.MEMORY,
    compute: Annotated[
        str,
        typer.Option(
            help=f"Type of Compute to use for the Cortex deployment. Defaults to {defaults.COMPUTE}.",
        ),
    ] = defaults.COMPUTE,
    gpu_count: Annotated[
        int,
        typer.Option(
            help=f"Number of GPUs to use for the Cortex deployment. Defaults to {defaults.GPU_COUNT}. Ignored if Compute is 'CPU'.",
        ),
    ] = defaults.GPU_COUNT,
    include: Annotated[
        list[str],
        typer.Option(
            help=(
                "Comma delimited string list of relative paths to files/folder to include. "
                "Defaults to all visible files/folders in project root."
            ),
        ),
    ] = defaults.INCLUDE,
    exclude: Annotated[
        list[str],
        typer.Option(
            help=(
                "Comma delimited list of relative paths to files/folder to exclude. "
                "Defaults to all hidden files/folders in project root."
            ),
        ),
    ] = defaults.EXCLUDE,
    python_version: Annotated[
        str,
        typer.Option(
            help="Python version to use. Defaults to the current interpreter version.",
        ),
    ] = defaults.PYTHON_VERSION,
    docker_base_image_url: Annotated[
        str,
        typer.Option(
            help=f"Base Docker Image to use. Defaults to {defaults.DOCKER_BASE_IMAGE_URL}.",
        ),
    ] = defaults.DOCKER_BASE_IMAGE_URL,
    min_replicas: Annotated[
        int,
        typer.Option(
            help=f"Minimum number of replicas to keep running. Defaults to {defaults.MIN_REPLICAS}.",
        ),
    ] = defaults.MIN_REPLICAS,
    max_replicas: Annotated[
        int,
        typer.Option(
            help=f"Maximum number of replicas to keep running. Defaults to {defaults.MAX_REPLICAS}.",
        ),
    ] = defaults.MAX_REPLICAS,
    cooldown: Annotated[
        int,
        typer.Option(
            help=f"Cooldown period in seconds. Defaults to {defaults.COOLDOWN} seconds.",
        ),
    ] = defaults.COOLDOWN,
    replica_concurrency: Annotated[
        int,
        typer.Option(
            help=f"Number of requests per replica to allow concurrently. Defaults to {defaults.REPLICA_CONCURRENCY}.",
        ),
    ] = defaults.REPLICA_CONCURRENCY,
    port: Annotated[
        Union[int, None],
        typer.Option(
            help=f"Port to use for a Custom Runtime deployment. Defaults to {defaults.PORT}.",
        ),
    ] = None,
    entrypoint: Annotated[
        Union[list[str], None],
        typer.Option(
            help=f"Entrypoint command for a Custom Runtime deployment. Defaults to {defaults.ENTRYPOINT}.",
        ),
    ] = None,
    healthcheck_endpoint: Annotated[
        Union[str, None],
        typer.Option(
            help=f"Healthcheck endpoint for a Custom Runtime deployment. Defaults to '{defaults.HEALTHCHECK_ENDPOINT}'.",
        ),
    ] = None,
):
    """
    Initialize an empty Cerebrium Cortex project.
    """
    console.print(f"Initializing Cerebrium Cortex project in new directory ./{name}")

    print_update_cli_message()

    if not os.path.exists(name):
        os.makedirs(name)
    else:
        cerebrium_log(
            level="WARNING",
            message="Directory already exists. Please choose a different name.",
            prefix_separator="\t",
        )
        bugsnag.notify(Exception("Directory already exists error."))
        raise typer.Exit(1)

    if not os.path.exists(os.path.join(name, "main.py")):
        with open(os.path.join(name, "main.py"), "w", newline="\n") as f:
            f.write(_EXAMPLE_MAIN)

    pip_dict = strip_delimiters(pip)
    apt_dict = strip_delimiters(apt)
    conda_dict = strip_delimiters(conda)

    scaling_config = ScalingConfig(
        min_replicas=min_replicas,
        max_replicas=max_replicas,
        cooldown=cooldown,
        replica_concurrency=replica_concurrency,
    )
    hardware_config = HardwareConfig(
        cpu=cpu,
        memory=memory,
        compute=compute,
        gpu_count=gpu_count,
        provider=defaults.PROVIDER,
        region=defaults.REGION,
    )
    if entrypoint is None and healthcheck_endpoint is None and port is None:
        custom_runtime_config = None
    else:
        entrypoint = entrypoint or defaults.ENTRYPOINT
        healthcheck_endpoint = healthcheck_endpoint or defaults.HEALTHCHECK_ENDPOINT
        port = port or defaults.PORT
        custom_runtime_config = CustomRuntimeConfig(
            entrypoint=entrypoint, port=port, healthcheck_endpoint=healthcheck_endpoint
        )
    dependency_config = DependencyConfig(pip=pip_dict, apt=apt_dict, conda=conda_dict)
    deployment_config = DeploymentConfig(
        name=name,
        python_version=python_version,
        docker_base_image_url=docker_base_image_url,
        include=include,
        exclude=exclude,
        shell_commands=defaults.SHELL_COMMANDS,
    )
    config = CerebriumConfig(
        scaling=scaling_config,
        hardware=hardware_config,
        deployment=deployment_config,
        dependencies=dependency_config,
        custom_runtime=custom_runtime_config,
    )
    config.to_toml(f"{name}/cerebrium.toml")
    console.print("Cerebrium Cortex project initialized successfully!")
    console.print(f"cd {name} && cerebrium deploy to get started")


@cli.command(
    "deploy",
    help="""
Deploy a new Cortex app to Cerebrium. Run `cerebrium deploy --help` for more information.\n
    \n
Usage: cerebrium deploy [OPTIONS]\n
\n
  Deploy a Cortex app to Cerebrium.\n
\n
Options:\n
  --name TEXT                    Name of the App. Overrides the value in the TOML file if provided.\n
  --disable-syntax-check         Flag to disable syntax check.\n
  --log-level [DEBUG|INFO]       Log level for the Cortex deployment. Can be one of 'DEBUG' or 'INFO'.\n
  --config-file PATH             Path to the cerebrium config TOML file. You can generate a config using `cerebrium init`.\n
  -y, --disable-confirmation     Disable the confirmation prompt before deploying.\n
  --disable-animation            Disable TQDM loading bars and yaspin animations.\n
  --disable-build-logs           Disable build logs during a deployment.\n
  -h, --help                     Show this message and exit.\n
\n
Examples:\n
  # Deploy an app with the default settings\n
  cerebrium deploy\n
\n
  # Deploy an app with a custom name and disabled syntax check\n
  cerebrium deploy --name my_app --disable-syntax-check\n
    """,
)
def deploy(
    name: Annotated[
        Optional[str],
        typer.Option(
            "--name",
            help="Name of the App. Overrides the value in the TOML file if provided.",
        ),
    ] = None,
    disable_syntax_check: Annotated[
        bool, typer.Option(help="Flag to disable syntax check.")
    ] = False,
    log_level: Annotated[
        str,
        typer.Option(
            help="Log level for the Cortex deployment. Can be one of 'DEBUG' or 'INFO'",
        ),
    ] = "INFO",
    config_file: Annotated[
        str,
        typer.Option(
            help="Path to the cerebrium config TOML file. You can generate a config using `cerebrium init`."
        ),
    ] = "./cerebrium.toml",
    disable_confirmation: Annotated[
        bool,
        typer.Option(
            "--disable-confirmation",
            "-y",
            help="Disable the confirmation prompt before deploying.",
        ),
    ] = False,
    disable_animation: Annotated[
        bool,
        typer.Option(
            "--disable-animation",
            help="Disable TQDM loading bars and yaspin animations.",
        ),
    ] = False,
    disable_build_logs: Annotated[
        bool,
        typer.Option("--disable-build-logs", help="Disable build logs during a deployment."),
    ] = False,
):
    print_update_cli_message()

    # Check user is logged in
    project_id = get_current_project_context()
    if not project_id:
        cerebrium_log(
            message="You must log in to use this functionality. Please run 'cerebrium login'",
            color="red",
        )
        bugsnag.notify(Exception("User not logged in"))
        raise typer.Exit(1)

    with cProfile.Profile() as pr:
        # load config toml file
        log_level = log_level.upper()
        assert log_level in [
            "DEBUG",
            "INFO",
            "WARNING",
            "ERROR",
            "INTERNAL",
        ], "Log level must be one of 'DEBUG' or 'INFO'"
        try:
            toml_config = toml.load(config_file)["cerebrium"]
        except FileNotFoundError:
            cerebrium_log(
                message="Could not find cerebrium.toml file. Please run `cerebrium init` to create one.",
                color="red",
            )
            bugsnag.notify(
                Exception(
                    "Could not find cerebrium.toml file. Please run `cerebrium init` to create one."
                )
            )
            raise typer.Exit(1)
        except KeyError:
            cerebrium_log(
                message="Could not find 'cerebrium' key in cerebrium.toml file. Please run `cerebrium init` to create one.",
                color="red",
            )
            raise typer.Exit(1)
        except Exception as e:
            bugsnag.notify(e)
            cerebrium_log(message=f"Error loading cerebrium.toml file: {e}", color="red")
            raise typer.Exit(1)

        deployment_section = toml_config.get("deployment", {})
        hardware_section = toml_config.get("hardware", {})
        config_error = False
        if not deployment_section:
            cerebrium_log(
                message="Deployment section is required in cerebrium.toml file. Please add a 'deployment' section.",
                level="ERROR",
            )
            config_error = True
        if "name" not in deployment_section:
            cerebrium_log(
                message="`deployment.name` is required in cerebrium.toml file. Please add a 'name' field to the 'deployment' section.",
                level="ERROR",
            )
            config_error = True
        if "gpu" in hardware_section:
            cerebrium_log(
                message="`hardware.gpu` field is deprecated. Please use `hardware.compute` instead.",
                level="ERROR",
            )
            config_error = True
        if "cuda_version" in deployment_section:
            cerebrium_log(
                message="`deployment.cuda_version` field is deprecated. Please use `deployment.docker_base_image_url` instead.",
                level="ERROR",
            )
            config_error = True
            # Check if the provider is Coreweave, if so print a V3 deprecation warning
        if hardware_section.get("provider", "aws") == "coreweave":
            cerebrium_log(
                message="Cortex V4 does not support Coreweave. Please consider updating your deployment to AWS.",
                level="ERROR",
            )
            config_error = True
        if config_error:
            raise typer.Exit(1)

        # Override name from TOML file if --name is provided
        if name:
            deployment_section["name"] = name

        deployment_config: DeploymentConfig = DeploymentConfig(**deployment_section)
        scaling_config: ScalingConfig = ScalingConfig(**toml_config.get("scaling", {}))
        hardware_config: HardwareConfig = HardwareConfig(**toml_config.get("hardware", {}))

        if "runtime" in toml_config and "custom" in toml_config["runtime"]:
            if "entrypoint" in toml_config["runtime"]["custom"]:
                if isinstance(toml_config["runtime"]["custom"]["entrypoint"], str):
                    toml_config["runtime"]["custom"]["entrypoint"] = toml_config["runtime"]["custom"]["entrypoint"].split()
            custom_runtime_config = CustomRuntimeConfig(**toml_config["runtime"]["custom"])
        else:
            custom_runtime_config = None

        dependency_config: DependencyConfig = DependencyConfig(
            **toml_config.get("dependencies", {})
        )

        config: CerebriumConfig = CerebriumConfig(
            scaling=scaling_config,
            hardware=hardware_config,
            deployment=deployment_config,
            dependencies=dependency_config,
            custom_runtime=custom_runtime_config,
        )

        build_status, setup_response = package_app(
            config,
            disable_build_logs,
            log_level,  # type: ignore
            disable_syntax_check,
            disable_animation,
            disable_confirmation,
        )
        if setup_response is None:
            message = "Error setting up your app and getting your logs. Please check your dashboard or contact support if the issue persists."
            cerebrium_log(
                message=message,
                color="red",
            )
            bugsnag.notify(Exception(message))
            raise typer.Exit(1)
        if build_status == "success":
            project_id = setup_response["projectId"]
            endpoint = setup_response["internalEndpoint"]
            dashboard_url = f"{api.dashboard_url}/projects/{project_id}/apps/{project_id}-{config.deployment.name}"
            info_string = f"App Dashboard: {dashboard_url}"

            # Loop over each function name and create the POST endpoint
            if custom_runtime_config is None:
                info_string += "\n\nEndpoints:"
                function_names = get_function_names()
                for function_name in function_names:
                    info_string += f"\n[bold red]POST[bold red] {endpoint}/{function_name}"

            dashboard_info = Panel(
                info_string,
                title=f"[bold green] {config.deployment.name} is now live!  ",
                border_style="green",
                width=140,
            )

            console.print(Group(dashboard_info))
        elif build_status in ["build_failure", "init_failure"]:
            bugsnag.notify(Exception("Unfortunately there was an issue with your deployment"))
            console.print(
                Text(
                    "Unfortunately there was an issue with your deployment",
                    style="red",
                )
            )
    pr.disable()
    if log_level == "INTERNAL":
        stats = Stats(pr)
        stats.sort_stats("tottime").print_stats(10)
