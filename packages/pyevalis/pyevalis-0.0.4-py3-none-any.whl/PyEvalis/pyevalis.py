import pandas as pd
import numpy as np


def topsis(inputFileName, weights, impacts, resultFileName):
    try:
        data = pd.read_csv(inputFileName)

        if data.shape[1] < 3:
            raise ValueError("Input file must contain three or more columns.")

        data_values = data.iloc[:, 1:]
        if not all(data_values.applymap(np.isreal).all()):
            raise ValueError("Error: All columns except the first must contain numeric values only.")

        weight = list(map(float, weights.split(',')))
        cost = impacts.split(',')
        print(weight)

        if len(weight) != data_values.shape[1]:
            raise ValueError(
                f"Number of weights ({len(weight)}) does not match the number of criteria ({data_values.shape[1]}).")
        if len(cost) != data_values.shape[1]:
            raise ValueError(
                f"Number of impacts ({len(cost)}) does not match the number of criteria ({data_values.shape[1]}).")

        if not all(c in ["+", "-"] for c in cost):
            raise ValueError("Impacts must be either '+' (positive) or '-' (negative).")

        normsqrt = np.sqrt((data_values ** 2).sum(axis=0))

        normalised_data = data_values / normsqrt
        if any(normsqrt == 0):
            raise ValueError(
                "One or more columns have zero variance, leading to division by zero during normalization.")

        after_weight_data = normalised_data * weight

        vpos = []
        vneg = []

        for i in range(len(cost)):
            if cost[i] == '+':
                vpos.append(after_weight_data.iloc[:, i].max())
                vneg.append(after_weight_data.iloc[:, i].min())

            else:
                vpos.append(after_weight_data.iloc[:, i].min())
                vneg.append(after_weight_data.iloc[:, i].max())

        vpos = np.array(vpos)
        vneg = np.array(vneg)

        spos = np.sqrt(((after_weight_data - vpos) ** 2).sum(axis=1))
        sneg = np.sqrt(((after_weight_data - vneg) ** 2).sum(axis=1))

        scores = sneg / (spos + sneg)

        data['Score'] = scores
        data['Rank'] = data['Score'].rank(ascending=False, method='max')

        print("Original data with scores and ranks:")
        print(data)

        data.to_csv(resultFileName, index=False)
        print(f"TOPSIS results saved to {resultFileName}")

    except FileNotFoundError:
        print(f"Error: The file '{inputFileName}' was not found. Please check the file path and try again.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
