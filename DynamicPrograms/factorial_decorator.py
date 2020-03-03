# factorial using memoization with decorators in a non-pythonic way
def memoize(f):
    memory = {}

    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]

    return inner


def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


if __name__ == "__main__":
    number = int(input("Enter a number"))
    fact = memoize(fact)
    print("The factorial is ", fact(number))
    print("The factorial is ", fact(number + 8))

# ======================================================================================================================
# factorial using memoization with decorators in a pythonic way
# def memoize(f):
#     memory = {}
#
#     def inner(num):
#         if num not in memory:
#             memory[num] = f(num)
#         return memory[num]
#
#     return inner
#
#
# @memoize
# def fact(num):
#     if num == 0:
#         return 1
#     else:
#         return num * fact(num - 1)
#
#
# if __name__ == "__main__":
#     number = int(input("Enter a number"))
#     print("The factorial is ", fact(number))
#     print("The factorial is ", fact(number + 8))
