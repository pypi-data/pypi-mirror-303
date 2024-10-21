from krawl.common.config.globals import Files

from ..schema.dtypes import NodeCategory
from .base_clf import BasePredictor, MockPredictor


class PredictorFactory:

    @classmethod
    def title_predictor(cls) -> BasePredictor:
        return BasePredictor(
            modelfile=Files.html_node_classifier,
            target=NodeCategory.TITLE)

    @classmethod
    def logo_predictor(cls) -> BasePredictor:
        return BasePredictor(
            modelfile=Files.html_node_classifier,
            target=NodeCategory.LOGO)

    @classmethod
    def mock_title_predictor(cls) -> BasePredictor:
        return MockPredictor(
            modelfile=Files.html_node_classifier,
            target=NodeCategory.TITLE)
