#!/usr/bin/env python3.8

numero = int(input('Ingrese un numero: '))
divisor = 2

while ((numero % divisor) != 0) and (divisor <= numero/2):
    divisor += 1
if (numero >1 ) and (divisor > numero/2):
    print('Es primo')
else:
    print('No es primo')
