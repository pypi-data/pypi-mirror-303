import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
# Importing the dataset
data = pd.read_csv('balanceScale.csv', header=None)
# Assigning column names (assuming the dataset does not have headers)
# The first column is the target and the remaining are the features
data.columns = ['target', 'feature1', 'feature2', 'feature3', 'feature4']
# Separating features and target variable
X = data.drop('target', axis=1)
y = data['target']
# Splitting the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Training the SVM model with a linear kernel
model = SVC(kernel='linear')
# Fitting the model
model.fit(X_train, y_train)
# Predicting the test set results
y_pred = model.predict(X_test)
# Calculating accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
# Confusion Matrix and Classification Report
print("Classification Report:\n", classification_report(y_test, y_pred))
# Plotting Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=np.unique(y_test),
yticklabels=np.unique(y_test))
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
# Parameter tuning using GridSearchCV
param_grid = {'C': [0.1, 1, 10, 100], 'kernel': ['linear', 'rbf']}
grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=3)
grid.fit(X_train, y_train)
# Best parameters and estimator
print("Best Parameters: ", grid.best_params_)
print("Best Estimator: ", grid.best_estimator_)
# Predicting again using the best model
y_pred_optimized = grid.predict(X_test)
# Accuracy after optimization
optimized_accuracy = accuracy_score(y_test, y_pred_optimized)
print(f"Optimized Accuracy: {optimized_accuracy:.2f}")
# Confusion Matrix and Classification Report after optimization
print("Optimized Classification Report:\n", classification_report(y_test,
y_pred_optimized))
