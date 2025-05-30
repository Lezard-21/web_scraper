import httpx as req
from lxml import etree


def scrap():
    temp = req.get("https://lxml.de/parsing.html")
    parse_to_html(temp.text)


def parse_to_html(raw_str: str):
    parser = etree.HTMLParser()
    html_root = etree.fromstring(raw_str, parser)
    result = etree.tostring(html_root, pretty_print=True, method="html")
    save_prety_html(result)


def save_prety_html(byte_html: bytes, file_name: str = "example.html"):
    temp = byte_html.decode("utf-8")
    with open(file_name, "w") as f:
        f.write(temp)


if __name__ == "__main__":
    scrap()
