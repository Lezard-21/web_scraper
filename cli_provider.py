from rich.console import Console
from rich.columns import Columns
from rich.table import Table
from rich.text import Text
from acci_provider import get_leyend

console = Console()
# ┌──────────────────────────────────────────────────────┐
# │                                                      │
# │                                                      │
# │                                                      │
# │   ▄▄█████▄   ▄█████▄   ██▄████   ▄█████▄  ██▄███▄    │
# │   ██▄▄▄▄ ▀  ██▀    ▀   ██▀       ▀ ▄▄▄██  ██▀  ▀██   │
# │    ▀▀▀▀██▄  ██         ██       ▄██▀▀▀██  ██    ██   │
# │   █▄▄▄▄▄██  ▀██▄▄▄▄█   ██       ██▄▄▄███  ███▄▄██▀   │
# │    ▀▀▀▀▀▀     ▀▀▀▀▀    ▀▀        ▀▀▀▀ ▀▀  ██ ▀▀▀     │
# │                                           ██         │
# │                                                      │
# └──────────────────────────────────────────────────────┘
#                           v1.0

leyend = get_leyend("SCRAP")
# center para mostrar el menu en diferentes columnas y centrado
alingment = "center"

options_principal_menu = [
    "Open from a link",
    "Open from a file",
    "Exit"]

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

menu_names = {
    "principal": options_principal_menu,
    "link": options_link_menu,
}
# para agregar mas menus solo se tienen que:
#    1.crear una lista con las opciones
#    2.-asignarle un nombre y agregarlo a la lista de nombres(menu_names), tambien asignarle una lista de opciones
#   3-agregar la lista match


def print_options(options: list):
    numbered_options = [f"[[cyan bold]{i}[/cyan bold]] {option}" for i,
                        option in enumerate(options, start=1)]
    two_columns = True if len(
        numbered_options) > 5 and alingment == "center" else False
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
                          width=(console.width // 2) - 5,
                          align=alingment)
        console.print(columns)
    else:
        table = Table(show_header=False, box=None)
        [table.add_row(option) for option in numbered_options]
        console.print(table, justify=alingment)
    console.print()


def show_menu(menu: str):
    title = Text(leyend, style="bold green")
    title_container = Table(show_header=False, box=None)
    [title_container.add_row(title)]
    console.print(title_container, justify=alingment)
    for name, options in menu_names:
        if name == menu:
            print_options(options)


if __name__ == "__main__":
    show_menu("link")
