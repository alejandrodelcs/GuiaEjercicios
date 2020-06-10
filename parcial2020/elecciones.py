#!/usr/bin/env python3
"""
Se cargan datos en un diccionario en forma manual. Estos datos consisten en el nombre de un partido politico,
la cantidad de votos validos, y la cantidad de votos invalidos que obtuvo en alguna localidad de nuestro
país (no se ingresa la localidad, solo se ingresa el nombre del partido y dos enteros, y un partido puede ser
ingresado muchas veces).
La carga finalizara cuando el data-entry presione enter cuando se le pida el nombre de un partido.


Escribir una funcion que permita realizar la carga, y su valor de retorno sea el diccionario deseado.
"""

def cargar_datos_elecciones():
    votacion = {}
    partido = input('Ingrese partido: ')
    while partido != '':
        voto_valido = int(input('Ingrese voto valido: '))
        voto_invalido =  int(input('Ingrese voto invalido: '))

        if partido in votacion:
            votacion[partido]["validos"] +=  voto_valido
            votacion[partido]["invalido"] +=  voto_invalido
        else:
            votacion[partido] = {"validos":voto_valido, "invalido":voto_invalido}
        partido = input('Ingrese partido: ')
        
    return votacion

def ganador_elecciones(votacion):
    partido_ganador = ""
    votacion_ganador =  -1
    for partido in votacion:
        if votacion[partido]["validos"] > votacion_ganador:
            partido_ganador = partido
            votacion_ganador = votacion[partido]["validos"]
    return partido_ganador,votacion_ganador

def total_votos(votacion):
    votos = 0
    for partido in votacion:
        votos += votacion[partido]["validos"]
    return votos

def clasificados_eleccion_general(votacion):
    votos_totales = total_votos(votacion)
    clasificados = []
    #clasificado = [partido for partido in votacion if votacion[partido]["valido"]/votos_totales > 0.1]
    for partido in votacion:
        if votacion[partido]["validos"] / votos_totales > 0.1:
            clasificados.append(partido)
    return clasificados

def ranking_votos_invalidos(votacion):
    ranking =  sorted(votacion.items(),key = lambda tupla_votos:tupla_votos[1]["invalidos"],reverse=True)
    return ranking
        

votacion = cargar_datos_elecciones()
print(ganador_elecciones(votacion))
print(clasificados_eleccion_general(votacion))
