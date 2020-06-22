#!/usr/bin/env python3
from fixture import campeonato
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""



// Va con un diccionario cargado - importar fixture



El diccionario "campeonato" tiene cargados a equipos de futbol como clave y una terna de numeros (lista), 

cuyo significado es: partidos ganados (primer valor), partidos empatados (segundo valor), 

partidos perdidos (tercer valor).



Se pide que hagas un programa en Python que:

a) Indique si hay solo un equipo que mas partidos jugados que el resto de los equipos.

b) Liste de mayor a menor los equipos por puntaje, teniendo en cuenta que obtiene 3 puntos por

cada partido ganado, y un punto por cada partido empatado.

Indicando:

equipo - puntaje



NOTA: bajate este archivo que tiene el diccionario cargado. El codigo escribilo en otro archivo, importando el de fixture.

NOTA 2: copia y pega este enunciado como comentario al principio de tu archivo.

NOMBRA TU ARCHIVO DE LA SIGUIENTE FORMA: padrón_apellido_ej_3a.py  reemplazando padrón por tu padrón y apellido, por tu apellido


-------------------------------------------------------------------------------

Aqui coloca tu Padron: 99655

Aqui coloca tu Apellido y Nombre: Del Carpio Sanchez Alejandro 

-------------------------------------------------------------------------------

"""


def equipos_con_partidos_mas_jugados(fixture):
    total_partidos = 0
    l_equipo = []
    for equipo in fixture:
        total_partidos = fixture[equipo][0] + fixture[equipo][1] + fixture[equipo][2]
        l_equipo.append((equipo, total_partidos))
    return l_equipo

def equipos_por_puntaje(fixture):
    l_ordenada_puntaje = sorted(fixture.items(), key = lambda x:x[1][1])
    return l_ordenada_puntaje


l_equipo = equipos_con_partidos_mas_jugados(campeonato)
l_equipo_ordenado = sorted(l_equipo, key = lambda p:p[1], reverse =True)
print("Equipo con mas partidos jugados: {} -  partidos: {} ".format(l_equipo_ordenado[0][0], l_equipo_ordenado[0][1]))

l_puntaje = equipos_por_puntaje(campeonato)   
for puntaje in l_puntaje:
    print("Equipo: {} - Puntaje: {}".format(puntaje[0], puntaje[1][0]))
