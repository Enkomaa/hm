import numpy as np
def my_mse(A: np.array, B: np.array) -> np.array:
    C = A - B
    # print(C)
    C = C * C
    # print(C)
    return C.mean()

A = np.array([1, 2, 3])
B = np.array([1, 5, 3])

print(my_mse(A, B))