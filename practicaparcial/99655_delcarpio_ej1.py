#!/usr/bin/env python3

def contar_letras(palabra):
    cont = 0
    for letra in palabra:
        if letra.isalpha():
            cont+=1
    return cont

def validar_cadena_alfanumerica(palabra):
    if palabra.isalnum():
        valido = 0
    else:
        valido = -1
    return valido

def contar_palabra(palabra):
    """
    >>> contar_palabra("Algoritmos")
    10
    >>> contar_palabra("Ejercicio1")
    9
    >>> contar_palabra("z")
    1
    >>> contar_palabra("Algoritmo 1")
    -1
    >>> contar_palabra("")
    -1
    >>> contar_palabra("+*ab")
    -1
    >>> contar_palabra("2por1")
    3
    >>> contar_palabra("010010111")
    0

    """
    if validar_cadena_alfanumerica(palabra) == -1:
        valido = -1
    else:
        valido = contar_letras(palabra)
    return valido


import doctest 
doctest.testmod()