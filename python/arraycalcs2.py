# implement a mathematical function that works on arrays

import numpy as np

def calcabswnd(u, v, minmag=0.1):

    abswnd = ((u**2) +(v**2))**0.5
    output = np.where( abswnd > minmag, abswnd, minmag)
    return output

u = np.array([[4,5,6], [2,3,4]])
v= np.array([[2,2,2], [1,1,1]])

print u
print v

print calcabswnd(u,v)
