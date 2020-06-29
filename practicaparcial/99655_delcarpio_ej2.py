#!/usr/bin/env python3

platos_1 = ["milanesa","pollo", "tarta de queso"]
platos_2 = ["tira de asado", "ensalada mixta", "pizza napolitana"]
platos_3 = ["milanesa", "ravioles", "papa fritas"]
platos_4 = ["merluza con papas", "sorretinos"]

valoraciones_1 = [5]
valoraciones_2 = [2, 5]
valoraciones_3 = [1,5,4,4]
valoraciones_4 = [4,8,5]
valoraciones_5 = [1]

def valoracion(valoraciones):
    acum = 0
    for num in valoraciones:
        acum += num
    return acum//len(valoraciones) 

def delivery(platos, valoraciones):
    """
    >>> delivery(platos_1,valoraciones_1)
    True
    >>> delivery(platos_2,valoraciones_2)
    True
    >>> delivery(platos_3, valoraciones_3)
    True
    >>> delivery(platos_4, valoraciones_4)
    False
    >>> delivery(platos_1, valoraciones_5)
    False
    """
    pos = 0
    valido = False
    platos_pedidos = ["milanesa", "papas fritas", "pizza napolitana", "Canelones", "Ravioles"]
    while pos<len(platos_pedidos) and valido == False:
        if platos_pedidos[pos] in platos and valoracion(valoraciones)>= 3:
            valido = True
        else:
            valido = False
        pos += 1

    return valido


import doctest
doctest.testmod()


