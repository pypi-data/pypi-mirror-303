"""
Public API for directly getting page content.
"""
from typing import Callable, Iterator, List, Optional

from krawl.common.schema.dtypes import CrawlResponse, StructuredResponseGroup
from krawl.expert_crawler import GenericCrawler


def get_main_text(
    urls: List[str],
    max_char_len: int = 2000,
    min_paragraph_len: int = 3,
    max_paragraph_len: int = 2000
) -> CrawlResponse:
    crawler = GenericCrawler()
    texts = [
        crawler.check_content(url)
        for url in urls
    ]
    return CrawlResponse(
        first=texts[0],
        items=texts
    )


def get_main_content_structured(
    urls: List[str],
    max_char_len: int = 2000,
    min_paragraph_len: int = 3,
    max_paragraph_len: int = 2000,
    link_filter: Optional[Callable[..., bool]] = None
) -> StructuredResponseGroup:
    crawler = GenericCrawler()
    resp = [
        crawler.check_content_structured(url=url, link_filter=link_filter)
        for url in urls
    ]
    return StructuredResponseGroup(
        first=resp[0],
        items=resp
    )


def get_meta(
    urls: List[str],
):
    pass


class BookKeeper:
    def __init__(self):
        self._items = set([])

    def add(self, item: str):
        self._items.add(item)

    def add_all(self, items: List[str]):
        for item in items:
            self.add(item)

    def get_unknown(self, items: Iterator[str]) -> List[str]:
        unknowns = set([item for item in items if item not in self._items])
        return list(unknowns)

    def reset(self):
        self._items = set([])


_BOOKKEEPER_ = BookKeeper()


def rget(
    urls: List[str],
    max_depth: int = 1,
    curr_depth: int = 0,
    curr_url_count: int = 1,
    max_url_count: int = 100,
    max_char_len: int = 2000,
    min_paragraph_len: int = 3,
    max_paragraph_len: int = 2000,
    link_filter: Optional[Callable[..., bool]] = None,
    link_filter_batched: Optional[Callable[..., bool]] = None
) -> Iterator[StructuredResponseGroup]:
    """`Recursively` open the url and read content

    - `breathfirst`
    - link_filter_batched: Optional[Callable[..., bool]] = None
        Exeternal `LLM` callbacks to filter the links
    """

    # Limit the total urls
    end_of = min(len(urls), max_url_count-curr_url_count)
    print(f"@DEPTH={curr_depth} {curr_url_count}/{max_url_count} END={end_of}")
    if end_of > 0:
        urls = urls[:end_of]
        resp = get_main_content_structured(
            urls=urls[:end_of],
            link_filter=link_filter
        )
        _BOOKKEEPER_.add_all(urls)
        yield from resp.items
    else:
        print("CLEAR BOOK")
        _BOOKKEEPER_.reset()

    # Go next iteration
    if (curr_depth < max_depth and end_of > 0):
        print(f"@DEPTH={curr_depth} Next iteration ...")
        front = [
            (href.text, href.url)
            for resp in resp.items for href in resp.links
        ]

        # Apply the `external filter`
        if link_filter_batched:
            front = link_filter_batched(front)
        else:
            front = [url for _, url in front]

        front = _BOOKKEEPER_.get_unknown(front)
        yield from rget(
            urls=front,
            max_depth=max_depth,
            curr_depth=curr_depth+1,
            curr_url_count=curr_url_count+len(urls),
            max_url_count=max_url_count,
            link_filter=link_filter,
            link_filter_batched=link_filter_batched
        )
