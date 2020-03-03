#Lists
my_list = [1,2,3,4,5]

# list is mutable
# reassigment to a list
 my_list[0]='string'

 # adding to a list
  my_list.append(7);
  #or appending a new Lists
#know the diff
  my_list.append([5,6,7,8])
  my_list.extend([1,3,6,8,0])

# removing an item
  my_list.pop()
  my_list.pop(0)   # index

 #basic function
 #reverse,sort is inplace
 my_list.reverse()
 my_list.sort()

 #nested list
 my_list = [1,2,['x','y','z']]
 print(my_list[2][2])

 #list comprehension
 matrix = [[1,2,3],[4,5,6],[7,8,6]]
 first_col = [row[0] for row in matrix]
# o/p [1,4,7]
 print(first_col)
 
