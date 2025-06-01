import httpx as req
from lxml import etree


def scrap(url: str):
    temp = req.get(url)
    parse_to_html(temp.text)


def parse_to_html(raw_str: str):
    parser = etree.HTMLParser()
    html_root = etree.fromstring(raw_str, parser)
    get_htags(html_root)
    result = etree.tostring(html_root, pretty_print=True, method="html")
    str_html = result.decode("utf-8")
    save_prety_html(str_html)


def save_prety_html(html: str, file_name: str = "example.html"):
    with open(file_name, "w") as f:
        f.write(html)


def get_htags(html_root: etree._Element):
    tags = search_tags(html_root, "h1 | //h2 | //h3")
    for header in tags:
        print(
            f"Etiqueta: {header.tag}, Texto: {header.text}")


def search_tags(html_root: etree._Element, tag: str):
    headers = html_root.xpath(f"//{tag}")
    return headers


if __name__ == "__main__":
    print("""""")
    scrap("https://lxml.de/parsing.html")
