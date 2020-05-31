#!/usr/bin/env python3


def es_diptongo(cadena):
    """
    >>> es_diptongo("aire")
    True
    >>> es_diptongo("perro")
    False
    >>> es_diptongo("agua")
    True
    >>> es_diptongo("caiman")
    True
    >>> es_diptongo("lagartija")
    False
    >>> es_diptongo("mexico")
    False
    """
    diptongo = ['ia','ie','io','ua', 'ue','uo']
    n=0
    resultado = False
    while n<len(diptongo)-1 and resultado == False:
        if (diptongo[n] in cadena) or ((diptongo[n])[::-1] in cadena):
            resultado = True
        n +=1
    return resultado

import doctest
doctest.testmod()

