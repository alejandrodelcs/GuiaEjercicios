#!/usr/bin/env python3

def ingreso_dicc(datos):
    
    provincia = None
    
    while provincia != '':
        provincia = input('Ingrese provincia: ')
        if provincia != '':
            cant_infectados = int(input('Ingrese cantidad de infectados: '))
            cant_fallecidos = int(input('Ingrese cantidad de fallecidos: '))
            if not provincia in datos: 
                datos[provincia] = [cant_infectados,cant_fallecidos]
            else:
                datos[provincia][0] += cant_infectados
                datos[provincia][1] += cant_fallecidos

def total_por_provincia(datos):
    cant_infectados = 0
    cant_fallecidos = 0
    for prov in datos:
        cant_infectados += datos[prov][0]
        cant_fallecidos += datos[prov][1]
        print('{} - cantidad de infectados: {} - cantidad de fallecidos- {} '.format(prov, cant_infectados, cant_fallecidos))

    return cant_infectados, cant_fallecidos

def imprimir_mortalidades(lista_mortalidades):

    if len(lista_mortalidades) != []:
        for dat in lista_mortalidades:
            print('\nMortalidades : {} - {} '.format(dat[0],dat[1]))
    else:
        print('No se encontro con provincia con relacion a la mortalidad')

def indice_mortalidad(datos):
    lista_covid = total_por_provincia(datos)
    lista_mortalidades = []
    mortalidad = (lista_covid[1]/lista_covid[0])

    print('\nMortalidad: ', mortalidad)

    for prov in datos: 
        mortalidad_prov = datos[prov][1]/datos[prov][0]
        if mortalidad_prov > mortalidad:
            lista_mortalidades.append((prov,mortalidad_prov))
    imprimir_mortalidades(lista_mortalidades)
    

def imprimir_prov_mayor_casos(lista_ordenada_casos):
    print('\nLista de casos')
    for casos in lista_ordenada_casos:
        print('{} - {}'.format(casos[0], casos[1]))


def provincia_mayor_casos(datos):
    lista_prov = []
    for prov in datos:
        lista_prov.append((prov,datos[prov][0]))
    imprimir_prov_mayor_casos(sorted(lista_prov, key = lambda infectados:infectados[1], reverse = True))

def main():
    datos = {}
    ingreso_dicc(datos)
    indice_mortalidad(datos)
    provincia_mayor_casos(datos)


main()