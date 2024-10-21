import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from tabulate import tabulate
import ipywidgets as widgets
from IPython import get_ipython
from IPython.display import display
from IPython.core.display import HTML
from IPython.display import clear_output

from ..stats.stats import *


def train_test_split(X, y, test_size=0.2):
    n_samples = X.shape[0]
    n_train = int((1 - test_size) * n_samples)

    # Randomly shuffle the data before splitting
    indices = np.random.permutation(n_samples)
    X_train, X_val = X[indices[:n_train]], X[indices[n_train:]]
    y_train, y_val = y[indices[:n_train]], y[indices[n_train:]]

    return X_train, X_val, y_train, y_val


def display_table_in_jupyter(metrics_dict):
    try:
        metrics_df = pd.DataFrame(metrics_dict)
        styled_df = metrics_df.style.format({
            "Value": "{:.4f}"  # Adjust format as needed
        }).set_table_styles([
            {'selector': 'thead th',
             'props': [('background-color', '#f7f7f9'), ('color', '#333'), ('font-weight', 'bold')]},
            {'selector': 'tbody td', 'props': [('text-align', 'center')]},
        ]).set_properties(**{
            'background-color': '#f4f4f9',  # Light background for table cells
            'border': '1px solid #ddd',  # Border for table cells
        })
        # Display in Jupyter
        display(styled_df)

    except Exception:
        print(tabulate(metrics_dict.items(), headers=["Evaluation Metric", "Value"], tablefmt="grid"))


def min_max_scale(X):
    """Scale features to [0, 1]."""
    X_min = X.min(axis=0)  # Minimum values for each feature
    X_max = X.max(axis=0)  # Maximum values for each feature
    return (X - X_min) / (X_max - X_min)  # Scale to [0, 1]


