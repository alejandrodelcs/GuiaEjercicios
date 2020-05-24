#!/usr/bin/env python3

def ingreso_dicc(localidades):
    localidad = input('Ingrese localidad: ')
    cant_personas = int(input('Ingrese cantidad personas: '))
    cant_empleados = int(input('Ingrese cantidad empleados: '))
    if not localidad in localidades:
        localidades[localidad] =  [cant_personas, cant_empleados]
    else:
        localidades[localidad][0] += cant_personas
        localidades[localidad][1] += cant_empleados

def imprimir_calculo_personas(total_edad_laboral, empleados_localidad):
    print('Cantidad de personas en edad laboral: {}'.format(total_edad_laboral))
    for localidad in empleados_localidad:
        print('Localidad: {} -  Empleados: {} '.format(localidad[0],localidad[1]))

def calculo_personas(localidades):
    total_edad_laboral = 0
    empleados_localidad = []
    for localidad in localidades:
        total_edad_laboral += localidades[localidad][0] 
        empleados_localidad.append((localidad,localidades[localidad][1]))
    imprimir_calculo_personas(total_edad_laboral, empleados_localidad)

def imprimir_desempleo_localidad(lista_ordenada):
    for tupla in lista_ordenada:
        print('Localidad: {} - Desocupacion: {}% '.format(tupla[0],tupla[1]))

def ordenar_por_desempleo(localidades):
    lista_desocupacion = []
    for localidad in localidades:
        desocupacion = (localidades[localidad][0]-localidades[localidad][1])/100
        lista_desocupacion.append((localidad,desocupacion))
    imprimir_desempleo_localidad(sorted(lista_desocupacion, key=lambda desocup: lista_desocupacion[1]))

def main():
    localidades = {}
    ingreso = 'no'
    while ingreso.lower() != 'si':
        ingreso_dicc(localidades)
        ingreso = input('¿Termino de cargar? si/no    ')
    calculo_personas(localidades)
    ordenar_por_desempleo(localidades)



main()