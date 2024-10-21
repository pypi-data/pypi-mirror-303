from typing import List

from duckduckgo_search import DDGS

from krawl.common import singleton

from .base_engine import SearchEngine, SearchHit


@singleton
class DDGEngine(SearchEngine):
    def __init__(self, track: str = ""):
        print(f"__INIT_DDGEngine__ {track}")
        super().__init__()
        self.engine = DDGS()

    def query(self, q: str, n_hits: int = 50) -> List[SearchHit]:
        hits = self.engine.text(q, max_results=n_hits)
        return [
            SearchHit(**hit)
            for hit in hits
        ]
