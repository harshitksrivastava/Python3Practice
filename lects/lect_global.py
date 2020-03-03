a = 10


def something():
    a = 9
    x= globals()['a']
    print(id(x))
    print('id of local a', id(a))
    print(id(globals()['a']))
    print('inside soemthing before changing',x)
    x = 5  # this does not change the global value of a
    print(id(x))
    globals()['a'] = 15       #this does change the global value of a
    print(id(x))
    print(id(a))
    print(id(globals()['a']))
    print('inside', a)


something()
print('outside', a)
