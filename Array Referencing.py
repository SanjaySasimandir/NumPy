import numpy as np
arr = np.array([1, 2, 3, 4, 5])
newArr = arr.copy()
print(newArr)  # [1 2 3 4 5]
# .copy() to prevent the original data from change while modifying the copy
