#!/usr/bin/env python3

def contar_palabras(primera_cadena, segunda_cadena, letra):
    frase =  primera_cadena + segunda_cadena
    return frase.count(letra)

def main():
    palabra_1 = input('Ingrese palabra: ')
    palabra_2 = input('Ingrese segunda palabra: ')
    letra = input('Ingrese tercera letra: ')
    
    print('La frase "{}" tiene {} {}'.format(palabra_1+' '+palabra_2,
                                        contar_palabras(palabra_1, palabra_2, letra), letra))
    
main()