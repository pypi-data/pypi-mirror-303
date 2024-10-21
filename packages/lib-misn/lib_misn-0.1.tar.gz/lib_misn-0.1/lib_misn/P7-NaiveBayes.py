import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
import seaborn as sns
# Sample dataset: You can replace this with your actual dataset
data = {
'Alt': ['Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N'],
'Est': ['0-10', '10-30', '30-60', '>60', '0-10', '10-30', '30-60', '>60', '0-10', '10-30',
'30-60', '>60'],
'Pat': ['S', 'N', 'F', 'S', 'N', 'F', 'S', 'N', 'F', 'S', 'N', 'F'],
'Type': ['F', 'I', 'B', 'T', 'F', 'I', 'B', 'T', 'F', 'I', 'B', 'T'],
'ans': ['Y', 'N', 'Y', 'N', 'Y', 'Y', 'N', 'N', 'Y', 'Y', 'N', 'N']
}
# Create DataFrame
df = pd.DataFrame(data)
# Convert categorical data to numerical

df_encoded = pd.get_dummies(df, drop_first=True)
# Features and target variable
X = df_encoded.drop('ans_Y', axis=1) # Features
y = df_encoded['ans_Y'] # Target variable (0: No, 1: Yes)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
random_state=42)
# Initialize the Naive Bayes model
model = GaussianNB()
# Train the model
model.fit(X_train, y_train)
# Make predictions
y_pred = model.predict(X_test)
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)
# Classification Report
class_report = classification_report(y_test, y_pred)
print("Classification Report:")
print(class_report)
# Visualize the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()
# Visualize the results
sns.countplot(x='ans', data=df, palette='Set2', legend=False)
plt.title('Distribution of Waiting Responses')
plt.xlabel('Will Wait (Y/N)')
plt.ylabel('Count')
plt.show()
