#!/usr/bin/env python3

def tabla_valores():
    for c in range(0,201,10):
        f = 9/5*c+32
        c = 5/9*(f-32)
        print('|Fahrenheit {} | Celsius {}|'.format(f,c))

tabla_valores()