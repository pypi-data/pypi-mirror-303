import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score,classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
# Function to import dataset
def importdata():
# Importing dataset from file path
    balance_data = pd.read_csv("abc.csv", header=None)
# Printing dataset information
    print("Dataset Length: ", len(balance_data))
    print("Dataset Head:\n", balance_data.head())
# Return the dataset
    return balance_data
# Function to split the dataset
def splitdataset(balance_data):
# Separate the features (X) and target (Y)
    X = balance_data.iloc[:, 1:5].values
    Y = balance_data.iloc[:, 0].values

# Split the dataset into training and testing sets (70% train, 30% test)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3,
random_state=100)
    return X_train, X_test, y_train, y_test
# Function to train the decision tree using entropy criterion
def train_using_entropy(X_train, y_train):
# Initialize Decision Tree with entropy criterion
    clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100,
max_depth=3, min_samples_leaf=5)
# Train the model
    clf_entropy.fit(X_train, y_train)
    return clf_entropy
# Function to make predictions on the test set
def prediction(X_test, clf_object):
# Predicting the labels for the test set
    y_pred = clf_object.predict(X_test)
    print("Predicted Values:\n", y_pred)
    return y_pred
# Function to calculate and print the accuracy and classification report
def cal_accuracy(y_test, y_pred):
    print("Accuracy: ", accuracy_score(y_test, y_pred) * 100)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
# Function to visualize the decision tree
def visualize_tree(clf_object):
    plt.figure(figsize=(8,6))
    plot_tree(clf_object, filled=True, feature_names=["Feature 1", "Feature 2",
    "Feature 3", "Feature 4"], class_names=["L", "B", "R"])
    plt.title("Decision Tree Visualization")
    plt.show()
# Main function
def main():
    # Step 1: Import the dataset
    data = importdata()
    # Step 2: Split the dataset into training and testing sets

    X_train, X_test, y_train, y_test = splitdataset(data)
    # Step 3: Train the decision tree using entropy criterion
    clf_entropy = train_using_entropy(X_train, y_train)
# Step 4: Predict the test set results
    print("Results using entropy:")
    y_pred_entropy = prediction(X_test, clf_entropy)
# Step 5: Calculate accuracy and display performance report
    cal_accuracy(y_test, y_pred_entropy)
# Step 6: Visualize the decision tree
    visualize_tree(clf_entropy)
# Running the main function
if __name__ == "__main__":
        main()