#!/usr/bin/env python3

def lista_mostrar():
    return [x**2 for x in range(1,101)]

def main():
    print(lista_mostrar())

main()