from rich.console import Console
from rich.columns import Columns
from rich.table import Table
from rich.text import Text

console = Console()
# console.print("""
# \t┌──────────────────────────────────────────────────┐
# \t│                                                  │
# \t│                                                  │
# \t│                                                  │
# \t│[green] ▄▄█████▄   ▄█████▄   ██▄████   ▄█████▄  ██▄███▄[/green]  │
# \t│[green] ██▄▄▄▄ ▀  ██▀    ▀   ██▀       ▀ ▄▄▄██  ██▀  ▀██[/green]  │
# \t│[green]  ▀▀▀▀██▄  ██         ██       ▄██▀▀▀██  ██    ██ [/green] │
# \t│[green] █▄▄▄▄▄██  ▀██▄▄▄▄█   ██       ██▄▄▄███  ███▄▄██▀ [/green] │
# \t│[green]  ▀▀▀▀▀▀     ▀▀▀▀▀    ▀▀        ▀▀▀▀ ▀▀  ██ ▀▀▀   [/green] │
# \t│[green]                                         ██       [/green] │
# \t│                                                  │
# \t└──────────────────────────────────────────────────┘"
#   """)
logo = """\n\n
          /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$
         /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$__  $$
        | $$  \\__/| $$  \\__/| $$  \\ $$| $$ \\  $$| $$  \\  $$
        |  $$$$$$ | $$      | $$$$$$$/| $$$$$$$$| $$$$$$$/
        \\____  $$| $$      | $$__  $$| $$__  $$| $$____/
   /$$  \\ $$| $$    $$| $$  \\ $$| $$  | $$| $$
  |  $$$$$$/|  $$$$$$/| $$  | $$| $$  | $$| $$
 \\______/  \\______/ |__/  |__/|__/  |__/|__/
                              \n
       v.0.1
        """

options_principal_menu = [
    "[1]  Open from a link",
    "[2]  Open from a file",
    "[3]  Exit"]

options_link_menu = [
    "Search tags",
    "Show full html",
    "Show full html",
    "Show full html",
    "Show full html",
    "Show full html",
    "Show full html",
    "Show full html",
    "Show full html",
    "Exit"]


def print_options(options: list, two_columns: bool = False):
    numbered_options = [f"[{i}] {option}" for i,
                        option in enumerate(options, start=1)]
    if two_columns:
        mid_point = len(numbered_options) // 2
        col1 = numbered_options[:mid_point]
        col2 = numbered_options[mid_point:]
        table = Table(show_header=False, box=None)
        [table.add_row(option) for option in col1]
        table2 = Table(show_header=False, box=None)
        [table2.add_row(option) for option in col2]
        columns = Columns([table, table2],
                          equal=True,
                          expand=True,
                          width=console.width // 2 - 2,
                          align="center")
        console.print(columns)
    else:
        for option in numbered_options:
            console.print(option, padding=2)
    console.print()


def show_menu(menu: str):
    title = Text(logo, style="bold green", justify="center")
    console.print(title, justify="center")
    match menu:
        case "principal":
            print_options(options_principal_menu)
        case "link":
            print_options(options_link_menu, True)
        case _:
            print_options(options_principal_menu)


if __name__ == "__main__":
    show_menu("link")
