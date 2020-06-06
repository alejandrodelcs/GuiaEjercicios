#!/usr/bin/env python3

'''Ejercicio 2

Escribir una función que reciba una cadena de caracteres a validar,
y un segundo parámetro, que contenga una cadena con los caracteres válidos. 
La función debe devolver True, si la cadena a validar, está formada sólo por
caracteres válidos; en caso contrario, deberá devolver False.'''


def es_valido_el_caracter(cadena_usr, cadena_valida):
    pos = 0
    while (cadena_valida[pos] in cadena_usr) and (pos<len(cadena_usr)):
        pos += 1
    return pos == len(cadena_usr) > 0

def main():
    cadena_caracteres =  input('Ingrese primera cadena: ')
    cadena_usr =  input('Ingrese segunda cadena: ')
    resultado = es_valido_el_caracter(cadena_usr, cadena_caracteres)
    print('cadena ingresada: {}'.format(resultado))

main()