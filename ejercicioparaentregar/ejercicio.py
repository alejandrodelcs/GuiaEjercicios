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

===============================================================================
Aqui coloca tu Padron:
Aqui coloca tu Apellido y Nombre:
-------------------------------------------------------------------------------
"""
def clave_ordenada(clave):
    clave_ordenada_asc = sorted(list(set(clave.lower())))
    clave_ordenada_desc = sorted(list(set(clave.lower())), reverse=True)
    if "".join(clave_ordenada_asc) in clave.lower():
        ordenado = True
    elif "".join(clave_ordenada_desc) in clave.lower():
        ordenado = True
    else:
        ordenado = False 
    return ordenado

def dig_adyacentes(clave):
    pos = 0
    igual = False
    while pos<len(clave)-1 and igual==False:
        if clave[pos] == clave[pos+1]:
            igual = True
        pos += 1
    return igual

def dig_max_min(clave):
    lista_num = ['0','1','2','3','4','5','6','7','8','9']
    pos = 0
    cont = 0
    dig_igual = False
    while pos<len(clave) and dig_igual == False:
        if clave[pos] in lista_num:
            cont += 1
        if cont > 4 and cont < 8:
            dig_igual = True
        pos += 1
    return dig_igual


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
    >>> validar_clave("247851")
    True
    >>> validar_clave("andres202145")
    True
    >>> validar_clave("lim0n3s")
    False
    >>> validar_clave("33aabbao")
    False

    """
    if dig_adyacentes(clave) == True:
        valido=False
    elif dig_max_min(clave) == False:
        valido=False
    elif clave_ordenada(clave) == True:
        valido = False
    else:
        valido = True
    return valido


import doctest
doctest.testmod()
