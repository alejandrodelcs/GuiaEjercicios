#!/usr/bin/env python3
def ingreso_dicc():
    datos_covid = {}
    provincia = input('Ingrese provincia: ')
    while provincia != '':
        infectados = int(input('Ingrese cantidad de infectados: '))
        fallecidos = int(input('Ingrese cantidad de fallecidos: '))
        if provincia in datos_covid:
            datos_covid[provincia]['infectados'] += infectados 
            datos_covid[provincia]['fallecidos'] += fallecidos
        else:
            datos_covid[provincia] = {'infectados': infectados, 'fallecidos': fallecidos}
        provincia = input('Ingrese provincia: ')
    return datos_covid

def estadisticas_totales(datos_covid):
    infectados = 0
    fallecidos = 0
    for provincia in datos_covid:
        infectados += datos_covid[provincia]['infectados']
        fallecidos += datos_covid[provincia]['fallecidos']
    return infectados, fallecidos


def provincias_alta_mortalidad(datos_covid,indice_de_mortalidad_general):
    provincias_mortales = []
    for provincia in datos_covid:
        indice_mortalidad_provincia = datos_covid[provincia]["fallecidos"] / datos_covid[provincia]["infectados"]
        if indice_mortalidad_provincia > indice_de_mortalidad_general:
            provincias_mortales.append(provincia)
    return provincias_mortales

def provincias_con_mas_casos(datos_covid):
    ordenada_por_casos = sorted(datos_covid.items(),key = lambda tupla:tupla[1]["infectados"], reverse = True)[:5]
    return ordenada_por_casos


datos_covid = ingreso_dicc()
infectados,fallecidos = estadisticas_totales(datos_covid)
print('Infectados {} - Fallecidos: {}'.format(infectados,fallecidos))
provincias_mortales = provincias_alta_mortalidad(datos_covid,fallecidos/infectados)
for provincia in provincias_mortales:
    print("provincia con mayor tasa de mortalidad: {}".format(provincia))
ordenada_por_casos = provincias_con_mas_casos(datos_covid)
for prov in ordenada_por_casos:
    print("Provincia: {} - Casos: {}".format(prov[0], prov[1]["infectados"]))

