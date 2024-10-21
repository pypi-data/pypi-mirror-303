from typing import Dict

import pandas as pd

from .model_io import ModelIO


class BaseClassifier:

    def __init__(self, modelfile: str):
        self.clf = ModelIO.load(model_filename=modelfile)

    def predict(self, features: Dict) -> str:
        new_data_df = pd.DataFrame([features])
        predictions = self.clf.predict(new_data_df)
        return predictions[0]


class BasePredictor(BaseClassifier):

    def __init__(
        self,
        modelfile: str,
        target: str
    ):
        super().__init__(modelfile=modelfile)
        self.target = target

    def hit(self, features: Dict) -> bool:
        return self.predict(features=features)


class MockPredictor(BasePredictor):

    def hit(self, features: Dict) -> bool:
        from random import random
        if random() > 0.5:
            return True
        return False
        return False
