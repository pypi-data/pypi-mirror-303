import joblib


class ModelIO:

    def load(model_filename: str):
        """
        Load the saved classifier
        """
        model_filename = model_filename
        try:
            classifier = joblib.load(model_filename)
            return classifier
        except Exception as e:
            print(f"Error loading the classifier: {e}")
            return None

    def dump(classifier, model_filename):
        """
        Save the trained classifier to a file
        """
        joblib.dump(classifier, model_filename)
        print(f"Classifier saved to {model_filename}")
