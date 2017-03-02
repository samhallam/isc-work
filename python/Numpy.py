# Introduction to Numpy arrays

import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]

a1 = np.array(x, np.int32)
a2 = np.array(x, np.float32)

print a1.dtype
print a2.dtype

# Creating arrays in different ways

a = np.zeros ((2,3,4))
print a

b= np.ones((2,3,4))
print b

c= np.arange((10))
print c

#indexing and slicing arrays

a = np.array([2,3.2,5.5,-6.4,-2.2, 2.4])

print a[1]
print a[1:4]

b = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4], 
              [1, 22, 4, 0.1, 5.3, -9],
              [3, 1, 2.1, 21, 1.1, -2]])

print b[:,3]
print b[1:4, 0:4]
print b[1: , 2]










