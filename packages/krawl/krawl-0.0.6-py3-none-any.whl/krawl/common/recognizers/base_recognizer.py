from typing import List

from bs4 import Tag


class BaseRecognizer:
    def __init__(self):
        pass

    def check(self, node: Tag, base_url: str) -> List:
        raise NotImplementedError
