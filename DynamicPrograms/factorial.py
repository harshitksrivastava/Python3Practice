# factorial using recursion without Dynamic Programming
# def fact(number):
#     if number == 0:
#         return 1
#     else:
#         return number * fact(number - 1)


# =====================================================================================================================
# factorial using recursion with Dynamic Programming (Memoization)
def fact(number):
    memory = {}
    if number not in memory:
        if number == 0:
            memory[number] = 1
        else:
            memory[number] = number * fact(number - 1)
    return memory[number]


# =====================================================================================================================
# Main function call
if __name__ == "__main__":
    num = int(input("enter the number"))
    print("factorial is", fact(num))
    print("factorial is", fact(num + 1))
    print("factorial is", fact(num + 8))
