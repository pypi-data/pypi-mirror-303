import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Sample data for features and labels
features = [
    {'word_count': 10, 'other_feature': 0.5},
    {'word_count': 15, 'other_feature': 0.8},
    {'word_count': 8, 'other_feature': 0.3},
    {'word_count': 12, 'other_feature': 0.6},
]

labels = ['tagline', 'heroline', 'tagline', 'heroline']

# Convert features into a DataFrame
features_df = pd.DataFrame(features)

# Convert labels into a Series
labels_series = pd.Series(labels)

# Now, you can use features_df and labels_series with the fit function
# For example, if you are using scikit-learn:

classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(features_df, labels_series)

new_data_point = {'word_count': 22, 'other_feature': 0.2}
new_data_df = pd.DataFrame([new_data_point])
predicted_label = classifier.predict(new_data_df)
print("Predicted Label:", predicted_label[0])
