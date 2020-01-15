# ODDS and EVENS
# class Sample:
#     pass
#
# x= Sample()
# print(type(x))

class Dog:

    # self keyword works likke this
    # breed is argument and value is passed through instantiation
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name


mydog = Dog('lab',"sammy")
print(mydog.breed)
print(mydog.name)

# CLASS ATTRIBUTE:
