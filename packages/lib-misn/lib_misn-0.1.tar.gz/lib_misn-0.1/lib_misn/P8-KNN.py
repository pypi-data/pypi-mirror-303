import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, roc_auc_score
from sklearn.preprocessing import label_binarize

# Load your dataset
df = pd.read_csv('balanceScale.csv')

# Split features and target variable
X = df.drop('B', axis=1).values  # Features
y = df['B'].values  # Target

# Binarize the output
y_bin = label_binarize(y, classes=np.unique(y))

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y_bin, test_size=0.4, random_state=42)

# Define neighbors and initialize accuracy arrays
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

for i, k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    train_accuracy[i] = knn.score(X_train, y_train)
    test_accuracy[i] = knn.score(X_test, y_test)

# Plotting accuracy
plt.title("KNN varying number of neighbors")
plt.plot(neighbors, test_accuracy, label="Test accuracy")
plt.plot(neighbors, train_accuracy, label="Train accuracy")
plt.legend()
plt.xlabel("Number of neighbors")
plt.ylabel("Accuracy")
plt.show()

# Fit KNN with the optimal number of neighbors
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)

# Predict and evaluate
y_pred = knn.predict(X_test)
print(confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1)))
print(classification_report(y_test.argmax(axis=1), y_pred.argmax(axis=1)))

# Calculate ROC curve and AUC for each class
n_classes = y_bin.shape[1]
fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_pred[:, i])
    roc_auc[i] = roc_auc_score(y_test[:, i], y_pred[:, i])

# Plot ROC curves
plt.figure()
for i in range(n_classes):
    plt.plot(fpr[i], tpr[i], label='ROC curve of class {0} (area = {1:0.2f})'.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curves for multiclass KNN (n_neighbors=7)')
plt.legend(loc='best')
plt.show()
