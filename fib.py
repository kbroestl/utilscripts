#! /usr/bin/env python

"""
[1, 2, 3, 5, 8, 13] should be the end result NOT the total
"""

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

def fibonacci(max):
    a, b = 0, 1
    while a <= max:
        yield a
        a,b = b, a+b

# for n in fibonacci(6):
#     print n,
# 
# print "\n", factorial(6)
# 
# def fib(n):
#     return n if n < 2 else fib(n-2) + fib(n-1)
#  
__fib_cache = {}
def fib(n):
    if n in __fib_cache:
        return __fib_cache[n]
    else:
        __fib_cache[n] = n if n < 2 else fib(n-2) + fib(n-1)
        return __fib_cache[n]

for n in map(fib, range(0,100)):
    print n,
# 
# for n in fib(10):
#     print n