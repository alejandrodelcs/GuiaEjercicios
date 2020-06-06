#!/usr/bin/env python3

cache = {}

def fib_m(n):
    if n <= 1: return 1
    if n not in cache:
        cache[n] = fib_m(n-1) + fib_m(n-2)
    return cache[n]


print(fib_m(100))