from rich.console import Console
from rich.table import Table

from .colorizer import Colorizer as CL

console = Console()


def display_table(data):
    if isinstance(data, list):
        # list of dict
        if len(data) and isinstance(data[0], dict):
            # determine whether an index needs to be shown
            showindex = True
            if len(data) and "index" in data[0]:
                showindex = False

            # Create rich table
            table = Table(show_header=True, header_style="bold")

            # Add columns
            headers = list(data[0].keys())
            if showindex:
                table.add_column("[dim white]#")
            for header in headers:
                table.add_column(f"[blue]{header}[/blue]")

            # Add rows
            for idx, dic in enumerate(data):
                row = [str(idx)] if showindex else []
                for k, v in dic.items():
                    if k in ["relativeStartTime", "relativeEndTime"]:
                        v = CL.past(v) if "(-" in v else CL.future(v)
                    row.append(str(v))
                table.add_row(*row)

            console.print(table)

        # list of scalars
        elif len(data):
            table = Table(show_header=False)

            if len(data) == 2:
                table.add_row(*[str(item) for item in data])
            else:
                for item in data:
                    table.add_row(str(item))

            console.print(table)

    if isinstance(data, dict):
        table = Table(show_header=True, header_style="bold")
        table.add_column("Key")
        table.add_column("Value")

        for k, v in data.items():
            table.add_row(f"[bold blue]{k}", str(v))

        console.print(table)
