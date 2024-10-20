# linear_regression/regression.py

import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, X, y):
        n = len(X)
        self.slope = (n * np.dot(X, y) - np.sum(X) * np.sum(y)) / (n * np.dot(X, X) - np.sum(X) ** 2)
        self.intercept = np.mean(y) - self.slope * np.mean(X)

    def predict(self, X):
        return self.intercept + self.slope * X
