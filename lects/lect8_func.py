# Filter
mylist=[1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 ==0


evens = filter(even_bool,mylist)
# above result has to be printed as listed
print(list(evens))



#Lambda Expression
#anonymous function
even = filter(lambda num:num%2 ==0,mylist)
print(list(evens))


# in operator
