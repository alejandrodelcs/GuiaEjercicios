#!/usr/bin/env python3
numero_1 = int(input('Ingrese numero: '))
numero_2 = int(input('Ingrese otro numero: '))

while numero_1 != 0 and numero_2 != 0:
    mayor = numero_2
    if numero_1 > numero_2:
        mayor = numero_2
        print('mayor: ', mayor)
        print('menor: ', numero_2)
        
    else:
        print('mayor: ', mayor)
        print('menos: ', numero_1)
    numero_1 = int(input('Ingrese numero: '))
    numero_2 = int(input('Ingrese otro numero: '))


'''me parece que esta incorrecto, igual lo pensé y es medio un embole porque llegado a esta parte 
lo indicado sería hacerlo con una lista o tupla paso ejercicio 6'''