import numpy as np

def mae(y_test, pred):
    """Calculate Mean Absolute Error."""
    return np.mean(np.abs(y_test - pred))

def mse(y_test, pred):
    """Calculate Mean Squared Error."""
    return np.mean((y_test - pred) ** 2)


def rmse(y_test, pred):
    """Calculate Root Mean Squared Error."""
    return np.sqrt(np.mean((y_test - pred) ** 2))


def rmsle(y_test, pred):
    """Calculate Root Mean Squared Log Error."""
    return np.sqrt(np.mean((np.log1p(y_test) - np.log1p(pred)) ** 2))


def mape(y_test, pred):
    """Calculate Mean Absolute Percentage Error."""
    return np.mean(np.abs((y_test - pred) / y_test)) * 100


def correlation(y_test, y_pred):
    """Calculate correlation coefficient."""
    cov_matrix = np.cov(y_test, y_pred)
    return cov_matrix[0, 1] / np.sqrt(cov_matrix[0, 0] * cov_matrix[1, 1])

