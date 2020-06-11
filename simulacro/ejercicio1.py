#!/usr/bin/env python3

"""
Escribir una funcion para validar una nueva clave de acceso.
La funcion debera recibir una cadena de caracteres, que contendra la clave
candidata, que fue ingresada por el usuario; y devolvera True o False,
dependiendo de si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud de entre 8 y 12 caracteres inclusive
- Solo puede estar formada por letras y numeros
- Debe contener al menos una letra mayuscula, una letra minuscula y 1 numero
"""
def validar_minusculas_mayusculas(clave):
    num_cadena = [x for x in clave if x.isdigit()]
    let_cadena = [y for y in set(clave.lower()) if y.isalpha()]
    
    if len(num_cadena) > 0 and len(let_cadena) > 0:
        valido = True
    else:
        valido = False

    return valido

def validar_caracteres(clave):
    cont = 0
    if validar_minusculas_mayusculas(clave):
        for letra in clave:
            if letra.isdigit() == True or letra.isupper() == True or letra.islower() == True:
                cont += 1
    return cont

def validar_clave(clave):
    """
    >>> validar_clave("12456789")
    False
    >>> validar_clave("Alejandro")
    False
    >>> validar_clave("Alejandr0321")
    True
    >>> validar_clave("pepeGrillo5")
    True
    """
    cont = validar_caracteres(clave)

    if len(clave) >= 8 and len(clave) <= 12 and cont > 1:
        valido = True
    else:
        valido = False 

    return valido 

import doctest
doctest.testmod()