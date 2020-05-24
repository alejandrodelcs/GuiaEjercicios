#!/usr/bin/env python3

def ordburbuja(lista):
    for dato in range(len(lista)-1,0,-1):
        for i in range(dato):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                print(temp)


lista = [72,8,86,79,46,10,37,40,19]
ordburbuja(lista)
print(lista)