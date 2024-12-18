import numpy as np

def prod_matrix(A: np.array, B: np.array) -> np.array:
    return A.dot(B)
A = np.array([[1, 2],
            [3, 4]])
B = np.array([[1, 1],
            [7, 8]])

print(prod_matrix(A, B))