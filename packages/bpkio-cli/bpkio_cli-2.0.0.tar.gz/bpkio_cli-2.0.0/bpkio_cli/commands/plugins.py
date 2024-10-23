import os
import subprocess
import sys
import zipfile
from datetime import datetime

import click
import cloup
from bpkio_cli.click_mods.accepts_plugins_group import (AcceptsPluginsGroup,
                                                        list_plugins_by_file)
from bpkio_cli.core.config_provider import CONFIG
from bpkio_cli.utils import prompt
from bpkio_cli.writers.breadcrumbs import display_ok
from rich.console import Console
from rich.table import Table

console = Console()


@cloup.command(
    cls=AcceptsPluginsGroup,
    aliases=["plugin"],
    help="Other functionality provided through addons (plugins)",
)
def plugins():
    pass


@cloup.command(help="List all the available addons", name="list")
def list_plugins():
    display_list_plugins()


def display_list_plugins(cache_buster=False):
    plugins = list_plugins_by_file(cache_buster=cache_buster)

    table = Table()
    table.add_column("file")
    table.add_column("commands")
    for i, (file, commands) in enumerate(plugins.items()):
        inner_table = Table(show_header=(i == 0))
        inner_table.add_column("name", width=20)
        inner_table.add_column("description", width=50)
        inner_table.add_column("scopes", width=20)
        for c in commands:
            inner_table.add_row(
                c.name,
                c.help,
                ", ".join(getattr(c, "scopes", [])),
            )

        table.add_row(
            file,
            inner_table,
        )

    console.print(table)


@cloup.command(help="Install a plugin package")
@cloup.argument("zip_file_path", type=click.Path(exists=True))
@click.pass_context
def install(ctx, zip_file_path):
    plugin_folder = CONFIG.get("path", section="plugins")
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(plugin_folder)

    # if there is any *.requirements.txt file, install it
    for f in os.listdir(plugin_folder):
        if f.endswith(".requirements.txt"):
            subprocess.check_call(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "-r",
                    os.path.join(plugin_folder, f),
                ]
            )

    display_list_plugins(cache_buster=True)


@cloup.command(
    help="Package plugin into a distributable", name="package", aliases=["zip"]
)
def zip_plugins():
    plugin_folder = CONFIG.get("path", section="plugins")
    plugins = list_plugins_by_file()
    plugin_names = list(plugins.keys())

    selected_plugins = prompt.select(
        message="Select the plugins to package",
        multiselect=True,
        choices=plugin_names,
    )

    if len(selected_plugins) == 1:
        zip_name = selected_plugins[0]
    else:
        zip_name = "multiple"
    zip_name += f"_{datetime.now().isoformat(timespec='seconds')}.bicplugins"

    with zipfile.ZipFile(zip_name, "w") as f_out:
        for p in selected_plugins:
            plugin_filename = f"{p}.py"
            f_out.write(
                os.path.join(plugin_folder, plugin_filename), arcname=plugin_filename
            )

            # check for requirements
            req_filename = f"{p}.requirements.txt"
            if os.path.exists(os.path.join(plugin_folder, req_filename)):
                f_out.write(
                    os.path.join(plugin_folder, req_filename),
                    arcname=req_filename,
                )

    display_ok("Plugin package stored in " + zip_name)


plugins.section("Management of addons", list_plugins, install, zip_plugins)
