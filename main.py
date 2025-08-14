import httpx as req
from lxml import etree


def scrap(url: str):
    try:
        response = req.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        parse_to_html(response.text)
    except req.RequestError as e:
        print(f"Error fetching URL {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def parse_to_html(raw_str: str):
    parser = etree.HTMLParser()
    html_root = etree.fromstring(raw_str, parser)
    get_htags(html_root)
    result = etree.tostring(html_root, pretty_print=True, method="html")
    str_html = result.decode("utf-8")
    save_prety_html(str_html)


def save_prety_html(html: str, file_name: str = "example.html"):
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(html)
    except IOError as e:
        print(f"Error writing to file {file_name}: {e}")


# Define configurable list of tags to search for
DEFAULT_HEADER_TAGS = ["h1", "h2", "h3"]


def generate_xpath_expression(tags: list[str]) -> str:

    return " | ".join(f"//{tag}" for tag in tags)


def get_htags(html_root: etree._Element, tags: list[str] = DEFAULT_HEADER_TAGS):
    xpath_expr = generate_xpath_expression(tags)
    headers = search_tags(html_root, xpath_expr)
    for header in headers:
        print(f"Etiqueta: {header.tag}, Texto: {header.text}")


def search_tags(html_root: etree._Element, tag: str) -> list[etree._Element]:
    try:
        headers = html_root.xpath(tag)
        return headers
    except etree.XPathEvalError as e:
        print(f"Invalid XPath expression: {e}")
        return []


if __name__ == "__main__":
    print("""""")
    scrap("https://lxml.de/parsing.html")
