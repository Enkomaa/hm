import numpy as np
A = np.arange(1, 10)
A = A.reshape(3, 3)
A_transpan = A.T
print(A_transpan)
print(np.sum(A))