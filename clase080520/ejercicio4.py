#!/usr/bin/env python3

def es_palindromo(cadena):
    '''
    >>es_palindromo("ana")
    True
    >>es_palindromo("los carros")
    False
    >>es_palindromo("luz azul")
    True
    >>es_palindromo("la ruta natural")
    True
    >>es_palindromo("tu perro ha muerto por un tren")
    False
    '''
    if cadena.isalnum() == False:
        resultado = False
    elif len(cadena) <= 2:
        resultado = False
    elif ("".join(cadena.split()))[:len(cadena)] != ("".join(cadena.split()))[::-1]:
        resultado == False
    else:
        resultado = True 

    return resultado

import doctest 
doctest.testmod()