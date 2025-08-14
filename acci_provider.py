from pyfiglet import Figlet
from rich.console import Console

console = Console()


def show_fonts():
    figlet = Figlet()
    fuentes = figlet.getFonts()

    console.print("[bold green]Fuentes disponibles en pyfiglet:[/bold green]")
    for i, fuente in enumerate(fuentes):
        console.print(f"{i + 1}. {fuente}")

    try:
        indice_fuente = int(console.input(
            "\n[bold yellow]Elige el número de la fuente:[/bold yellow] ")) - 1
        if indice_fuente < 0 or indice_fuente >= len(fuentes):
            raise ValueError
        fuente_seleccionada = fuentes[indice_fuente]
    except ValueError:
        console.print(
            "[bold red]Opción inválida, usando fuente por defecto.[/bold red]")
        fuente_seleccionada = "slant"
    return fuente_seleccionada


def show_colors():
    with open("rich_colors_list.txt") as f:
        console.print(
            "\n[bold green]Colores disponibles en rich:[/bold green]")
        console.print(f.read())
    color = console.input(
        "[bold yellow]Ingresa un color:[/bold yellow] ").strip().lower()
    if not color:
        color = "cyan"
    return color


def get_leyend(
        texto: str,
        fuente_seleccionada: str = "slant",
        color: str = "cyan"
):
    figlet = Figlet()
    figlet.setFont(font=fuente_seleccionada)
    ascii_text = figlet.renderText(texto)
    return ascii_text
    # console.print(f"[bold {color}]{ascii_text}[/bold {color}]")


if __name__ == "__main__":
    console.print(get_leyend("cli_provider.py"))
    # show_colors()
