#!/usr/bin/env python3

"""
Escribir una funcion para validar una nueva clave de acceso.
La funcion debera recibir una cadena de caracteres, que contendra la clave
candidata, ingresada por el usuario; y devolvera True o False, dependiendo de
si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud de entre 6 y 10 caracteres inclusive
- Solo puede estar formada por vocales (no acentuadas) y digitos pares
- Debe estar formada por una combinacion cualquiera de:
    vocales mayusculas y digitos pares, o
    vocales minusculas y digitos pares, o
    vocales minusculas y mayusculas, o
    vocales minusculas, mayusculas y digitos pares
"""


def validacion_vocal_dig_pares(clave):
    pos = 0
    pos_num = 0
    valido = True

    if len(clave) >= 6 and len(clave) <= 10:
        num_cadena = [x for x in clave if x.isdigit()]
        while pos<len(clave) and pos_num < len(num_cadena) and valido == True :
            if clave[pos] in "aeiouAEIOU" and int("".join(num_cadena[pos_num])) % 2 == 0:
                valido = True
            else:
                valido = False
            pos += 1
            pos_num += 1
    else:
        valido = False
    return valido
    
def validar_clave(clave):
    """
    >>> validar_clave("avenida46")
    False
    >>> validar_clave("AeIoD013")
    False
    >>> validar_clave("AeIo846")
    True
    >>> validar_clave("AeooIi48")
    True
    """
    if validacion_vocal_dig_pares(clave):
        valido = True
    else:
        valido = False
        
    return valido

import doctest
doctest.testmod()