#!/usr/bin/env python3

def digitos_adyacentes(cadena):
    pos = 0
    adyacente = False
    while pos<len(cadena) and adyacente == False:
        if (cadena[pos:pos+2]).isnumeric() == True and cadena[pos:pos+1] == cadena[pos+1:pos+2]:
            adyacente = True 
        pos += 1
    return adyacente


def secuencia_ordenada(cadena):
    cadena_ord =  "".join(sorted(cadena))
    cadena_ord_dec = "".join(reversed(cadena_ord))
    cadena_sin_dup = "".join(sorted(set(cadena.lower())))
    ordenado = False

    if cadena.isnumeric() == True and (cadena_ord == cadena or cadena_ord_dec == cadena):
        ordenado =  True
    elif cadena.isdigit() == False and cadena_sin_dup in cadena:
        ordenado = True
    elif cadena.isdigit() == False and cadena_sin_dup[::-1] in cadena:
        ordenado = True
        
    return ordenado

def contar_digitos(cadena):
    cont = 0
    if secuencia_ordenada(cadena) == False and digitos_adyacentes(cadena) == False:
        for caracter in cadena:
            if caracter.isdigit():
                cont += 1
    else:
        cont = -1
    return cont

def validar_clave(clave):
    """ Casos de Prueba:

    >>> validar_clave("florencia25")
    False
    >>> validar_clave("24aei2")
    False
    >>> validar_clave("eAEIOui")
    False
    >>> validar_clave("123456")
    False
    >>> validar_clave("97532")
    False
    >>> validar_clave("99756")
    False
    >>> validar_clave("344283")
    False
    >>> validar_clave("639210")
    True
    >>> validar_clave("23451")
    True
    >>> validar_clave("53131")
    True
    >>> validar_clave("4aI8xS1z4")
    True
    >>> validar_clave("andresito50")
    False
    >>> validar_clave("445566778899")
    False

    """
    if contar_digitos(clave)>=4 and contar_digitos(clave)<=8:
        valido = True
    else:
        valido = False 

    return valido

import doctest
doctest.testmod()

