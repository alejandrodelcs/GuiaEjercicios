#!/usr/bin/env python3

def imprime_datos(lista_peso_1,lista_peso_2,lista_peso_3,lista_peso_4):
    print('Entre 0,000 y 10,000 kg.  hay {} niños'.format(len(lista_peso_1)))
    print('Entre 10,001 y 20,000 kg. hay {} niños'.format(len(lista_peso_2)))
    print('Entre 20,001 y 30,000 kg. hay {} niños'.format(len(lista_peso_3)))
    print('Más de 30,000 kg.         hay {} niños'.format(len(lista_peso_4)))
    
def clasificacion_peso(lista_peso_1, lista_peso_2, lista_peso_3, lista_peso_4,peso):
    i=1

    if peso >= 1 and peso <= 10:
        lista_peso_1.append(i)
    elif peso >= 11 and peso <=20:
        lista_peso_2.append(i)
    elif peso >= 21 and peso <= 30:
        lista_peso_3.append(i)
    else:
        lista_peso_4.append(i)

def ingreso_peso():
    bandera = True
    while bandera == True:
        print('Termina con cero')
        peso = int(input('Ingrese peso: '))
        if peso < 0:
            print('Error de ingreso')
            bandera = True
        else:
            bandera = False
    return peso

def main():
    lista_peso_1 = []
    lista_peso_2 = []
    lista_peso_3 = []
    lista_peso_4 = []

    peso = ingreso_peso()
    while peso != 0:
            clasificacion_peso(lista_peso_1,lista_peso_2,lista_peso_3, lista_peso_4, peso)
            peso = ingreso_peso()

    imprime_datos(lista_peso_1,lista_peso_2,lista_peso_3,lista_peso_4)


    

main()


