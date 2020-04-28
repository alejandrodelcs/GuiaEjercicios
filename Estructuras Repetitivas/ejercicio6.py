#!/usr/bin/env python3

suma = 0

numero_1 = int(input('Ingrese un numero: '))
numero_2 = int(input('Ingrese otro numero: '))

for i in range(1,numero_2+1):
    print(i)
    suma = suma + numero_1

print('{} X {} = {}'.format(numero_1,numero_2,suma))