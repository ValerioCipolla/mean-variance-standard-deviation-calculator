import numpy as np

# output mean, variance, standard devition, min, min, and sum
# of the rows, columns, and elements in a 3x3 matrix


def calculate(list):
    matrix = np.array(list)
    try:
        matrix = matrix.reshape(3, 3)
    except ValueError:
        raise ValueError("List must contain nine numbers.")
    dic = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }
    dic['mean'] = [np.mean(matrix, axis=0).tolist(), np.mean(
        matrix, axis=1).tolist(), np.mean(matrix).tolist()]
    dic['variance'] = [np.var(matrix, axis=0).tolist(), np.var(
        matrix, axis=1).tolist(), np.var(matrix).tolist()]
    dic['standard deviation'] = [np.std(matrix, axis=0).tolist(), np.std(
        matrix, axis=1).tolist(), np.std(matrix).tolist()]
    dic['max'] = [np.max(matrix, axis=0).tolist(), np.max(
        matrix, axis=1).tolist(), np.max(matrix).tolist()]
    dic['min'] = [np.min(matrix, axis=0).tolist(), np.min(
        matrix, axis=1).tolist(), np.min(matrix).tolist()]
    dic['sum'] = [np.sum(matrix, axis=0).tolist(), np.sum(
        matrix, axis=1).tolist(), np.sum(matrix).tolist()]
    return dic
