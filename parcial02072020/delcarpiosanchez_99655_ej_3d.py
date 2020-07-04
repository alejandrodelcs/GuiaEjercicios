#!/usr/bin/env python3
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from vecinos import vecinos
"""

// Va con un diccionario cargado - importar el modulo vecinos

El diccionario vecinos tiene cargados para cada piso y depto los datos de las expensas normales y extraordinarias del mes pasado.

Es decir, la lista de dos enteros que cada clave tiene asociada representa, "expensas normales" y "expensas extraordinarias", en ese orden.



Se pide que armes un programa en Python que:

- Indique al administrador de consorcio cuánto tiene que recaudar en total

- Liste el promedio de expensas normales y el promedio de extraordinarias

- Muestre quién paga mayor proporción de extraordinarias por sobre expensas normales



NOTA: bajate este archivo que tiene el diccionario cargado. El codigo escribilo en otro archivo, importando el módulo vecinos.

NOTA 2: copia y pega este enunciado como comentario al principio de tu archivo.

NOMBRA TU ARCHIVO DE LA SIGUIENTE FORMA: apellido_legajo_ej_3d.py  reemplazando legajo por tu padrón y apellido, por tu apellido



-------------------------------------------------------------------------------



Aqui coloca tu Padron: 99655



Aqui coloca tu Apellido y Nombre: Del Carpio Sanchez Alejandro



-------------------------------------------------------------------------------


"""

def total_recaudar(vecinos):
    for dpto,expensas in vecinos.items():
        total = expensas[0]+expensas[1]
    return total

def promedio_expensas(vecinos):
    total_normales = 0
    total_extraordinarias = 0
    cont = 0 #Contador 
    for dpto,expensas in vecinos.items():
        total_normales += expensas[0] #Calculo de expensas normales
        total_extraordinarias += expensas[1] #calculo de expensas extraordinarias
        cont += 1 #va contando las veces que va itera por cada clave, así obtengo el total de dpto

    promedio_normales = total_normales/cont 
    promedio_extraordinaria =  total_extraordinarias/cont
        
    return promedio_normales,promedio_extraordinaria

def mayor_proporcion_de_extraordinarias(vecinos):
    dicc_vecinos = {}
    for dpto,expensas in vecinos.items():
        proporcion = expensas[1]/expensas[0]
        dicc_vecinos[dpto] = proporcion

    pago_mayor_extraordinaria = sorted(dicc_vecinos.items(),key=lambda vecino:vecino[1],reverse=True)
    
    return pago_mayor_extraordinaria
    


total = total_recaudar(vecinos)
print("Total Recaudado: {}".format(total))

l_promedio = promedio_expensas(vecinos)
print('Promedio de Expensas Normales {} - Promedio de Expensas Extraordinarias{}'.format(l_promedio[0],l_promedio[1]))

vecino_que_pago_mas = mayor_proporcion_de_extraordinarias(vecinos)
print("Vecino que pago mayor recaudacion: {}".format(vecino_que_pago_mas[0][0]))
