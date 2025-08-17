import json
from rich.console import Console
from rich.columns import Columns
from rich.table import Table
from rich.text import Text
from acci_provider import get_leyend

console = Console()


class Menu():

    def __init__(self, leyend: str, json_menus_path: str, actions_map: dict = None, alignment: str = "center"):
        self.leyend = get_leyend(leyend)
        self.alignment = alignment
        self.actions_map = actions_map
        self.menus = self.load_json(json_menus_path)

    def load_json(self, path: str) -> dict:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def print_options(self, options: list):
        numbered_options = [f"[[cyan bold]{i}[/cyan bold]] {option}" for i,
                            option in enumerate(options, start=1)]
        two_columns = True if len(
            numbered_options) > 5 and self.alignment == "center" else False
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
                              align=self.alignment)
            console.print(columns)
        else:
            table = Table(show_header=False, box=None)
            [table.add_row(option) for option in numbered_options]
            console.print(table, justify=self.alignment)
        console.print()

    def show_menu(self, menu_name: str):
        menu = self.menus.get(menu_name)
        if not menu:
            console.print(f"[red]Menu '{menu_name}' not found[/red]")
            return
        title = Text(self.leyend, style="bold green")
        title_container = Table(show_header=False, box=None)
        [title_container.add_row(title)]
        console.print(title_container, justify=self.alignment)
        items = menu["items"]
        options = []
        for i, item in enumerate(items):
            options.append(item["label"])
        self.print_options(options)

    def execute_option(self, menu_name: str, choice: int):
        try:
            menu = self.menus[menu_name]
            option = menu["items"][choice - 1]
            action_name = option["action"]
            action_func = self.actions_map.get(action_name)
            if callable(action_func):
                action_func()
            else:
                console.print(
                    f"[red]No function found for action '{action_name}'[/red]")
        except (IndexError, KeyError):
            console.print("[red]Invalid option[/red]")


if __name__ == "__main__":
    menu = Menu("SCRAP", "menu.json", actions_map={
                "exit_app": lambda: exit(0)})
    menu.show_menu("principal")
