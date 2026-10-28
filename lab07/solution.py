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