class LinearRegression:
    def __init__(self, lr=0.001, n_iters=1000, patience=10, normalize=True):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        self.patience = patience
        self.normalize = normalize
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.train_errors = []
        self.val_errors = []

    def fit(self, X, y, split: int = 0.7, shuffle=False, seed=None):
        """
        Fit the model to the training data.

        X: numpy array; Contains independent variables.

        y: numpy array; Contains dependent variable.

        split: int between 0 and 1.

        shuffle: bool.

        seed: int.
        """
        if not isinstance(X, np.ndarray) or not isinstance(y, np.ndarray):
            raise ValueError("X and y must be numpy arrays.")
        if X.ndim != 2 or y.ndim != 1:
            raise ValueError("X must be 2D and y must be 1D.")

        num_samples = X.shape[0]
        if num_samples != y.shape[0]:
            raise ValueError("Number of samples in X and y must be equal.")
        split_index = int(num_samples * split)  # 70% for training

        if shuffle:
            if seed is not None:
                np.random.seed(seed)
            else:
                np.random.seed(None)
            shuffled_indices = np.random.permutation(len(X))
            X, y = X[shuffled_indices], y[shuffled_indices]

        indices = np.arange(num_samples)
        self.X_train, self.X_test = X[indices[:split_index]], X[indices[split_index:]]
        self.y_train, self.y_test = y[indices[:split_index]], y[indices[split_index:]]

        if self.normalize:
            self.X_train = min_max_scale(self.X_train)
            self.y_train = min_max_scale(self.y_train)
            self.X_test = min_max_scale(self.X_test)
            self.y_test = min_max_scale(self.y_test)

        n_samples, n_features = self.X_train.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        best_mse = float('inf')
        wait = 0

        for i in range(self.n_iters):
            y_pred = np.dot(self.X_train, self.weights) + self.bias

            dw = (1 / n_samples) * np.dot(self.X_train.T, (y_pred - self.y_train))
            db = (1 / n_samples) * np.sum(y_pred - self.y_train)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            train_error = mse(self.y_train, self.predict(self.X_train))
            val_error = mse(self.y_test, self.predict(self.X_test))

            # Store the errors
            self.train_errors.append(train_error)
            self.val_errors.append(val_error)

            if self.X_test is not None and self.y_test is not None:
                val_pred = self.predict(self.X_test)
                current_mse = mse(self.y_test, val_pred)
                # print(f"Iteration {i}: Train MSE = {mse(y, self.predict(X))}, Val MSE = {current_mse}")

                if current_mse < best_mse:
                    best_mse = current_mse
                    wait = 0
                else:
                    wait += 1
                    if wait >= self.patience:
                        # print("Early stopping...")
                        break

    def predict(self, X):
        """Predict using the trained model."""
        if self.normalize:
            X = min_max_scale(X)
        return np.dot(X, self.weights) + self.bias

    def plot(self, X=None, y=None):
        """Plot the results of the linear regression."""
        if X is None or y is None:
            X = self.X_test
            y = self.y_test
        if X.shape[1] != 1:
            print("Single independent variable plot possible only")
            return
        y_pred = self.predict(X)

        def plot1():
            plt.figure(figsize=(8, 6))
            plt.scatter(X, y, color='blue', label='Data points', s=10)
            plt.plot(X, y_pred, color='black', linewidth=2, label='Prediction')
            plt.xlabel('Independent variable')
            plt.ylabel('Dependent variable')
            plt.title('Linear Regression Results')
            plt.legend()
            plt.grid(True)
            plt.show()

        def plot2():
            residuals = y - y_pred

            plt.figure(figsize=(8, 6))
            plt.scatter(X, residuals)
            plt.axhline(0, color='red', linestyle='--')  # Add a horizontal line at 0 for reference
            plt.xlabel('Independent variable (x)')
            plt.ylabel('Residuals')
            plt.title('Residual Plot')
            plt.show()

        def plot3():
            residuals = y - y_pred

            plt.figure(figsize=(8, 6))
            sns.histplot(residuals, kde=False, stat='density', bins=20, color='blue')
            mean = np.mean(residuals)
            std = np.std(residuals)
            xmin, xmax = plt.xlim()  # Get the limits of the current x-axis for proper curve fitting

            n = len(residuals)
            skewness = (n / ((n - 1) * (n - 2))) * np.sum(((residuals - mean) / std) ** 3)

            # Calculate excess kurtosis from scratch
            kurtosis = (n * (n + 1) * np.sum(((residuals - mean) / std) ** 4)) / ((n - 1) * (n - 2) * (n - 3)) - (
                    (3 * (n - 1) ** 2) / ((n - 2) * (n - 3)))

            x_vals = np.linspace(xmin, xmax, 100)
            normal_curve = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_vals - mean) / std) ** 2)

            plt.plot(x_vals, normal_curve, color='red', label='Normal Distribution Curve')
            plt.xlabel('Residuals')
            plt.ylabel('Density')
            plt.title('Histogram of Residuals with Normal Distribution Curve')
            plt.legend(title=f"Skewness: {skewness:.3f}\nKurtosis: {kurtosis:.3f}")
            plt.show()

        def plot4():
            residuals = y - y_pred
            sorted_residuals = np.sort(residuals)
            n = len(sorted_residuals)
            theoretical_quantiles = np.linspace(0, 1, n + 2)[1:-1]  # Avoiding 0 and 1
            normal_quantiles = np.array(
                [np.percentile(np.random.normal(0, 1, 100000), q * 100) for q in theoretical_quantiles])

            # Alternatively, to generate the normal quantiles directly:
            # normal_quantiles = np.random.normal(0, 1, n)

            plt.figure(figsize=(8, 6))
            plt.scatter(normal_quantiles, sorted_residuals, label="Residuals")

            # Add a 45-degree line for reference
            min_val = min(normal_quantiles.min(), sorted_residuals.min())
            max_val = max(normal_quantiles.max(), sorted_residuals.max())
            plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label="45-degree Line")

            # Add labels and title
            plt.xlabel('Theoretical Quantiles (Normal Distribution)')
            plt.ylabel('Sample Quantiles (Residuals)')
            plt.title('Q-Q Plot of Residuals')
            plt.legend()
            plt.show()

        def plot5():
            plt.figure(figsize=(8, 6))
            plt.plot([i for i in range(len(self.train_errors))], self.train_errors, label='Training Error',
                     color='blue')
            plt.plot([i for i in range(len(self.val_errors))], self.val_errors, label='Validation Error', color='red')
            plt.xlabel('Number of Training Samples')
            plt.ylabel('Mean Squared Error')
            plt.title('Model Performance Curve')

            plt.legend()
            plt.grid(True)
            plt.show()

        def plot6():
            X = np.concatenate([self.X_train, self.X_test])
            y = np.concatenate([self.y_train, self.y_test])
            train_sizes = np.linspace(0.1, 1.0, 10)

            # Split data manually into training and validation sets
            X_train, X_val, y_train, y_val = train_test_split(X, y)

            train_errors = []
            val_errors = []
            temp = LinearRegression()
            # Loop through different training set sizes
            for train_size in train_sizes:
                n_train = int(train_size * X_train.shape[0])

                # Use a subset of training data
                X_train_subset = X_train[:n_train]
                y_train_subset = y_train[:n_train]

                # Train the model on the subset
                temp.fit(X_train_subset, y_train_subset, split=.8)

                # Predict on the training and validation sets
                y_train_pred = temp.predict(X_train_subset)
                y_val_pred = temp.predict(X_val)

                # Calculate training and validation error using MSE
                train_error = mse(y_train_subset, y_train_pred)
                val_error = mse(y_val, y_val_pred)

                # Store the errors
                train_errors.append(train_error)
                val_errors.append(val_error)
            plt.figure(figsize=(8, 6))
            sample_sizes = train_sizes * X_train.shape[0]

            # Plot the training and validation errors
            plt.plot(sample_sizes, train_errors, label='Training Error', color='blue')
            plt.plot(sample_sizes, val_errors, label='Validation Error', color='red')

            plt.xlabel('Number of Training Samples')
            plt.ylabel('Mean Squared Error')
            plt.title('Learning Curve')

            # Diagnose whether the model has high bias, ideal generalization, or high variance
            if train_errors[-1] > 0.1 and val_errors[-1] > 0.1 and abs(
                    train_errors[-1] - val_errors[-1]) < 0.05:
                plt.text(0.5, 0.6, 'High Bias (Underfitting)', fontsize=12, color='black',
                         transform=plt.gca().transAxes)
            elif val_errors[-1] > 0.1 and (val_errors[-1] - temp.train_errors[-1]) > 0.05:
                plt.text(0.5, 0.6, 'High Variance (Overfitting)', fontsize=12, color='black',
                         transform=plt.gca().transAxes)
            else:
                plt.text(0.5, 0.6, 'Ideal Generalization', fontsize=12, color='black', transform=plt.gca().transAxes)
            plt.legend()
            plt.grid(True)
            plt.show()

        shell_name = get_ipython().__class__.__name__
        if shell_name == 'ZMQInteractiveShell' or shell_name == 'Shell':
            custom_style = """
            <style>
                .widget-tab-contents {
                    border: 2px solid #4CAF50;
                    border-radius: 5px;
                    padding: 10px;
                }
                .widget-tab {
                    background-color: #f2f2f2;
                }
                .widget-tab > .p-TabBar-tab {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px;
                    border-radius: 4px;
                }
                .widget-tab > .p-TabBar-tab.p-mod-selected {
                    background-color: #45a049;
                    font-weight: bold;
                }
                .widget-tab > .p-TabBar-tab:hover {
                    background-color: #66bb6a;
                }
            </style>
            """
            display(HTML(custom_style))

            tab1 = widgets.Output()
            tab2 = widgets.Output()
            tab3 = widgets.Output()
            tab4 = widgets.Output()
            tab5 = widgets.Output()
            tab6 = widgets.Output()

            with tab1:
                plot1()
            with tab2:
                plot2()
            with tab3:
                plot3()
            with tab4:
                plot4()
            with tab5:
                plot5()
            with tab6:
                plot6()

            tab_widget = widgets.Tab(children=[tab1, tab2, tab3, tab4, tab5, tab6])
            tab_widget.set_title(0, 'Scatter Plot')
            tab_widget.set_title(1, 'Residual Plot')
            tab_widget.set_title(2, 'Histogram')
            tab_widget.set_title(3, 'Q-Q Plot')
            tab_widget.set_title(4, 'Model Performance Curve')
            tab_widget.set_title(5, 'Learning Curve')

            display(tab_widget)
        else:
            plot1()
            plot2()
            plot3()
            plot4()
            plot5()
            plot6()

    def evaluate(self, X=None, y=None):
        """Evaluate the model on the test set."""
        if X is None or y is None:
            X = self.X_test
            y = self.y_test

        y_pred = self.predict(X)
        mse_value = mse(y, y_pred)
        mae_value = mae(y, y_pred)
        rmse_value = rmse(y, y_pred)
        rmsle_value = rmsle(y, y_pred)
        mape_value = mape(y, y_pred)
        correlation_value = correlation(y, y_pred)

        shell_name = get_ipython().__class__.__name__
        if shell_name == 'ZMQInteractiveShell' or shell_name == 'Shell':
            metrics_dict = {
                "Evaluation Metric": ["MSE", "MAE", "RMSE", "RMSLE", "MAPE", "Correlation"],
                "Value": [mse_value, mae_value, rmse_value, rmsle_value, mape_value, correlation_value]
            }
            display_table_in_jupyter(metrics_dict)

        else:
            metrics_dict = {
                "MSE": mse_value,
                "MAE": mae_value,
                "RMSE": rmse_value,
                "RMSLE": rmsle_value,
                "MAPE": f"{mape_value:.2f}%",
                "Correlation": correlation_value
            }
            print(tabulate(metrics_dict.items(), headers=["Evaluation Metric", "Value"], tablefmt="grid"))


__all__ = ['LinearRegression']
