import re
from urllib import parse

import tldextract


def fullhref(base: str, url: str) -> str:
    # url = (
    #     src.lstrip("/") if src.startswith("///") else
    #     parse.urljoin(base_url, src)
    # )
    return parse.urljoin(base, url)


def host(url: str) -> str:
    parsed_url = parse.urlparse(url)
    parts = parsed_url.hostname.split('.')
    domain = '.'.join(parts[-2:])
    return domain


def url_domain(url):
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    return domain


def are_homo(url1: str, url2: str) -> bool:
    return url_domain(url1) == url_domain(url2)


def are_hetero(url1: str, url2: str) -> bool:
    return not are_homo(url1, url2)


def requestable(url: str) -> bool:
    return (
        url.startswith("http") and
        re.search(r"\.pdf", url) is None
    )
