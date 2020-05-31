#!/usr/bin/env python3

"""
Las 23 provincias más CABA realizan sus aportes a la Nación mediante impuestos, a su vez, Nación le transfiere fondos mediante la coparticipación.
A cada provincia se le asocian 6 datos: los 5 primeros son los impuestos que pagan a Nación, en el siguiente orden: IVA, Ganancias, Contribuciones, Exportaciones, Otros. El último dato es la coparticipación que paga Nación a las provincias.
Se pide hacer un programa en Python que:
1)	Determine el impuesto máximo abonado, indicando el tipo de impuesto y la provincia. Por ejemplo: Córdoba – Ganancias - $3200 millones.
2)	Indique si el IVA fue el mayor impuesto abonado en el año teniendo en cuenta el total de impuestos.
3)	Imprima un listado de las 10 provincias que recibieron mayor coparticipación en relación a sus aportes, ordenado de mayor a menor por porcentaje, por ejemplo, si aportó 40 y recibió 30, el porcentaje es 75% (30/40). Se debe indicar porcentaje – provincia:

Porcentaje	Provincia

Nota: 
•	Los montos vienen dados en millones de pesos.
"""
def cargar_dicc_prov(provincias):
    prov = input('Ingrese Provincia: ')
    iva = int(input('Ingrese impuesto pagado de IVA: '))
    ganancias = int(input('Ingrese ganancias: '))
    contribuciones = int(input('Ingrese contribuciones: '))
    exportaciones = int(input('Ingrese exportaciones: '))
    cooparticipacion =  int(input('Ingrese cooparticipación que aporto: '))
    if not prov in provincias:
        provincias[prov] = [iva,ganancias,contribuciones,exportaciones,cooparticipacion]
    else:
        provincias[prov][0] += iva
        provincias[prov][1] += ganancias
        provincias[prov][2] += contribuciones
        provincias[prov][3] += exportaciones
        provincias[prov][4] += cooparticipacion

def imprimir_impuesto_max_abonado(impuesto_max):
    for prov in impuesto_max:
        if impuesto_max[prov][1]==0:
            print('{} - {} - ${} millones'.format(prov,'IVA',impuesto_max[prov][0]))
        elif impuesto_max[prov][1]==1:
            print('{} - {} - ${} millones'.format(prov,'Ganancias',impuesto_max[prov][0]))
        elif impuesto_max[prov][1]==2:
            print('{} - {} - ${} millones'.format(prov,'Contribuciones',impuesto_max[prov][0]))
        elif impuesto_max[prov][1]==3:
            print('{} - {} - ${} millones'.format(prov,'Exportaciones',impuesto_max[prov][0]))

def mayor_iva(total_impuesto, provincias):
    for prov in provincias:
        if provincias[prov][0]<total_impuesto[prov]:
            print('El IVA fue el mayor impuesto abonado en el año : {} - ${} millones'.format(prov,
                                                                                            total_impuesto[prov]))


def iva_abonado_anio(provincias):
    total_impuesto = {}
    for prov in provincias:
        total = provincias[prov][0]+provincias[prov][1]+provincias[prov][2]+provincias[prov][3]
        total_impuesto[prov] = total
    mayor_iva(total_impuesto, provincias)


def impuesto_max(provincias):
    impuesto_max = {}
    for prov in provincias:
        impuesto_max[prov]=[max(provincias[prov]),provincias[prov].index(max(provincias[prov]))]
    imprimir_impuesto_max_abonado(impuesto_max)

def imprimir_mayor_cooparticipacion(lista_ordenada_prov):
    for pos in range(len(lista_ordenada_prov)):
        print('{} - {}'.format(lista_ordenada_prov[pos][0], lista_ordenada_prov[pos][1]))

def cooparticipacion_porcentaje(provincias):
    coopar = []
    for prov in provincias:
        print(prov,end='')
        recibio_coopar = int(input('-Ingrese coparticipación que recibio: '))
        porcentaje = (recibio_coopar/provincias[prov][4])*100
        coopar.append((prov,porcentaje))

    imprimir_mayor_cooparticipacion(sorted(coopar, key=lambda recibido: coopar[1]))
    print(coopar)
    print(sorted(coopar, key=lambda recibido: coopar[1]))
    

def main():
    provincias = {}
    fin = 'no'
    while fin.lower() == 'no':
        cargar_dicc_prov(provincias)
        fin = input('¿Termino de cargar? si/no   ')
    impuesto_max(provincias)
    iva_abonado_anio(provincias)
    cooparticipacion_porcentaje(provincias)

main()