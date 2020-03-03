# factorial using memoization without decorators
"""use this command on terminal "python -m cProfile factorial.py" to see the difference"""

# def fact(number):
#     if number == 0:
#         return 1
#     else:
#         return number * fact(number - 1)

#
# if __name__ == "__main__":
#     num = int(input("enter the number"))
#     print("factorial is", fact(num))


memory = {}


def fact(number):
    if number not in memory:
        if number == 0:
            memory[number] = 1
        else:
            memory[number] = number * fact(number - 1)
    return memory[number]


if __name__ == "__main__":
    num = int(input("enter the number"))
    print("factorial is", fact(num))
    print("factorial is", fact(num+1))
    print("factorial is", fact(num+8))
