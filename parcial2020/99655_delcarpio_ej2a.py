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

def main():
    datos = {}
    ingreso_dicc(datos)

    for prov in datos:
        print('{} - cantidad de infectados: {}  cantidad de fallecidos- {} '.format(prov,datos[prov][0], datos[prov][1]))


main()
