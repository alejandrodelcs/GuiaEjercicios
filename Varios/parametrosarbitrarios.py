#!/usr/bin/env python3

def parametros_arbitrarios(*parametros,**parametros2):
    print(parametros)
    print(parametros2)
    for i in parametros:
        print(i)

parametros_arbitrarios('perro','gato','perro','mono',mexico='agua',argentina='pasto')
