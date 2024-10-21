from abc import ABC, abstractmethod
from typing import Callable, Dict, List

import jsonlines
from bs4 import BeautifulSoup

from krawl.common.config.globals import Files


class CrawlerABC(ABC):

    @abstractmethod
    def extract_record(
        soup: BeautifulSoup,
        node_selector: Callable
    ) -> Dict:
        pass


class CrawlerBase(CrawlerABC):

    def extract_record(
        soup: BeautifulSoup,
        node_selector: Callable
    ) -> Dict:
        raise NotImplementedError

    def dump_record(self, record: Dict):
        filename = Files.record_file
        with jsonlines.open(filename, 'a') as fh:
            fh.write(record)

    def dump_records(self, records: List[Dict]):
        with jsonlines.open(Files.record_file, 'a') as fh:
            for rec in records:
                fh.write(rec)
        print(f"Written records in file {Files.record_file}")

    def load_html_from_file(self):
        """
        For _testing purpose_
        """
        filename = "data/dummies/tiny.html"
        with open(filename) as fh:
            return fh.read()
