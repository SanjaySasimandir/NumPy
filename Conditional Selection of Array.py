import numpy as np
arr = np.arange(0, 50, 5)
print(arr)  # [ 0  5 10 15 20 25 30 35 40 45]

print(arr > 35)
# [False False False False False False False False  True  True]

print(arr[arr > 35])  # [40 45]
