#!/usr/bin/env python3

numero_1 =  int(input('Ingrese numero: '))
numero_2 = int(input('Ingrese otro numero: '))

suma = numero_1+numero_2
multiplicacion=numero_1*numero_2
division=numero_1/numero_2

print('Menu')
print('1)Suma\n2)Multiplicacion\n3)division')
opcion = int(input('Ingrese opcion: '))
if opcion == 1:
    print(suma)
elif opcion == 2:
    print(multiplicacion)
elif opcion == 3:
    print(division)