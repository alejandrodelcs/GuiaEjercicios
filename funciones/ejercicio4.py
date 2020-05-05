#!/usr/bin/env python3

from numeroprimo import es_primo

def resultado_primo(resultado):
    if resultado == True:
        print('El numero es primo')
    else:
        print('El numero no es primo')

def main():
    numero = int(input('Ingrese un numero: '))
    resultado = es_primo(numero)
    resultado_primo(resultado)
main()
