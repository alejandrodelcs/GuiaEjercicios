#!/usr/bin/env python3

def divisores(num):
    lista_divisores = []
    for i in range(1,num+1):
        if num%i == 0:
            lista_divisores.append(i)
    return lista_divisores

def max_com_div(lista_div_1,lista_div_2):
    lista_mcd = []
    for i in lista_div_1:
        if i in lista_div_2:
            lista_mcd.append(i)
    return lista_mcd 

def main():
    numero_1 = int(input('Ingrese un numero: '))
    numero_2 = int(input('Ingrese otro numero: '))
    lista_div_1 = divisores(numero_1)
    lista_div_2 = divisores(numero_2)

    lista_de_divisores = max_com_div(lista_div_1,lista_div_2)

    print(lista_de_divisores)

main()

