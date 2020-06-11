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

def digitos_adyacentes(cadena):
    pos = 0
    adyacente = False
    while pos<len(cadena) and adyacente == False:
        if (cadena[pos:pos+2]).isnumeric() == True and cadena[pos:pos+1] == cadena[pos+1:pos+2]:
            adyacente = True 
        pos += 1
    return adyacente


def secuencia_ordenada(cadena):

    num_cadena = [x for x in cadena if x.isdigit()]
    let_cadena = [y for y in set(cadena.lower()) if y.isalpha()]
    
    if len(num_cadena) != 0 and (sorted(num_cadena) == num_cadena or sorted(num_cadena)[::-1] == num_cadena):
        ordenado = True
    elif len(let_cadena) != 0 and (sorted(let_cadena) == let_cadena or sorted(let_cadena)[::-1]== let_cadena):
        ordenado = True
    else:
        ordenado = False 
    
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
    >>> validar_clave("Alejandro5013")
    True
    >>> validar_clave("Argentina2001")
    False
    >>> validar_clave("Ezequiel1234")
    False
    >>> validar_clave("MedcbaMmm")
    False
    """
    if contar_digitos(clave)>=4 and contar_digitos(clave)<=8:
        valido = True
    else:
        valido = False 

    return valido

import doctest
doctest.testmod()




