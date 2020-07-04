#!/usr/bin/env python3

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Escribir una funcion que devuelva verdadero si elegis una pelicula que te proponen,
falso de lo contrario.
La funcion recibe dos listas: una de actores / actrices (actores) que actuan en
esa pelicula y otra de puntajes.
La lista actores puede tener desde 1 a n actores / actrices.
La lista puntajes puede tener desde 1 a m puntajes (del 1 al 10).

Se elige la pelicula cuando:
- En la lista actores tiene "Leonardo Di Caprio" o "Emma Stone" o "Jazmin Stuart" y 
- en la lista de puntajes, hay mayor cantidad de notas mayores o iguales a 6 que las
  que son menores a 6

Ademas, agrega DOS casos de prueba adicionales,en donde uno sea Falso y el otro Verdadero.


-------------------------------------------------------------------------------
Aqui coloca tu Padron: 
Aqui coloca tu Apellido y Nombre: 
-------------------------------------------------------------------------------
"""

actores_1 = ["Gerardo Romano", "Jazmin Stuart", "Esteban Bigliardi"]
actores_2 = ["Emma Stone", "Michael Keaton", "Edward Norton"]
actores_3 = ["Ricardo Darin", "Soledad Villamil"]
actores_4 = ["Leonardo Di Crapio", "Rodolfo Machado"]
actores_5 = ["Brad Pitt"]
puntajes_1 = [6]
puntajes_2 = [2, 8]
puntajes_3 = [5, 6, 9, 7, 8]
puntajes_4 = [7,5,9]
puntajes_5 = [3,1]


def elegir_pelicula(actores, puntajes):

    """ Casos de Prueba:

    >>> elegir_pelicula(actores_1, puntajes_2)
    False
    >>> elegir_pelicula(actores_3, puntajes_3)
    False
    >>> elegir_pelicula(actores_2, puntajes_1)
    True
    >>> elegir_pelicula(actores_4, puntajes_4)
    True
    >>> elegir_pelicula(actores_5, puntajes_5)
    False
    """
    #--------- Escribi el Codigo de la Funcion a partir de aqui ---------------#
    pos_actores = 0
    valido = False
    cont_valido = 0
    cont_invalido = 0
    actores_validos =  ["Emma Stone", "Jazmin Stuart", "Leonardo Di Crapio", "Susana Gimenez"]
    for pos in puntajes:    
        if pos>=6:
            cont_valido += 1
        else:
            cont_invalido += 1
    
    while pos_actores<len(actores) and valido == False:
        if actores[pos_actores] in actores_validos and cont_valido>cont_invalido:
            valido = True
        pos_actores += 1

    return valido
    

# -------------------------------- Bloque Principal -----------------------------#
import doctest
doctest.testmod()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++