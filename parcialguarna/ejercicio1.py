x#!/usr/bin/env python3

def elegir_pelicula(actores, puntajes):
    actores_validos =  ["Emma Stone", "Jazmin Stuart", "Leonardo Di Crapio", "Susana Gimenez"]
    elegido = False
    for act in actores:
        for pts in puntajes:
            if act in actores_validos and pts in [678910]:
                elegido = True

    return elegido

actores_1 = ["Gerardo Romano", "Jazmin Stuart", "Esteban Bigliardi"]
puntajes_1 = [6]
print(elegir_pelicula(actores_1, puntajes_1))
