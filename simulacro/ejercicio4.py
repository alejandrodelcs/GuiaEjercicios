#!/usr/bin/env python3
"""
Escribir una funcion para validar una nueva clave de acceso.
La funcion deber recibir una cadena de caracteres, que contendra la clave
candidata, que fue ingresada por el usuario; y devolvera True o False,
dependiendo de si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud total de entre 4 y 10 caracteres
- Estar formada por igual cantidad de caracteres numericos y caracteres
  alfabeticos, y no puede contener ningun otro caracter.
- Los caracteres alfabeticos y numericos deben estar intercalados, no pueden
  haber dos letras consecutivas, ni dos digitos numericos consecutivos.
"""

def caracteres_intercalados(clave):
    pos = 0
    valido = True
    while pos<len(clave) and valido == True:
        if clave[pos:pos+1] == clave[pos+1:pos+2]:
            valido = False
        else:
            valido = True
        pos += 1
    return valido


def cantidad_caracteres(clave):
    valido = False
    if caracteres_intercalados(clave):
        num_cadena = [x for x in clave if x.isdigit()]
        let_cadena = [y for y in set(clave.lower()) if y.isalpha()]
        if len(num_cadena) == len(let_cadena):
            valido = True
        else:
            valido = False

    return valido


def cant_num(clave):
    cont_num = 0
    cont_letra = 0
    for letra in clave:
        if letra.isdigit():
            cont_num += 1
        elif letra.isalpha():
            cont_letra += 1
    print(cont_num,cont_letra)



def validar_clave(clave):
    """
    >>> validar_clave("aleE44")
    False
    >>> validar_clave("123465")
    False
    >>> validar_clave("Alejo52854")
    True
    >>> validar_clave("45AxI03D")
    True

    """
    if len(clave)>=4 and len(clave)<=10 and cantidad_caracteres(clave) == True:
        valido = True 
    else:
        valido = False

    return valido

