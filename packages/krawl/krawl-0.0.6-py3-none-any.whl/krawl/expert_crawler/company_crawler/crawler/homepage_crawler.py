"""
Example
-------
>>> python companyshot/mine_landingpage.py check https://www.glean.ai/
"""

from typing import Dict

from bs4 import BeautifulSoup

from krawl.common.flow import CrawlerBase
from krawl.common.soup_utils import HtmlPageReader

from ..recognizers import (
    BaseRecognizer,
    ExtUrlRecognizer,
    IconRecognizer,
    PrimaryHeaderRecognizer,
    TitleRecognizer,
)


class LandingPageCrawler(CrawlerBase):

    def __init__(self):
        self.reader = HtmlPageReader()
        self.workers: Dict[str, BaseRecognizer] = {
            "title": TitleRecognizer(),
            "headerprimary": PrimaryHeaderRecognizer(),
            "icon": IconRecognizer(),
            "elink": ExtUrlRecognizer()
        }

    def baserecord(self, url: str) -> dict:
        return {"url": url}

    def extract_record(
        self,
        soup: BeautifulSoup,
        url: str
    ):

        record = self.baserecord(url)
        for name, worker in self.workers.items():
            hit = worker.check(node=soup, base_url=url)
            record[name] = hit
        return record

    def check(self, url: str, save_to_file: bool = True):
        soup = self.reader.get_soup(url=url)
        record = self.extract_record(soup=soup, url=url)
        try:
            soup = self.reader.get_soup(url=url)
            record = self.extract_record(soup=soup, url=url)
        except Exception as err:
            print(f"LANDINGPAGEERR: {err} @{url}")
            record = self.baserecord(url)
        if save_to_file:
            self.dump_records(records=[record])

    def test(self):
        html_content = self.load_html_from_file()
        soup = HtmlPageReader.parse_html(html_content=html_content)
        record = self.extract_record(soup=soup)
        self.dump_records(records=[record])
