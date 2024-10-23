from importlib.metadata import version
from importlib.util import find_spec

import click
from bpkio_cli.core.app_context import AppContext


# Command: DOCTOR
@click.command(hidden=True)
@click.pass_obj
def doctor(obj: AppContext):
    """Validate access to the API and display tenant information"""

    module_spec = find_spec("bpkio_cli")
    print(f"bpkio-cli - version: {version('bpkio_cli')} \n -> {module_spec.origin}")

    # Check version of the bpkio_python_sdk module with importlib
    module_spec = find_spec("bpkio_api")
    print(
        f"bpkio-python-sdk - version: {version('bpkio_python_sdk')} \n -> {module_spec.origin}"
    )

    try:
        print("\nTesting for admin mode:")
        module_spec = find_spec("bpkio_api_admin")
        print(
            f"bpkio-python-sdk-admin - version: {version('bpkio_python_sdk_admin')} \n -> {module_spec.origin}"
        )
        print("    running at admin level")
    except Exception as e:
        print(e)
        print("    running at standard level")
        pass
