from numpy import *

arr = array([1, 2, 3, 4])
arr2 = arr + 5
# arr2 = append(arr2, [10])
arr3 = arr + arr2
print(arr3)


arr4 = arr
print(id(arr4))             # 140597859647536
print(id(arr))              # 140597859647536


""" if we want to have copy of arr in different location then use .view() """


arr5 = arr.view()
print(id(arr4))             #
print(id(arr))              # 

