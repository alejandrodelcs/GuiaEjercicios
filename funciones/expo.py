#!/usr/bin/env python3


def calculo_exponente(base, exponente):
    resultado = 1
    if exponente > 0 and base > 0:
        for num in range(1,int(exponente)+1):
            resultado =  resultado*base
    elif exponente < 0:
            resultado = (-1*exponente)/base
    return resultado

