# interrogating and manipulating arrays

import numpy as np

arr = np.array ([range(4), range(10, 14)])

print arr
print arr.shape
print arr.size
print arr.max()
print arr.min()

# generating new arrays by modifying our array


print np.reshape(arr, (2,2,2))
print np.transpose(arr)
print np.ravel(arr)
print arr.astype(np.float64)



