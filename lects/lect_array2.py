from array import *

arr = array('i', [])
n = int(input('Enter the length of the array'))

for i in range(n):
    x = int(input("enter the number"))
    arr.append(x)

print(arr)
val = int(input('Enter the value for search'))

k = 0
for i in arr:
    if i == val:
        print(k)
    k += 1

try:
    print(arr.index(val))
except ValueError:
    print("number does not exist")


