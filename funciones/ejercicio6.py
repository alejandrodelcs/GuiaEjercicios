#!/usr/bin/env python3

from numeroprimo import es_primo

def descomposicion_primos(numero_usr):
    numero = 1
    lista_primos = []
    bandera = True
    while es_primo(numero) == True or bandera == True:
        if int(numero_usr%numero) == 0:
            cociente = int(numero_usr/numero)
            numero_usr =  cociente
            lista_primos.append(numero)
        elif int(numero_usr/numero) == 1:
            bandera = False
        else:
            numero += 1
    print(numero)

def main():
    numero_usr = int(input('Ingrese numero: '))
    descomposicion_primos(numero_usr)


main()



