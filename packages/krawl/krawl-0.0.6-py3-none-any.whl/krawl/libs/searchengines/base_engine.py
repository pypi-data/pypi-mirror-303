from abc import ABC, abstractmethod
from typing import List

from pydantic import BaseModel


class SearchHit(BaseModel):
    title: str
    href: str
    body: str


class SearchEngine(ABC):
    def __init__(self):
        self.engine = None

    @abstractmethod
    def query(self, q: str, n_hits: int = 50) -> List[SearchHit]:
        raise NotImplementedError
