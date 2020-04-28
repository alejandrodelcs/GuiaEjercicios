#!/usr/bin/env python3.8

cont = 0

numero = int(input('Ingrese un numero: '))

for i in range(1,numero+1):
    if numero%i == 0:
        cont = cont +1 

if cont == 2 or numero == 0:
    print('el numero es primo')
else:
    print('el numero no es primo')
