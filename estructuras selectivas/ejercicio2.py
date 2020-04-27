#!/usr/bin/env python3
numero_1 = float(input('Ingrese un numero: '))
numero_2 = float(input('Ingrese otro numero: '))

if numero_1 > numero_2:
    print('el numero {} es mayor a {}'.format(numero_1,numero_2))
else:
    print('el numero {} es mayor a {}'.format(numero_2,numero_1))