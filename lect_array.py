from array import *

vals = array('i', [1, 2, 3, 4])

print(vals.buffer_info())
for e in vals:
    print(e)


new_arr = array(vals.typecode, (a for a in vals))

for e in new_arr:
    print(e)
print(id(vals))
print(id(new_arr))
print(type(new_arr))  # <class 'array.array'>
"""arr = vals + 5        # can only append to the array in array module, hence not possible
   print(arr)            # above operation is allowed in numpy for array"""
