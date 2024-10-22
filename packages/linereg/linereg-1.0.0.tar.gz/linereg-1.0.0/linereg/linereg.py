
import numpy as np

class Linereg:
    def __init__(self):
        self.slope = 0
        self.intercept = 0

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        n = len(X)

        # Calculate slope and intercept
        self.slope = (n * np.sum(X * y) - np.sum(X) * np.sum(y)) / (n * np.sum(X**2) - np.sum(X)**2)
        self.intercept = (np.sum(y) - self.slope * np.sum(X)) / n

    def predict(self, X):
        return self.slope * np.array(X) + self.intercept
