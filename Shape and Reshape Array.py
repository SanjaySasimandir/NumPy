import numpy as np
a = np.zeros(6, np.int8)
a = a.reshape(2, 3)
print(a)
'''
[[0 0 0]
 [0 0 0]] 2x3 Matrix
'''
print(a.shape)  # (2, 3) Prints dimension of matrix
