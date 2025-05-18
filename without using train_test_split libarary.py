#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sohel
#
# Created:     19/05/2025
# Copyright:   (c) sohel 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Given data
outlook = ['S', 'S', 'O', 'R', 'R', 'R', 'O', 'S', 'S', 'S', 'O', 'O', 'R', 'R']
temp = ['H', 'H', 'H', 'C', 'C', 'C', 'H', 'C', 'M', 'M', 'M', 'H', 'M', 'M']
humidity = ['H', 'H', 'H', 'H', 'N', 'N', 'N', 'H', 'H', 'H', 'N', 'N', 'H', 'N']
windy = ['F', 'T', 'F', 'F', 'F', 'T', 'T', 'F', 'F', 'T', 'T', 'F', 'T', 'T']
play = ['N', 'N', 'P', 'P', 'P', 'N', 'P', 'N', 'P', 'P', 'P', 'P', 'P', 'N']

# Create DataFrame
data = pd.DataFrame({
    'Outlook': outlook,
    'Temp': temp,
    'Humidity': humidity,
    'Windy': windy,
    'Play': play
})

# Encode categorical variables
le = LabelEncoder()
for col in data.columns:
    data[col] = le.fit_transform(data[col])

# Separate features and target
X = data.drop('Play', axis=1)
y = data['Play']

# Train Naive Bayes model
model = GaussianNB()
model.fit(X, y)

# Predict on training data
predictions = model.predict(X)

# Output results
print("Accuracy:", accuracy_score(y, predictions))
print("\nClassification Report:\n", classification_report(y, predictions))