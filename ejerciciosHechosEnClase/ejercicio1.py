#!/usr/bin/env python3.8
factorial = 1
numero = int(input('Ingrese un numero: '))

if numero < 0:
    print('el numero ingresado no es valido')
else:
    for n in range(1,numero+1):
        factorial *= n
    print('el factorial es', factorial)