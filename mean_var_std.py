import numpy as np

def calculate(list_input):
    if len(list_input) < 9:
        raise ValueError("List must contain nine numbers.")
    matrix_list = np.array(list_input)
    matrix_list = matrix_list.reshape(3,3)
    return {'mean' : [np.mean(matrix_list, axis=0).tolist(), np.mean(matrix_list, axis=1).tolist(), np.mean(list_input).tolist()],
    'variance' : [np.var(matrix_list, axis=0).tolist(), np.var(matrix_list, axis=1).tolist(), np.var(list_input).tolist()],
    'standard deviation' : [np.std(matrix_list, axis=0).tolist(), np.std(matrix_list, axis=1).tolist(), np.std(list_input).tolist()],
    'max' : [np.max(matrix_list, axis=0).tolist(), np.max(matrix_list, axis=1).tolist(), np.max(list_input).tolist()],
    'min' : [np.min(matrix_list, axis=0).tolist(), np.min(matrix_list, axis=1).tolist(), np.min(list_input).tolist()],
    'sum' : [np.sum(matrix_list, axis=0).tolist(), np.sum(matrix_list, axis=1).tolist(), np.sum(list_input).tolist()]}
