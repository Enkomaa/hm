import numpy as np
A = np.arange(1, 101, 1)
print(np.sum(A[A % 2 == 0]))