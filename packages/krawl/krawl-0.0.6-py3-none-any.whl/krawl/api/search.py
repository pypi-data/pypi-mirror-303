from typing import Iterator, List

from krawl.api.pagecontent import get_main_content_structured
from krawl.common.schema.dtypes import StructuredResponse
from krawl.libs.searchengines import DDGEngine, SearchHit

_ddgo_ = DDGEngine()


def _ignore(host: str) -> bool:
    return "linkedin" in host


def search_web(q: str, n_hits: int = 50) -> List[SearchHit]:
    return _ddgo_.query(q=q, n_hits=n_hits)


def search_and_click(q: str, n_hits: int = 50) -> Iterator[StructuredResponse]:
    """Search a QUERY and open each HIT
    """
    hits = search_web(q, n_hits=n_hits)
    for hit in hits:
        yield (
            StructuredResponse(
                title=hit.title,
                coretext=hit.body
            ) if _ignore(hit.href) else
            get_main_content_structured(urls=[hit.href]).first
        )
