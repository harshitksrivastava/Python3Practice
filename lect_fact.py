def fact(a):
    if a == 0:
        return 1
    else:
        return a * fact(a - 1)


x = int(input('Enter the number to find factorial'))
result = fact(x)
print(result)
