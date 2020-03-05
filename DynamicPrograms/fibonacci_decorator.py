# fibonacci using memoization with decorators in a non-pythonic way
def memoize(f):
    fib_cache = {}

    def inner(num):
        if num not in fib_cache:
            fib_cache[num] = f(num)
        return fib_cache[num]
    return inner


def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


if __name__ == '__main__':
    fib = memoize(fib)
    number = int(input("enter the number \n"))
    print(fib(number))
    print(fib(number+1))
    print(fib(number+2))
    print(fib(number+3))


# =====================================================================================================================
# fibonacci using memoization with decorators in a pythonic way
# def memoize(f):
#     fib_cache = {}
#
#     def inner(num):
#         if num not in fib_cache:
#             fib_cache[num] = f(num)
#         return fib_cache[num]
#     return inner
#
#
# @memoize
# def fib(num):
#     if num <= 1:
#         return num
#     else:
#         return fib(num - 1) + fib(num - 2)
#
#
# if __name__ == '__main__':
#     number = int(input("enter the number \n"))
#     print(fib(number))
#     print(fib(number+1))
#     print(fib(number+2))
#     print(fib(number+3))
