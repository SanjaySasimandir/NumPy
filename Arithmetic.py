import numpy as np
arr = np.arange(1, 10)  # [1 2 3 4 5 6 7 8 9]

print(arr + 2)  # [ 3  4  5  6  7  8  9 10 11] Addition
print(arr - 2)  # [-1  0  1  2  3  4  5  6  7] Subtraction
print(arr * 2)  # [ 2  4  6  8 10 12 14 16 18] Multiplication
print(arr / 2)  # [0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5] Division
print(arr % 3)  # [1 2 0 1 2 0 1 2 0] Remainder

print(np.sqrt(arr))
# [1.         1.41421356 1.73205081 2.         2.23606798 2.44948974 2.64575131 2.82842712 3.        ]
