from ml_models.dtypes import LabelledClassifierDataSet
from ml_models.training_data.labelled_data_classififer import features, labels


def dataset_labelled_classifier():
    return LabelledClassifierDataSet(
        features=features,
        labels=labels
    ) 