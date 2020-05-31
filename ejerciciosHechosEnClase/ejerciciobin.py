#!/usr/bin/env python3

def es_binario(cadena):
    posicion = 0
    n = 0
    '''if len(cadena) == 0:
        binario = False

    while binario and n < len(cadena)-1:
        if cadena[n] != "0" or cadena[n] != "1":
            binario = False
        n += 1'''

    while (posicion < len(cadena) and (cadena[posicion] in "01"):
            posicion += 1
    return posicion == len(cadena) > 0


def main():
    binario = input('Ingrese numero binario: ')
    resultado = es_binario(binario)
    print('Es binario: {} '.format(resultado))
            
main()
