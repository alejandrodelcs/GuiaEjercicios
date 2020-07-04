#!/usr/bin/env python3
'''
Escribir una función que reciba una cadena de caracteres alfanuméricos y devuelva la cantidad de 
caracteres alfabéticos (letras) que hay en la cadena.

Debe validar que lo recibido sea una cadena formada sólo por números y/o letras, si no lo fuera, la función 
debe devolver -1.

Deberá comprobar el correcto funcionamiento, mediante los siguientes casos de prueba usando la librería 
doctest.

Para "Algoritmos1", debe devolver 10
Para "Ejercicio1", debe devolver 9
Para "z", debe devolver 1
Para "Algoritmos 1", debe devolver -1
Para "", debe devolver -1
Para "+*ab", debe devolver -1
Para "2por1", debe devolver 3
Para "01101011110", debe devolver 0

INCLUÍ EL ENUNCIADO QUE TE HA TOCADO, en el programa como comentario inicial, seleccionado y pegando todo 
el texto.

NOMBRA TU ARCHIVO DE LA SIGUIENTE FORMA: padrón_apellido_ej1.py  reemplazando padrón por tu padrón y 
apellido, por tu apellido

'''

def charCount(cadena):
    '''
    >>> charCount("Algoritmos")
    10
    >>> charCount("Ejercicio1")
    9
    >>> charCount("z")
    1
    >>> charCount("Algoritmos 1")
    -1
    >>> charCount("")
    -1
    >>> charCount("+*ab")
    -1
    >>> charCount("2por1")
    3
    >>> charCount("01101011110")
    0
    '''
    cont = 0

    if cadena.isalnum():
        for letra in cadena:
            if letra.isalpha():
                cont += 1
    else:
        cont = -1

    return cont 

import doctest
doctest.testmod()


