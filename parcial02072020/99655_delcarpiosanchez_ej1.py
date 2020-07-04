#!/usr/bin/env python3

"""
Escribir una función que reciba una cadena de caracteres y devuelva una tupla con  la cantidad de vocales encontradas para cada una de las 5 vocales.
No debe diferenciar entre letras mayúsculas, minúsculas, ni vocales acentuadas.
Cada posición en la tupla, corresponde a una de las vocales, vea los casos de prueba.
No puede utilizar para esta solución, ninguno de los métodos provistos por el lenguaje para el tratamiento de cadenas, como: count, find, index, rindex, etc.

Deberá comprobar el correcto funcionamiento, mediante los siguientes casos de prueba usando la librería doctest.

Para ("aeiou") debe devolver (1,1,1,1,1)
Para ("") debe devolver (0,0,0,0,0)
Para ("Yo los conozco, son ocho los monos!") debe devolver (0,0,0,11,0)
Para ("MURCIÉLAGO") debe devolver (1,1,1,1,1)
Para ("3004924024004232-1") debe devolver (0,0,0,0,0)
Para ("AaáEeIiOoUuú") debe devolver (3,2,2,2,3)
"""

def contar_vocales(cadena):
    """
    >>> contar_vocales("aeiou")
    (1, 1, 1, 1, 1)
    >>> contar_vocales("")
    (0, 0, 0, 0, 0)
    >>> contar_vocales("Yo los conozco, son ocho los monos!")
    (0, 0, 0, 11, 0)
    >>> contar_vocales("MURCIÉLAGO")
    (1, 1, 1, 1, 1)
    >>> contar_vocales("3004924024004232-1")
    (0, 0, 0, 0, 0)
    >>> contar_vocales("AaáEeIiOoUuú")
    (3, 2, 2, 2, 3)
    """
    
    cont_a =  cont_e = cont_i = cont_o = cont_u = 0
    for letra in cadena:
        if letra in 'aAáÁ':
            cont_a += 1 
        elif letra in 'eEÉé':
            cont_e += 1
        elif letra in 'iIÍí':
            cont_i += 1
        elif letra in 'oOÓó':
            cont_o += 1
        elif letra in 'uUÚú':
            cont_u += 1
    return cont_a,cont_e,cont_i,cont_o,cont_u

print(contar_vocales("AaáEeIiOoUuú"))




