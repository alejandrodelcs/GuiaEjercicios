#!/usr/bin/env python3

""" Ejercicio 3
    Ingresar en un diccionario localidades (clave) y dos datos:
    cantidad de personas en edad laboral – cantidad de empleados.
    Los datos surgen de distintas planillas, por lo que una misma clave
    (localidad) se puede ingresar varias veces, debiendo sumarse los valores.
    Se pide: 
    a) Calcular el total de personas en edad laboral y empleados
    para cada localidad e imprimirlo.
    b) Imprimir un listado ordenado de mayor a menor por porcentaje
    de desocupación. Indicando: localidad - % de desocupación
"""
def ingreso_datos():
    localidades = {}
    localidad = input('Ingrese localidad: ')
    while localidad != '':
        cantidad_personas = int(input("Ingrese cantidad de personas: "))
        cantidad_empleados = int(input("Ingrese cantidad de empleados: "))
        if localidad in localidades:
            localidades[localidad]["personas"] +=  cantidad_personas
            localidades[localidad]["empleados"] += cantidad_empleados
        else:
            localidades[localidad] = {"personas":cantidad_personas, "empleados":cantidad_empleados}
        localidad = input('Ingrese localidad: ')
    return localidades 


def calculo_desocupacion(localidades):
    desocupacion = {}
    for localidad in localidades:
        desocupados = localidades[localidad]["personas"] - localidades[localidad]["empleados"]
        desocupacion[localidad] = (100*desocupados)/localidades[localidad]["personas"]
    return desocupacion

def desocupados_ordenado(desocupacion):
    ordenados_por_desocupacion = sorted(desocupacion.items(), key=lambda desc:desc[1],reverse=True)

    return ordenados_por_desocupacion


localidades = ingreso_datos()
for localidad in localidades:
    print("Localidad:{} \nPersonas en edad laboral: {} \nCantidad de personas en edad laboral: {}".format(localidad, 
    localidades[localidad]["personas"], localidades[localidad]["empleados"]))
desocupacion = calculo_desocupacion(localidades)
ordenados_por_desocupacion=desocupados_ordenado(desocupacion)
for dat in ordenados_por_desocupacion:
    print("Localidad: {}\nDesocupacion {:.3f}".format(dat[0], dat[1]))







