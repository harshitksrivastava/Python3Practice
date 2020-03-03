# multi dimensional
from numpy import *

arr1 = array([
        [1, 2, 3, 4],
        [5, 6, 7, 8]
            ])

arr2 = arr1.flatten()

m = matrix(arr1)
print(m)
print(arr1)

m1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
print(m1)
print(diagonal(m1))
m1[0, 0]=10
print(m1)
