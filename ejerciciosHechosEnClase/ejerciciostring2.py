#!/usr/bin/env python3

def sumar_numeros(palabra):
    acum = 0
    for i in palabra:
        if i > 0:
            acum += i
        else:
            acum = 0
            print('')
    return acum

def es_alfanumerica(palabra):
    if palabra.isdigit() == False:
        alfanumerica = 1
    else:
        alfanumerica = 0
    return alfanumerica

def main():
    palabra = input('Ingrese palabra: ')
    #resultado = sumar_numeros(palabra)
    digitos = es_alfanumerica(palabra)

    #print('Es alfanumerica {}.  La suma de los numeros es: {}'.format(resultado, digitos))

    print(es_alfanumerica(palabra))

main()