import numpy as np
import pandas as pd

class LinrarRegression:

    def __init__(self):
        self.coeff = None

    def fit(self, X, y):
        n = X.shape[0]

        ones = np.ones((n, 1))

        X = np.hstack((ones, X))
        
        B = np.linalg.inv(X.T @ X) @ X.T @ y

        self.coeff = B

    def predict(self, X):        

        n = X.shape[0]
        
        ones = np.ones((n, 1))

        X = np.hstack((ones, X))
        
        return(X @ self.coeff)