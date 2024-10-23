import os

import bugsnag
from rich import print

from cerebrium import __version__ as cerebrium_version
from cerebrium.commands.app import app
from cerebrium.commands.auth import login, save_auth_config
from cerebrium.commands.cortex import init
from cerebrium.commands.files import ls_files, cp_file, rm_file
from cerebrium.commands.project import project_app
from cerebrium.core import cli
from cerebrium.utils.bugsnag_setup import init_bugsnag

bugsnag.configure(
    api_key="606044c1e243e11958763fb42cb751c4",
    project_root=os.path.dirname(os.path.abspath(__file__)),
    release_stage=os.getenv("CEREBRIUM_ENV", "prod"),
    app_version=cerebrium_version,
    auto_capture_sessions=True,
)

init_bugsnag()

cli.add_typer(
    app,
    name="app",
    help="Manage apps. See a list of apps, app details and scale apps. Run `cerebrium app --help` for more information.",
)
cli.add_typer(
    project_app,
    name="project",
    help="Manage projects. Run `cerebrium project --help` for more information.",
)

cli.command("ls")(ls_files)
cli.command("cp")(cp_file)
cli.command("rm")(rm_file)


@cli.command()
def version():
    """
    Print the version of the Cerebrium CLI
    """
    print(cerebrium_version)


# Add commands directly to the CLI
cli.command()(login)
cli.command()(save_auth_config)
cli.command()(init)

if __name__ == "__main__":
    cli()
