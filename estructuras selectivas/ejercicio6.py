#!/usr/bin/env python3

numero = int(input('Ingrese un numero: '))

numero_2 = int(input('Ingrese el numero el cual quiera saber si es divisor: '))

if numero%numero_2 == 0:
    print('el numero {} es divisor de {}'.format(numero_2,numero))
else:
    print('el numero {} NO es divisor de {}'.format(numero_2,numero))