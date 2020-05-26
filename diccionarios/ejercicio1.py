#!/usr/bin/env python3

def ingreso_dicc(cant_lluvia):
    provincia = input('Ingrese localidad: ')

    for mes in range(4):
        cant = int(input('Ingrese Cantidad de lluvia: '))
        humedad_relativa = float(input('Ingrese humedad relativa: '))

        if not provincia in cant_lluvia:
            cant_lluvia[provincia] = [(cant,humedad_relativa,mes)]
        else:
            cant_lluvia[provincia].append((cant,humedad_relativa,mes))


def imprimir_mayor_mes(lista_lluvias):
    lista_meses = ['Enero', 'Febrero', 'Marzo', 'Abril','Mayo',
                    'Junio','Julio','Agosto','Septiembre','Octubre',
                    'Noviembre', 'Diciembre']
    for dat in range(3):
        print('Provincia: {} - Cantidad: {} mm - Mes: {}'.format(lista_lluvias[dat][0],
                                                            lista_lluvias[dat][1],
                                                            lista_meses[lista_lluvias[dat][2]]))
def mayor_lluvia_mes(cant_lluvia):
    lista_prov = []
    for provincia in cant_lluvia:
        for dat in cant_lluvia[provincia]:
            lista_prov.append((provincia,dat[0], dat[2]))
    
    print(lista_prov)
    imprimir_mayor_mes(sorted(lista_prov, key=lambda cantidad: cantidad[1],reverse=True))
    



def main():
    cant_lluvia = {}
    fin = 'no'
    while fin.lower() == 'no':
        ingreso_dicc(cant_lluvia)
        fin = input('¿termino de cargar? si/no    ')
    mayor_lluvia_mes(cant_lluvia)


main()