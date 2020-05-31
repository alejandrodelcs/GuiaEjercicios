#!/usr/bin/env python3

def cadena_invertida(cadena):
    cadena_invertida = cadena[::-1]

    return cadena_invertida


def main():
    palabra = input('Ingrese palabra: ')
    print('palabra invertida: {}'.format(cadena_invertida(palabra)))


main()