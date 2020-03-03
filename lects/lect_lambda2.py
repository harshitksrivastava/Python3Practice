from functools import reduce
nums = [3, 2, 5, 6, 7, 8, 9, 1]


# def is_even(n):
#     return n % 2 == 0


evens = list(filter(lambda a: a % 2 == 0, nums))
even_double = list(map(lambda a: a * 2, evens))
even_triple = dict(zip(evens, list(map(lambda a: a*2, evens))))
print(evens)
print('id of evens', id(evens))
print('id of even_double', id(even_double))
print('even_doubles', even_double)
sum = reduce(lambda a, b: a+b, even_double)
print(sum)
print(even_triple)