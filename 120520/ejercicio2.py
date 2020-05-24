#!/usr/bin/env python3

def numero_impares(lista_num):
    """
        Función que analiza si cada numero de lista_num es impar
        devuelve una lista de estos
    """
    lista_impares = []
    pos = 0
    while len(lista_impares) !=3 and pos<len(lista_num)-1:
            if lista_num[pos]%2 != 0:
                lista_impares.append(lista_num[pos])
            pos += 1
    if len(lista_impares) < 3:
        lista_impares = ['*']
    return lista_impares

def posiciones_pares(lista_num):
    """
        Función que devuelve una lista con los valores de
        posiciones pares.
    """
    lista_pos_pares =[]
    for pos in range(len(lista_num)):
        if pos%2 == 0:
            lista_pos_pares.append(lista_num[pos])
    return lista_pos_pares

def ordenar_lista(lista_num): 
    """
        Ordena la lista ingresada por el usuario
    """
    return sorted(lista_num, reverse = False) 

def retorno_lista(lista):
    """
        Esta función recibe las listas que retorna la funciones : 
        numeros_impares, posiciones_pares, ordenar_lista.
        Devuelve numero que contiene la lista.
    """
    for num in lista:
        print(num, end = ' ')

def validacion_impares(lista_impares):
    """
        Esta Función valida que se encuentre 3 numeros impares, en caso 
        de encontrarlo los devuelve.
    """
    if lista_impares[0] == '*':
        print('Imposible mostrar impares, no se encontro 3 como maximo...\n')
    else:
        print('\nValores impares hasta el 3er valor inclusive:', end =' ')
        retorno_lista(lista_impares)
        print('\n')
    
def mostrar_listas(lista_impares,lista_pares,lista_ordenada, lista_num):
    """
        Esta función se encarga de llamar a validacion_impares y retorno_lista.
        Retorno lista, devuelve cada valor de la lista.
    """
    linea = 100*('*')
    print(linea)
    validacion_impares(lista_impares)
    print('Elementos de posiciones pares:', end =' ')
    retorno_lista(lista_pares)
    print('\n')
    print('Elementos ordenados de manera ascendente:', end =' ')
    retorno_lista(lista_ordenada)
    print('\n')
    print('Valores ingresados:', end =' ')
    retorno_lista(lista_num)
    print('\n')
    print(linea)

def ingreso_num(lista_num):
    """
        Ingreso del usuario, validacion en caso de que este repetido el numero
        retorna el numero correcto
    """
    repetido =  True
    while repetido == True:
        num = int(input('Ingrese numero: '))
        if num in lista_num:
            print('\n***Ya ingreso {} .***\n'.format(num))
            repetido = True
        else:
            repetido = False
        
    return num 

def ingreso_lista():
    """
        Función que va añadiendo numeros ingresados por el usuario
        termina con 0 en caso de que quiera terminar y lo pasa por parametro
        a las función mostrar_listas. 
    """
    lista_num = []
    print('Termina con cero\n')
    num = ingreso_num(lista_num)
    lista_num.append(num)
    while num!=0:
        print('Termina con cero\n')
        num = ingreso_num(lista_num)
        if num != 0:
            lista_num.append(num)
    mostrar_listas(numero_impares(lista_num),posiciones_pares(lista_num),
                                    ordenar_lista(lista_num),lista_num)

ingreso_lista()





