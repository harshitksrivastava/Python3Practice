def Person(name, **kwargs):
    print(name)
    for i, j in kwargs.items():
        print(i, ":", j)


Person('harshit', place='lucknow', age=18)
