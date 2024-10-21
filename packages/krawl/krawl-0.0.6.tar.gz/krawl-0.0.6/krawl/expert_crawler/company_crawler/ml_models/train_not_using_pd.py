# Sample data for features and labels
from sklearn.ensemble import RandomForestClassifier
features = [
    {'word_count': 10, 'other_feature': 0.5},
    {'word_count': 15, 'other_feature': 0.8},
    {'word_count': 8, 'other_feature': 0.3},
    {'word_count': 12, 'other_feature': 0.6},
]

labels = ['tagline', 'heroline', 'tagline', 'heroline']

# Convert features and labels to lists
feature_list = [[d['word_count'], d['other_feature']] for d in features]
label_list = labels

# Train the classifier

classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(feature_list, label_list)

# New data point for prediction
new_data_point = {'word_count': 22, 'other_feature': 0.2}
new_data_list = [new_data_point['word_count'], new_data_point['other_feature']]

# Use the trained classifier to make a prediction
predicted_label = classifier.predict([new_data_list])

print("Predicted Label:", predicted_label[0])
