#!/usr/bin/env python3
def leer_lineas(archivo):
    l_temp =[]
    with open(archivo, "r") as archivo:
        for linea in archivo:
            linea = linea.rstrip('\n')
            l_temp.append(linea)
    return l_temp

def tabla_valores(archivo):
    with open(archivo, "a") as archivo:
        for c in range(0,201,10):
            f = 9/5*c+32
            c = 5/9*(f-32)
            archivo.write('|Fahrenheit {} | Celsius {}|\n'.format(f,c))

archivo = 'temperaturas.txt'
tabla_valores(archivo)
r = leer_lineas(archivo)