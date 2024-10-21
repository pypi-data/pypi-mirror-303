from typing import List

from bs4 import BeautifulSoup, Tag

from krawl.common.recognizers.base_recognizer import BaseRecognizer
from krawl.common.soup_utils import TextPostprocessor, URLTool, to_html_context

from ..predictors.node_predictors import PredictorFactory


class TitleRecognizer(BaseRecognizer):
    def __init__(self):
        pass

    def check(self, node: Tag, base_url: str) -> List:
        elems = [elem for elem in [node.title, node.h1] if elem]
        if elems:
            title = TextPostprocessor.primary_text(node.title.text)
        else:
            title = ""
        return [title]


class IconRecognizer(BaseRecognizer):
    def __init__(self):
        pass

    def extract(self, soup: BeautifulSoup, base_url: str):
        icon_link = soup.find('link', rel=['icon', 'shortcut icon'])

        if icon_link:
            icon_url = icon_link.get('href')
            return URLTool.to_abs(url=icon_url, base_url=base_url)
        else:
            return None

    def check(self, node: Tag, base_url: str) -> List:
        info = self.extract(soup=node, base_url=base_url)
        return [info]


class TaglineRecognizer(BaseRecognizer):
    def __init__(self):
        pass

    def check(self, node: Tag, base_url: str) -> List:
        features = to_html_context(node).model_dump()
        hit = PredictorFactory.mock_title_predictor().hit(features=features)
        if hit:
            return node
        return None


class ExtUrlRecognizer(BaseRecognizer):
    def __init__(self):
        pass

    def check(self, node: Tag, base_url: str) -> List:
        content = URLTool.find_external_urls(soup=node, base_url=base_url)
        return content


class PrimaryHeaderRecognizer(BaseRecognizer):

    def check(self, node: Tag, base_url: str) -> List:
        elem = node.h1
        content = TextPostprocessor.primary_text(elem.text)
        return content
