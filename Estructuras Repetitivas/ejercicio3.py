#!/usr/bin/env python3
acum = 0

num = int(input('Ingrese un numero: '))

if num !=0:
    while num!=0:
        acum = acum + num
        print('\nSuma parcial: ', acum)
        num = int(input('\ntermina con cero\nIngrese un numero: '))
        
else:
    print('Suma Parcial: 0')