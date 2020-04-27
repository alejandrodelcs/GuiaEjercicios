#!/usr/bin/env python3
"""x = 3
if (x < 5):
    x = x + 1
if (x == 5):
    x = x + 2
if (x > 5):
    x = x + 3
print(x)"""

x = 4
if (x < 5):
    x = x + 1
elif (x == 5):
    x = x + 2
else:
    x = x + 3
print(x)

'''La diferencia entre es que en el primero la condición del if se va a evaluar en cada linea de codigo, mientras
que en el otro lo evalua una sola vez, para luego descartar las demas opciones.'''
