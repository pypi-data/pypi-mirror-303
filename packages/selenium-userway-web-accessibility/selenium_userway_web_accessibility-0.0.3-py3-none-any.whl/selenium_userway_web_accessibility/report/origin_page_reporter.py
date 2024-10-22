import re
import time

from ..utils.base36_encode import base36_encode

URL_REGEX = re.compile(r"^https?://([^/]+)(/.*)?$")


def generate_origin_page_filename(url: str) -> str:
    match = URL_REGEX.match(url)

    if not match:
        return ""

    site_name, path = match.groups()
    path = (path or "").rstrip("/").replace("/", "-")
    hash_value = base36_encode(int(time.time()))

    return "-".join(filter(None, [site_name, path, f"{hash_value}.html"]))


def save_origin_page_html(page_path: str, html_content: str) -> None:
    with open(page_path, "w", encoding="utf-8") as file:
        file.write(html_content)
