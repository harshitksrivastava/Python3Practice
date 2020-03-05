# fibonacci without recursion and without Dynamic Programming
def fib(num):
    a = 0
    b = 1
    while num - 2 >= 0:
        c = a + b
        (a, b) = (b, c)
        num -= 1
    return c


# =====================================================================================================================
# fibonacci with recursion and without Dynamic Programming
# def fib(num):
#     if num <= 1:
#         return num
#     return fib(num - 1) + fib(num - 2)
#

# =====================================================================================================================
# fibonacci with recursion and with Dynamic Programming(Memoization)
# def fib(num):
#     memory = {}
#     if num not in memory:
#         if num <= 1:
#             memory[num] = num
#         else:
#             memory[num] = fib(num - 1) + fib(num - 2)
#     return memory[num]


# =====================================================================================================================
# Main function call
if __name__ == '__main__':
    number = int(input("Enter fibonacci number \n"))
    print(fib(number))
    print(fib(number + 1))
    print(fib(number + 2))
    print(fib(number + 3))
