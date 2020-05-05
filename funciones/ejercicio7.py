#!/usr/bin/env python3

def serie_ordenada(lista1):
    lista_ordenada_ascendente = sorted(lista1)
    lista_ordenada_descendiente =  sorted(lista1)

    if lista1 == lista_ordenada_ascendente:
        ordenada = 1
    elif lista1 == lista_ordenada_descendiente:
        ordenada = 0
    else:
        ordenada = 2
    
    return ordenada 


    