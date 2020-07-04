#!/usr/bin/env python3
import unicodedata
"""
Escribir una función que reciba una cadena de caracteres alfanuméricos y 
devuelva una cadena formada por las vocales que hay en la cadena, en el orden que aparecen, sin repetirlas .
Estén o no acentuadas, ó esten en mayúscula ó minúscula, sólo deben aparecer una vez (ver los casos de prueba).

Validar que la cadena recibida esté formada sólo por caracteres alfanuméricos, 
caso contrario, devovler '*' (caracter asterisco).

Deberá comprobar el correcto funcionamiento, mediante los siguientes casos de prueba usando 
la librería doctest.

Para "Algoritmos y Programación", debe devolver '*'
Para "Programación1", debe devolver 'oai'
Para "", debe devolver '*'
Para "+*ab", debe devolver '*'
Para "AÉREO", debe devolver 'AÉO'
Para "Aerolíneas", debe devolver 'Aeoí'
Para "-P-f/7", debe devolver '*'
"""
            

def vocales_cadena(cadena):
    """
    >>> vocales_cadena("Algoritmos y Programación")
    *
    >>> vocales_cadena("Programación1")
    oai
    >>> vocales_cadena("")
    *
    >>> vocales_cadena("+*ab")
    *
    >>> vocales_cadena("AÉREO")
    AÉO
    >>> vocales_cadena("Aerolíneas")
    Aeoí
    >>> vocales_cadena("-Pf/7")
    *
    """
    vocales = ''
    palabra = ''
    if cadena.isalnum():
        for letra in cadena:
            if letra in 'aeiouáéíóúAEIOUÁÉÍÓÚ':
                vocales += letra
    else:
        vocales = '*'
    return vocales
    
print(vocales_cadena("AÉREO"))
