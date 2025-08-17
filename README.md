# Web Scraping (CLI)

Interfaz de presentación por línea de comandos (CLI) para un proyecto de web scraping. Actualmente, solo está terminada la capa de presentación mediante CLI; la lógica de scraping y acciones aún no están implementadas.

## Estado del proyecto

- Solo la interfaz de menús por CLI está funcional.
- Acciones como `open_link`, `open_file`, `search_tags`, `show_html` no están implementadas todavía.
- La única acción operativa es `exit_app`.

## Requisitos

- Python 3.13+
- Dependencias:
  - pyfiglet
  - rich
  - lxml

Estas ya están declaradas en [pyproject.toml](cci:7://file:///home/david/workspace/web_scraping/pyproject.toml:0:0-0:0).

## Instalación

Instala las dependencias del proyecto (método simple):
```bash
pip install -U pyfiglet rich lxml
```

O con uv:
```bash
uv add pyfiglet rich lxml
```

## Ejecución

Desde la raíz del proyecto:
```bash
python main.py
```

- Se mostrará el título en ASCII y el menú principal definido en [menu.json](cci:7://file:///home/david/workspace/web_scraping/menu.json:0:0-0:0).
- Selecciona las opciones por número.
- El renderizado de texto/tablas usa Rich.

## Estructura del proyecto

```
.
├─ main.py                  # Punto de entrada: instancia y controla el menú
├─ cli_provider.py          # Clase Menu: carga JSON y muestra opciones con Rich
├─ actions.py               # Mapa de acciones (ACTIONS) y decorador register_action
├─ acci_provider.py         # Utilidades de ASCII art (pyfiglet) y colores
├─ constanst.py             # Constantes de la app (nombre, disposición)
├─ menu.json                # Definición de menús y acciones
├─ rich_colors_list.txt     # Listado de colores de Rich (utilidad)
├─ pyproject.toml           # Metadatos del proyecto y dependencias
└─ README.md
```

## Uso de la CLI

- [Menu](cci:2://file:///home/david/workspace/web_scraping/cli_provider.py:10:0-74:54) en [cli_provider.py](cci:7://file:///home/david/workspace/web_scraping/cli_provider.py:0:0-0:0):
  - Carga [menu.json](cci:7://file:///home/david/workspace/web_scraping/menu.json:0:0-0:0) con [load_json()](cci:1://file:///home/david/workspace/web_scraping/cli_provider.py:18:4-20:34).
  - Muestra opciones formateadas con Rich ([print_options()](cci:1://file:///home/david/workspace/web_scraping/cli_provider.py:22:4-45:23)).
  - Ejecuta acciones por nombre con [execute_option()](cci:1://file:///home/david/workspace/web_scraping/cli_provider.py:62:4-74:54), usando `ACTIONS` de [actions.py](cci:7://file:///home/david/workspace/web_scraping/actions.py:0:0-0:0).

- [main.py](cci:7://file:///home/david/workspace/web_scraping/main.py:0:0-0:0):
  - Crea el menú con [Menu(APP_NAME, "menu.json", actions_map=ACTIONS)](cci:2://file:///home/david/workspace/web_scraping/cli_provider.py:10:0-74:54).
  - Muestra el menú `principal` y solicita una opción numérica en bucle.

## Implementación de acciones (pendiente)

Registra funciones en [actions.py](cci:7://file:///home/david/workspace/web_scraping/actions.py:0:0-0:0) con el decorador [register_action](cci:1://file:///home/david/workspace/web_scraping/actions.py:11:0-18:20) o añádelas al diccionario `ACTIONS`. Ejemplo:

```python
from actions import register_action

@register_action("open_link")
def open_link():
    # TODO: Implementar apertura de URL y scraping
    print("open_link no está implementado todavía")
```

Asegúrate de que el nombre coincide con [menu.json](cci:7://file:///home/david/workspace/web_scraping/menu.json:0:0-0:0):
```json
{ "label": "Open from a link", "action": "open_link" }
```

## Roadmap

- Implementar acciones:
  - open_link: leer URL y cargar HTML (posible uso de requests + lxml).
  - open_file: leer HTML desde archivo local.
  - search_tags: búsqueda por selectores.
  - show_html: imprimir HTML o fragmentos.
- Validaciones y manejo de errores.
- Tests básicos.
- Documentar casos de uso y ejemplos.

## Notas

- El título en ASCII se genera con [get_leyend()](cci:1://file:///home/david/workspace/web_scraping/acci_provider.py:39:0-48:65) en [acci_provider.py](cci:7://file:///home/david/workspace/web_scraping/acci_provider.py:0:0-0:0) usando pyfiglet.
- La disposición del menú y estilo usan Rich. Si no ves colores, verifica tu terminal.
```
