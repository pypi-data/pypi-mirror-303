# Save this in linear_regression.py
import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        self.slope = 0
        self.intercept = 0

    def fit(self, X, y):
        # Formula to calculate the slope and intercept
        n = len(X)
        x_mean = np.mean(X)
        y_mean = np.mean(y)
        
        self.slope = np.sum((X - x_mean) * (y - y_mean)) / np.sum((X - x_mean) ** 2)
        self.intercept = y_mean - self.slope * x_mean

    def predict(self, X):
        # Predict values using the linear model y = mx + c
        return self.slope * X + self.intercept

    def get_parameters(self):
        return self.slope, self.intercept
