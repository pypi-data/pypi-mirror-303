from typing import Callable, Iterable, List, Optional

from bs4 import Tag

from krawl.common.soup_utils import TextPostprocessor
from krawl.common.url_utils import are_hetero, are_homo, fullhref, requestable


class SoupGrabber:
    """Extract all kinds of stuff from a bs4 soup object."""

    @staticmethod
    def elemtext(elem: Tag) -> str:
        if elem:
            return TextPostprocessor.primary_text(elem.text)
        else:
            return ""

    @staticmethod
    def elemtext_iter(elems: List[Tag]) -> List[str]:
        return [TextPostprocessor.primary_text(e.text) for e in elems]

    @staticmethod
    def title(soup: Tag) -> str:
        """Extract the `title`."""
        return SoupGrabber.elemtext(soup.title)

    @staticmethod
    def h1(soup: Tag) -> str:
        """Extract the first h1 tag from a soup object."""
        return SoupGrabber.elemtext(soup.h1)

    @staticmethod
    def h1_primary(soup: Tag) -> str:
        return SoupGrabber.h1(soup)

    @staticmethod
    def h1_all(soup: Tag) -> List[str]:
        """Extract all `h1`"""
        return SoupGrabber.elemtext_iter(soup.find_all('h1'))

    @staticmethod
    def h2_all(soup: Tag) -> List[str]:
        """Extract all `h1`"""
        return SoupGrabber.elemtext_iter(soup.find_all('h2'))

    @staticmethod
    def links(
        soup: Tag,
        base_url: str,
        within: str = "body",
        top_n: int = 288,
        filter_condition: Optional[Callable[..., bool]] = None
    ) -> Iterable[dict]:
        """Extract all `urls`

        Parameters
        ----------
        top_n : int
            The top n links to extract
        """
        for idx, elem in enumerate(soup.select(f"{within} a".strip())):
            if idx >= top_n:
                break
            text = TextPostprocessor.primary_text(elem.text)
            url = elem.get("href", "")
            if text and url:
                fullurl = fullhref(base_url, url)
                if not requestable(fullurl):
                    continue
                if (
                    filter_condition is None or
                    filter_condition(text, fullurl, base_url)
                ):
                    yield {
                        "text": text,
                        "url": fullurl
                    }

    @staticmethod
    def inbound_links(
        soup: Tag,
        base_url: str,
        within: str = "body",
        top_n: int = 288
    ) -> Iterable[dict]:
        def _homo(text, url, baseurl) -> bool:
            return are_homo(url, baseurl)
        yield from SoupGrabber.links(soup, base_url, filter_condition=_homo)

    @staticmethod
    def outbound_links(
        soup: Tag,
        base_url: str,
        within: str = "body",
        top_n: int = 288
    ) -> Iterable[dict]:
        def _hetero(text, url, baseurl) -> bool:
            return are_hetero(url, baseurl)
        yield from SoupGrabber.links(soup, base_url, filter_condition=_hetero)

    @staticmethod
    def image_primary(soup: Tag, base_url: str) -> str:
        """Extract the `url` of the primary image"""

        def _position_score(i: int) -> float:
            score = (
                -1e6 if i >= 5.0 else
                (5.0 - i)
            )
            return score

        def _numerical_from_attribute(
            x: str,
            min_: int = 0
        ) -> int:
            try:
                val = int(x)
                if val >= min_:
                    return val
                return 0
            except Exception:
                return 0

        def _numerical_score(attr: str) -> float:
            return _numerical_from_attribute(attr, min_=100)/100

        def _size_score(width: str, style: str) -> float:
            score = _numerical_score(width) + _numerical_score(style)
            return score

        images = []
        for idx, elem in enumerate(soup.find_all('img')):
            if idx >= 10:
                break

            src = elem.get("src", "")
            width = elem.get("width")
            style = elem.get("style")

            url = fullhref(base_url, src)

            sizescore = _size_score(width, style)
            posscore = _position_score(idx)
            score = posscore + sizescore
            images.append((url, score))
            # print(f"IMAGEINFO@{idx}: {elem}")
            # print(f"SIZESCORE: {width} | {style} | {sizescore} | {posscore}")

        for url_score in sorted(images, key=lambda x: x[-1], reverse=True):
            return url_score[0]

        return ""
