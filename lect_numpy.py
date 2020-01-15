from numpy import *


arr = array([1, 2, 3, 4, 5])                # by default values are taken as int
print(arr)
print("type of arr is " + str(type(arr)))
print("type of arr is {}".format(arr.dtype))


arr_linspace = linspace(0, 15, 16)
print(arr_linspace)
print("type of arr_linspace is "+str(type(arr_linspace)))
print("type of arr_linspace is "+str(arr_linspace.dtype))


arr_arange  = arange(0, 10, 2)              # excludes the last stop value just as range() function
print('the elements using arange {}'.format(arr_arange))


arr_logspace = logspace(1, 10, 10, base=2)
print('the elements {}'.format(arr_logspace))


arr_zeros = zeros(5)
arr_zeros_int = zeros(5, int)
print('the elements are {}'.format(arr_zeros))
print('the elements are {}'.format(arr_zeros_int))


arr_ones = ones(5)
arr_ones_int = ones(5, int)
print('the elements are {}'.format(arr_ones))
print('the elements are {}'.format(arr_ones_int))
