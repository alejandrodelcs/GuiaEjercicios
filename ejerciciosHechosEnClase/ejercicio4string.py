#!/usr/bin/env python3

def palabra_ordenada(palabra):
    letras_palabra = list(palabra)
    letras_palabra_ordenada = sorted(letras_palabra, reverse = False)

    if letras_palabra == letras_palabra_ordenada:
        ascendente = True
    else:
        ascendente = False
    return ascendente

def main():
    palabra = input('Ingrese palabra: ')
    resultado = palabra_ordenada(palabra)
    print('Ascendente: {}'.format(resultado))


main()