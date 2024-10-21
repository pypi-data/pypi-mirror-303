import pandas as pd
from ml_models.dtypes import LabelledClassifierDataSet
from sklearn.ensemble import RandomForestClassifier


def train_classifier(ds: LabelledClassifierDataSet):
    """
    Train the classifier and save it
    """

    feature_df = pd.DataFrame(ds.features)
    labels_series = pd.Series(ds.labels)

    classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    classifier.fit(feature_df, labels_series)
    return classifier
