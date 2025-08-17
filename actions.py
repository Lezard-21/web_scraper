ACTIONS = {
    "exit_app": lambda: exit(0),
}

# Se lanza cuando se intenta registrar un nombre de acción duplicado.


class ActionAlreadyExists(Exception):
    pass


def register_action(*names: str):
    def decorator(func):
        for name in names:
            if name in ACTIONS:
                raise ActionAlreadyExists(f"Action '{name}' ya existe.")
            ACTIONS[name] = func
        return func
    return decorator


def initialize_actions_list():
    if len(ACTIONS) <= 1:
        print("asdasd")
