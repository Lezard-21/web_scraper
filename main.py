import httpx as req
from lxml import etree


def scrap(url: str):
    temp = req.get(url)
    parse_to_html(temp.text)


def parse_to_html(raw_str: str):
    parser = etree.HTMLParser()
    html_root = etree.fromstring(raw_str, parser)
    result = etree.tostring(html_root, pretty_print=True, method="html")
    str_html = result.decode("utf-8")
    save_prety_html(str_html)


def save_prety_html(html: str, file_name: str = "example.html"):
    with open(file_name, "w") as f:
        f.write(html)


def search_htags():
    pass


if __name__ == "__main__":
    scrap("https://lxml.de/parsing.html")
