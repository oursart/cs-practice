import numpy as np


def reshape_rows(values, width):
    array = np.asarray(values, dtype=float)
    if width <= 0 or array.size % width != 0:
        return []
    table = array.reshape(-1, width)
    return table.tolist()


def block(matrix, rows, columns):
    array = np.asarray(matrix, dtype=float)
    if array.size == 0:
        return []
    selected = array[np.ix_(rows, columns)]
    return selected.tolist()


def column_means(matrix):
    array = np.asarray(matrix, dtype=float)
    if array.size == 0:
        return []
    means = np.mean(array, axis=0)
    rounded = np.round(means, 6)
    return rounded.tolist()


def column_range(matrix, column):
    array = np.asarray(matrix, dtype=float)
    if array.size == 0:
        return 0.0
    values = array[:, column]
    spread = np.max(values) - np.min(values)
    return float(np.round(spread, 6))
