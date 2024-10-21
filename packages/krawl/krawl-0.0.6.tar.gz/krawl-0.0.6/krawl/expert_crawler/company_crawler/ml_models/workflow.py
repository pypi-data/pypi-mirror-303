from ml_models.dataset import dataset_labelled_classifier
from ml_models.train import train_classifier
from sklearn.model_selection import train_test_split


class ClassifierWF:
    dssample = dataset_labelled_classifier()

    def run():
        features = ClassifierWF.dssample.features
        labels = ClassifierWF.dssample.labels

        X_train, X_test, y_train, y_test = train_test_split(
            features, labels, test_size=0.2, random_state=42)

        clf = train_classifier(ds=dataset_labelled_classifier())
        return clf
