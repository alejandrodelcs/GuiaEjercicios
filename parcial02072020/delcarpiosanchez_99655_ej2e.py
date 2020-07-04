#!/usr/bin/env python3
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Escribir una función que recibe una lista de audiolibros (tuplas) 

Cada tupla tiene el autor de un audiolibro y la  duración del mismo en minutos.

La función debe devolver True si encuentra que hay al menos un audiolibro que te interese escuchar.



Los audiolibros que te interesan son los que cumplen alguna de las siguientes condiciones:

- El autor sea "Jorge Luis Borges", "J. K. Rowling" o "Stephen King"

- La duracion sea menos de 2 horas o más de 10



Ademas, agregá DOS casos de prueba adicionales,en donde uno sea Falso y el otro Verdadero.



NOTA: bajate este archivo que tiene listas cargadas y casos de prueba. El código escribilo ahí mismo.

NOMBRA TU ARCHIVO DE LA SIGUIENTE FORMA: apellido_legajo_ej_2e.py  reemplazando legajo por tu padrón y apellido, por tu apellido.


-------------------------------------------------------------------------------
Aqui coloca tu Padron: 99655
Aqui coloca tu Apellido y Nombre: Del Carpio Sanchez Alejandro
-------------------------------------------------------------------------------
"""

audiolibros_1 = [("Jorge Luis Borges", 180), ("Richard Dawkins", 220), ("José Saramago", 520)]
audiolibros_2 = [("Paulo Coelho", 480), ("Jimena La Torre", 500), ("Anónimo", 599)]
audiolibros_3 = [("Mark Twain", 100), ("Dan Brown", 1000), ("Fredrik Backman", 400)]
audiolibros_4 = [("Gustavo Bianchi", 220), ("Andres Juarez",180)]
audiolibros_5 = [("Alejandro Del Carpio",500), ("Sofia Marchesini", 550), ("Pedro Del Caño", 100)]

def filtrar_audiolibros(audiolibros):

    """ Casos de Prueba:

    >>> filtrar_audiolibros(audiolibros_1)
    True
    >>> filtrar_audiolibros(audiolibros_2)
    False
    >>> filtrar_audiolibros(audiolibros_3)
    True
    >>> filtrar_audiolibros(audiolibros_4)
    False
    >>> filtrar_audiolibros(audiolibros_5)
    True

    
    """
    #--------- Escribi el Codigo de la Funcion a partir de aqui ---------------#
    pos = 0
    pos2 = 0
    interes = False
    l_autores = ["Jorge Luis Borges","J. K. Rowling","Stephen King","Alejandro Del Carpio"]
    while pos<len(audiolibros) and pos2<len(l_autores) and interes == False:
        if l_autores[pos2] in audiolibros[pos]:
            interes = True
        elif audiolibros[pos][1] <= 120 or audiolibros[pos][1] >= 600:
            interes = True
        else:
            interes = False
        pos += 1
        pos2 += 1

    return interes



# -------------------------------- Bloque Principal -----------------------------#

import doctest
doctest.testmod()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++