
#Strings
# basics
'hello'
"hello"
"I'm a star"

# indexing
mystr = 'wqertyuiop'
print(mystr)
print(mystr[0])
print(mystr[-1])

# slicing
# 2nd to last
print(mystr[2:])
#from 0 to upto 3 but not including 3
print(mystr[:3])
#from 2 to upto 5 but not including 5
print(mystr[2:5])
#whole string is printed
print(mystr[:])
#whole string with diff of 2 (every second character)
print(mystr[::2])



# basic methods
# Strings are immutable
# to uppper case
mystr.upper()
# to lower case
mystr.lower()
# .capitalize()
# .split()


# print formatting
x = "Insert another string into here:{}".format("INSERT ME!")
print(x)
x = "{} Insert another string into here:{}".format("Hello","INSERT ME!")
