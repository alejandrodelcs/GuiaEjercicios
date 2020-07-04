"""

Escribir una funcion que devuelva verdadero si elegis un delivery que figura en un sitio, falso de lo 
contrario. 

La funcion recibe dos listas: una de platos y otra de valoraciones dadas en cantidad de motos.

La lista platos puede tener desde 1 a n platos.

La lista valoraciones puede tener desde 1 a m valoraciones (de 1 a 5).



Se elige el delivery cuando:

- En la lista platos tiene "milanesa" y "papas fritas" (ambos platos deben estar como dos platos distintos) 
o "pizza napolitana"  

- Ademas de lo anterior, el promedio de valoraciones tiene que ser mayor o igual que 3,

  salvo que tenga algun 1, en ese caso no se acepta



Ademas, agrega DOS casos de prueba adicionales,en donde uno sea Falso y el otro Verdadero.



NOTA: bajate este archivo que tiene listas cargadas y casos de prueba. El codigo escribilo ahi mismo.

NOMBRA TU ARCHIVO DE LA SIGUIENTE FORMA: padrón_apellido_ej_2c.py  reemplazando padrón por tu padrón y 
apellido, por tu apellido.




-------------------------------------------------------------------------------

Aqui coloca tu Padron: 106223

Aqui coloca tu Apellido y Nombre: Litteri Ivan

-------------------------------------------------------------------------------

"""
    #--------- Escribi el Codigo de la Funcion a partir de aqui ---------------#
def deliveryReception(meals, ratings):
    """ 
    Casos de Prueba:

    >>> deliveryReception(meals_1, ratings_1)
    False
    >>> deliveryReception(meals_2, ratings_3)
    False
    >>> deliveryReception(meals_3, ratings_2)
    True
    >>> deliveryReception(meals_4, ratings_5)
    True
    >>> deliveryReception(meals_5, ratings_5)
    False
    >>> deliveryReception(meals_4, ratings_4)
    False
    >>> deliveryReception(meals_5, ratings_4)
    False

    """
    #Declaro esta variable como True, para luego ser devuelta como tal si pasa las interrogaciones
    delivery = True
    #Declaro una variable que utilizare mas adelante con valor 0
    totalRating = 0

    #Recorro los ratings
    for i in ratings:
        #Si algun rating es 1, cambio el valor de la variable que declare al principio
        if i == 1:
            delivery = False
        #Sumo al rating total el valor del rating que toma i en cada iteracion
        totalRating += i

    #Calculo el promedio de rating 
    averageRating = totalRating / len(ratings)

    #Analizo si el pedido cumple los requisitos para delivery
    if not (("milanesa" in meals and "papas fritas" in meals) or "pizza napolitana" in meals) or averageRating < 3:
        delivery = False

    #Retorno si tengo o no que hacer delivery
    return delivery

# ------------------------------- Bloque Principal -----------------------------#
meals_1 = ["milanesa", "pollo", "tarta de queso"]
meals_2 = ["tira de asado", "ensalada mixta", "pizza napolitana"]
meals_3 = ["milanesa", "ravioles", "papas fritas"]
meals_4 = ["pizza napolitana", "batatas fritas"]
meals_5 = ["milanesa"]
ratings_1 = [5]
ratings_2 = [2, 5]
ratings_3 = [1, 5, 4, 4]
ratings_4 = [3, 2, 2, 2]
ratings_5 = [3, 3]

import doctest
doctest.testmod()