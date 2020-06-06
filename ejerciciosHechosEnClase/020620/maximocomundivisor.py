#!/usr/bin/env python3

def mcd(num1,num2):
    if num1%num2 == 0: return num2
    return mcd(num2, num1%num2)

print(mcd(56,104))