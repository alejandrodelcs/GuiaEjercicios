#!/usr/bin/env python3

"""
Escribir una funcion para validar una nueva clave de acceso.
La función debera recibir una cadena de caracteres, que contendra la clave
candidata, ingresada por el usuario; y devolvera True o False, dependiendo de
si cumple con las condiciones establecidas.

La clave debe:
- Tener como minimo entre 4 y 8 digitos numericos
- Los digitos adyacentes no pueden ser iguales
- La clave no puede formar una secuencia ordenada creciente o decreciente
"""

def digitos_adyacentes(clave):
    pos = 0
    valido = True
    while pos<len(clave) and valido == True:
        if clave[pos:pos+1] == clave[pos+1:pos+2]:
            valido = False
        else:
            valido = True 
        pos += 1
    return valido

def clave_ordenada(clave):
    ordenado = False 

    if digitos_adyacentes(clave):
        num_cadena = [x for x in clave if x.isdigit()]
        let_cadena = [y for y in set(clave.lower()) if y.isalpha()]
    
        if "".join(num_cadena) in clave or "".join(let_cadena) in clave:
            ordenado = True
    return ordenado

def validar_clave(clave):
    """
    >>> validar_clave("Alejandro1234")
    False
    >>> validar_clave("aabbcc1122")
    False
    >>> validar_clave("7Alej01")
    True
    >>> validar_clave("xI3b8vA")
    True
    """
    
    if len(clave) >= 4 and len(clave) <= 8 and clave_ordenada(clave) == False:
        valido = True
    else:
        valido = False

    return valido

import doctest
doctest.testmod()
