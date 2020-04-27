#!/usr/bin/env python3


print('Menu')
print('Opcion1\nOpcion2\nOpcion3\nOpcion4')

opcion = int(input('Ingrese opcion: '))

if opcion>=1 and opcion<=4: 
    print('opcion correcta')
else:
    print('opcion incorrecta')