#!/usr/bin/env python3.8

numero = int(input('Ingrese un numero: '))
divisor = 2
cant_primos = 0

for i in range(1,numero+1):
    while ((i % divisor) != 0) and (divisor <= i/2):
        divisor += 1
    if (i >1 ) and (divisor > i/2):
        print('Es primo: ', i)
        cant_primos += 1
        
print('cantidad de primos: ', cant_primos)
