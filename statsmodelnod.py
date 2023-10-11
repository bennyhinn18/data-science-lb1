import numpy as np
import statsmodels.api as sm

def fit_linear_regression(x, y):
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    return model

def print_regression_summary(model):
    print(model.summary())

def generate_random_data():
    x = np.random.rand(100)
    y = 2*x + np.random.normal(0, 1, 100)
    return x, y
