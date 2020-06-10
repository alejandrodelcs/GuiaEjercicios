#!/usr/bin/env python3
from datos import *
import random

def validacion_mes():
    mes =  None
    anio = None
    while mes == None and anio == None:
        print('No puede ingresar letras, solo numeros.\nPor ejemplo: Febrero: 2, Año: 2020')
        try:
            mes = random.randint(1, 12)
            anio = random.randint(2016, 2020)
            if mes not in list(range(1,32)):
                mes = None
        except ValueError:
            print('¡Error!.')
    return mes,anio

def temp_min_promedio(datos_met):
    suma = 0
    l_minimas_ult_mes = [datos_met[ciudad][-1][1] for ciudad in datos_met]
    for temp in l_minimas_ult_mes:
        suma += temp
    print('Promedio Minimas Temperaturas: {:.3f} °C '.format(suma/len(l_minimas_ult_mes)))



def ciudades_min_max(datos_met,min_max):
    l_ciudades = []
    for ciudad in datos_met:
        if min_max in [pos[1] for pos in datos_met[ciudad]]:
            l_ciudades.append(ciudad)

    #print([ciudad for ciudad in datos_met if min_max in [pos[1] for pos in datos_met[ciudad]]])
    print('Menor temperatura Maxima: {} - {} °C'.format(l_ciudades[0],min_max))

def min_temperatura(datos_met):
    min_max = min([pos[1] for ciudad in datos_met for pos in datos_met[ciudad]])
    ciudades_min_max(datos_met,min_max)


def max_min_temperatura(tupla_ciudades):
    for ciudad,listas in tupla_ciudades:
        print('-------------------------------------------------')
        for pos in range(len(listas)):
            print(' Ciudad: {} - Temp Maxima: {}'.format(ciudad,listas[pos][2]))
            print(' Ciudad: {} - Temp Mínima: {}'.format(ciudad,listas[pos][1]))
        print('-----------------------------------------------------------------')

def imprimir_amplitud_termica(l_ordenado):
    for dat1,dat2,dat3 in l_ordenado:
        print(' Ciudad: {} - Amplitud Termica: {} -  Dia: {}'.format(dat1,dat2,dat3[0]))
    


def amplitud_termica(datos_met):
    l = []
    suma = 0
    for ciudad in datos_met:
        max_termica =  max([datos[2]-datos[1] for datos in datos_met[ciudad]])
        l_dias = [dat[0] for dat in datos_met[ciudad] if dat[2]-dat[1]==max_termica]
        l.append((ciudad,max_termica,l_dias))
    imprimir_amplitud_termica(sorted(l,key= lambda x:x[1]))
    
def mostrar_datos(datos_met):
    valido = False
    while valido == False:
        ciudad = input('\n\nIngrese Ciudad que desea información: ')
        if ciudad in datos_met:
            print('-----------------------------------------------------------------')
            for dia in datos_met[ciudad]:
                print('Día: {} - Ciudad: {} - Min: {} - Max: {}'.format(dia[0],ciudad,dia[1], dia[2]))
                print('-----------------------------------------------------------------')
            valido = True
        else:
            print('\nCiudad Inexistente')

def ingreso():
    ciudades = []
    dias = validacion_mes()
    datos_met = cargar_datos(dias[0],dias[1])
    if datos_met != {}:
        max_min_temperatura(sorted(datos_met.items(), key = lambda x: x[0]))
        min_temperatura(datos_met)
        temp_min_promedio(datos_met)
        amplitud_termica(datos_met)
        mostrar_datos(datos_met)

ingreso()