# array calculations and operations

import numpy as np

a = np.array([range(4), range(10,14)])
b = np.array([2, -1, 1, 0])

print a
print b

ab = a*b

print ab

b1 = b*100

print b1

b2 = b*100.0

print b2

print b1 == b2

print b1.dtype, b2.dtype

#array comparisons

arr = np.array([range(0,10)])

print arr

print arr <3

condition = np.logical_or(arr < 3, arr > 8)
newarr = np.where(condition, arr * 5, arr * -5)

print newarr

