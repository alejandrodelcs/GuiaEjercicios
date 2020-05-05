#!/usr/bin/env python3

from funciones import expo

def main():
    base =  float(input('ingrese base: '))
    exponente = float(input('Ingrese exponente: '))

    resultado = expo.calculo_exponente(base, exponente)
    print(resultado)

main()