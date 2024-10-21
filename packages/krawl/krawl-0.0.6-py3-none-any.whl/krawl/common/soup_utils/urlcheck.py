from collections import defaultdict
from typing import List
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup


def hostcore(url: str) -> str:
    parts = urlparse(url).netloc.split('.')
    return parts[-2]


def url_domain(url: str) -> str:
    parsed_url = urlparse(url)
    parts = parsed_url.netloc.split('.')
    if len(parts) > 1:
        return parts[-2] + '.' + parts[-1]
    return parsed_url.netloc


def url_prime(url: str) -> str:
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    fullhost = scheme + "://" + url_domain(url=url)
    return fullhost


def can_ignore(
        url: str,
        markers: List[str]) -> bool:
    if url.startswith('mailto'):
        return True
    core = hostcore(url=url)
    for marker in markers:
        if marker in core:
            return True
    return False


class URLTool:
    @staticmethod
    def find_external_urls(
        soup: BeautifulSoup,
        base_url: str
    ) -> List:
        exturls = defaultdict(set)
        all_links = [a.get('href') for a in soup.find_all('a')]
        base_host = url_domain(url=base_url)
        base_core = hostcore(url=base_url)
        abs_urls = [urljoin(base_url, link) for link in all_links]
        for link in abs_urls:
            if can_ignore(link, markers=[base_core]):
                continue
            if url_domain(url=link) != base_host:
                exturls[url_prime(link)].add(link)
        return [(k, list(v)) for k, v in exturls.items()]

    @staticmethod
    def to_abs(
        url: str,
        base_url: str
    ) -> str:
        return urljoin(base_url, url)
