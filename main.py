import constanst as const
import scrap
from cli_provider import Menu
from actions import ACTIONS

menu = Menu(const.APP_NAME, "menu.json", actions_map=ACTIONS)

while True:
    menu.show_menu("principal")
    try:
        choice = int(input("Select option: "))
        menu.execute_option("principal", choice)
    except ValueError:
        print("Please enter a number")
