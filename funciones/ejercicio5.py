#!/usr/bin/env python3

from numeroprimo import es_primo

def imprime_numeros_primos(numero):

    for num in range(2,numero+1):
        resultado = es_primo(num)
        if resultado == True:
            print(num)


def main():
    print('Mostrara los numeros primos hasta el numero que ingrese.')
    numero = int(input('Ingrese numero: '))
    imprime_numeros_primos(numero)

main()
