'''
Escribir una función que reciba una cadena de caracteres alfanuméricos y devuelva la cantidad de 
caracteres alfabéticos (letras) que hay en la cadena.

Debe validar que lo recibido sea una cadena formada sólo por números y/o letras, si no lo fuera, la función 
debe devolver -1.

Deberá comprobar el correcto funcionamiento, mediante los siguientes casos de prueba usando la librería 
doctest.

Para "Algoritmos", debe devolver 10
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
apellido, por tu apellido.
'''
import doctest

def charCount(string):
    '''Test Cases

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
    #Declaro una variable que utilizare como contador mas adelante
    charCount = 0

    #Filtro strings que contengan caracteres especiales
    if not string.isalnum():
        charCount = -1
    #Si no tiene caracteres especiales, analizo los caracteres por separado
    else:
        #Recorro el string
        for char in string:
            #Cuento las letras
            if char.isalpha():
                charCount += 1

    #Devuelvo la cantidad de letras
    return charCount

doctest.testmod()
