"""
Reference:
    https://github.com/yashpatel2711/DataScience-Series/blob/main/Sentiment_analysis%28IMDB%20Review%29.ipynb
"""

import pandas as pd
import numpy as np
import nltk
import re
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
nltk.download('stopwords')
from nltk.corpus import stopwords


class MultinomialNB:
    def __init__(self, alpha=1.0):
        """
        Multinomial Naive Bayes classifier with Laplace smoothing.

        Parameters:
        - alpha (float): Smoothing parameter for Laplace smoothing. Default is 1.0.
        """
        self.alpha = alpha
        self.class_prior = None  # the prior probabilities of each class
        self.class_counts = None  # the count of samples in each class
        self.feature_counts = None  # the count of each feature in each class
        self.feature_prob = None  # the probability of each feature in each class

    def fit(self, X, y):
        """
        Fit the Multinomial Naive Bayes classifier to the training data.

        Parameters:
        - X (array-like, shape = [n_samples, n_features]): Training samples.
        - y (array-like, shape = [n_samples]): Target values.

        Returns:
        None
        """
        self.class_counts = np.bincount(y)  # Count the occurrences of each class
        self.class_prior = self.class_counts / len(y)  # Calculate class prior probabilities
        self.feature_counts = np.zeros((len(np.unique(y)), X.shape[1]))  # Initialize feature count matrix

        for i, label in enumerate(np.unique(y)):
            self.feature_counts[i] = np.sum(X[y == label], axis=0)  # Count feature occurrences for each class

        self.feature_prob = (self.feature_counts + self.alpha) / (
            np.sum(self.feature_counts, axis=1, keepdims=True) + X.shape[1] * self.alpha
        )  # Calculate feature probabilities with Laplace smoothing

    def predict(self, X):
        """
        Perform classification on the input samples.

        Parameters:
        - X (array-like, shape = [n_samples, n_features]): Input samples.

        Returns:
        - y_pred (array-like, shape = [n_samples]): Predicted class labels.
        """
        x_dense = X.toarray()  # Convert sparse matrix to dense array
        scores = np.dot(x_dense, np.log(self.feature_prob.T)) + np.log(self.class_prior)
        # Calculate scores for each class using dot product and logarithm
        return np.argmax(scores, axis=1)  # Return class label with the highest score


def clean_data(text):
    soup = BeautifulSoup(text, "html.parser")
    result = re.sub('\[[^]]*\]', '',  soup.get_text().lower())
    return result


# Load the IMDb movie review dataset
df = pd.read_csv('imdb_dataset.csv')
# print(df.describe())
# print(df.head(10))
# print(df['sentiment'].value_counts())

# Preprocessing: Convert sentiment labels to binary (positive: 1, negative: 0)
df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['review'].apply(clean_data), df['sentiment'], test_size=0.5, random_state=42)

# Create a Count Vectorizer to convert text into a matrix of token counts
vectorizer = CountVectorizer(stop_words=stopwords.words('english'))  # Remove stop words from the reviews
X_train_counts = vectorizer.fit_transform(X_train)
# print(X_train_counts)
# print(y_train)
X_test_counts = vectorizer.transform(X_test)

# Create a Multinomial Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_counts, y_train)

# Perform predictions on the test set
y_pred = clf.predict(X_test_counts)

# Print actual and predicted labels
# print("Actual labels:", y_test)
# print("Predicted labels:", y_pred)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print(classification_report(y_test, y_pred, zero_division=0))

print(confusion_matrix(y_test, y_pred))



