import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin

nextYear = 2022
class KmPerYear(BaseEstimator, TransformerMixin):
    def __init__(self):
        None

    def fit(self, X, y = None):
        return self

    def transform(self, X):
        KPY = pd.DataFrame((X["Distance"] / (nextYear - X["Year"])), columns=["KmPerYear"])
        return X.join(KPY) 