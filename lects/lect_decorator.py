def div(a, b):
    return a / b


def sample_div(func):
    def inner(a, b):
        print('This is inside the sample_div')
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


f = sample_div(div)
result = f(2, 4)
print(result)
