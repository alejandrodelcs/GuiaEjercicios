#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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

Aqui coloca tu Padron: 106223

Aqui coloca tu Apellido y Nombre: Litteri Ivan

-------------------------------------------------------------------------------

"""
import fixture 

def playedMatches(dictionary):
    #Creo una lista con el total de los partidos jugados por cada equipo
    playedMatchesCount = [sum(matchResults) for team, matchResults in dictionary.items()]
    #Tomo el mayor valor de la lista con el total de los partidos jugados por cada equipo
    maxMatchesPlayed = max(playedMatchesCount)
    #Me fijo si hay mas de un equipo que haya jugado esa mayor cantidad de partidos
    teamsWithMoreMatches = playedMatchesCount.count(maxMatchesPlayed)
    
    #Devuelvo True si hay solo un equipo que jugo mas partidos que los demas, False en caso contrario
    return teamsWithMoreMatches == 1

#Creo el diccionario con los equipos como keys y sus puntos como values, ordenados de mayor a menor
def pointsPerTeamCalculator(dictionary):
    #Creo un diccionario vacio, para utilizarlo mas adelante
    newDict = {}

    #Recorro el diccionario que entra a la funcion como argumento
    #Desempaqueto los items del diccionario en dos variables
    for team, matchResults in dictionary.items():
        #Desempaqueto los valores de matchResults en tres variables para utilizar las que me interesan por separado
        won, tied, lost = matchResults
        #Agrego al diccionario, al equipo como key y su cantidad de puntos como value
        newDict[team] = 3 * won + tied

    #Retorno el diccionario ordenado de mayor a menor por cantidad de puntos 
    return sorted(newDict.items(), key=lambda pack: pack[1], reverse=True)

#Imprimo los resultados en funcion de las consignas
def printResults(dictionary):
    #Entra al if si la funcion playedMatches es True, sino, entra al else
    if playedMatches(dictionary):
        print("Hay solo un equipo que jugo mas partidos que los demas")
    else:
        print("No hay solo un equipo que jugo mas partidos que los demas")
    #Recorro el diccionario ordenado que obtengo de la funcion pointsPerTeamCalculator y lo desempaqueto en dos variables de interes  
    for team, points in pointsPerTeamCalculator(dictionary):
        print(f'{team} - {points}')
    
#tournament es una variable global que esta en el archivo fixture (es el diccionario)
printResults(fixture.tournament)