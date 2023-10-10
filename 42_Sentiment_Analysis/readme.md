# Sentiment Analysis Project

This project implements sentiment analysis using two different approaches:

1. Multinomial Naive Bayes Classifier
2. BERT-based Neural Network Classifier

Note: Some errors might be shown but do not affect the running of the models. The models might take anywhere from 5 minutes to 2 hours to run.

## Getting Started

To get started with the project, follow the instructions below.

### Prerequisites

- Python 3.x
- Libraries: pandas, numpy, nltk, sklearn, BeautifulSoup, torch, transformers

### Installation

Install the required libraries:
- pip install pandas numpy nltk sklearn BeautifulSoup torch transformers

### Data Preprocessing

The IMDb movie review dataset is used for this project. The dataset is loaded and preprocessed as follows:

1. Clean the text data by removing HTML tags and special characters.
2. Convert sentiment labels to binary (positive: 1, negative: 0).
3. Split the dataset into training and testing sets.

## Approach 1: Multinomial Naive Bayes Classifier

The Multinomial Naive Bayes classifier with Laplace smoothing is implemented. The steps are as follows:

1. Create a CountVectorizer to convert text into a matrix of token counts.
2. Fit the classifier on the training data.
3. Perform predictions on the test data.
4. Calculate accuracy, classification report, and confusion matrix.

## Approach 2: BERT-based Neural Network Classifier

The BERT-based Neural Network classifier is implemented using the transformers library. The steps are as follows:

1. Define the SentimentDataset class to preprocess and tokenize the input data.
2. Define the custom collate function for DataLoader.
3. Load the BERT tokenizer and the IMDb dataset.
4. Split the dataset into training and test sets.
5. Create the training and test datasets.
6. Create the data loaders.
7. Initialize the BERT model for sequence classification.
8. Define the optimizer and learning rate.
9. Train the model for multiple epochs.
10. Evaluate the model on the training and test sets.
11. Print train loss, train accuracy, train F1 score, test accuracy, and test F1 score for each epoch.

## References

- Approach 1: [Reference 1](https://github.com/yashpatel2711/DataScience-Series/blob/main/Sentiment_analysis%28IMDB%20Review%29.ipynb)
- Approach 2: [Reference 2](https://github.com/LinkedInLearning/transformers-text-classification-for-nlp-using-bert-2478096/blob/main/IMDB_text_classification.ipynb)