#!/usr/bin/env python3
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from fixture import campeonato
"""

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

Aqui coloca tu Padron: 

Aqui coloca tu Apellido y Nombre: 

-------------------------------------------------------------------------------

"""


def partidos_jugados(campeonato):
    acum = 0
    lista_partidos_jugados=[]
    for equipo,jugadas in campeonato.items():
        acum = jugadas[0]+jugadas[1]+jugadas[2]
        lista_partidos_jugados.append(acum)
    
    max_cant_jugadas = max(lista_partidos_jugados)

    mas_partidos_jugados =  lista_partidos_jugados.count(max_cant_jugadas)

    return mas_partidos_jugados == 1


def equipo_por_puntaje(campeonato):
    l_equipo_puntaje = []
    for equipo in campeonato:
        puntaje = 3*campeonato[equipo][0]+campeonato[equipo][1]
        l_equipo_puntaje.append((equipo,puntaje))

    return sorted(l_equipo_puntaje,key=lambda puntaje:puntaje[1],reverse=True)


def mostrar_resultados(campeonato):
    if partidos_jugados(campeonato):
        print('Hay un solo equipo con mas partidos jugados')
    else:
        print('No hay equipo con mas partidos jugados ')

    for equipo,puntaje in equipo_por_puntaje(campeonato):
        print("{}-{}".format(equipo,puntaje))

mostrar_resultados(campeonato)
    