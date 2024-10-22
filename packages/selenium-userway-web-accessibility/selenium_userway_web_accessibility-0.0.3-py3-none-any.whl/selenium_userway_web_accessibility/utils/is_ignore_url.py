import re
from typing import List


def is_ignore_url(url: str, ignore_urls: List[str]) -> bool:
    for ignore_url in ignore_urls:
        try:
            if re.search(ignore_url, url):
                return True
        except re.error:
            raise ValueError(f"{ignore_url} is not a valid RegExp")

    return False
