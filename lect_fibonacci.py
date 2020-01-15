

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n < 0:
        print('invalid input')
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a+b
            a, b = b, c
            # if c > n:                 # this condition gives all the fibonacci under the entered value
            #     break
            print(c)


z=int(input('Enter the number'))
fib(z)
