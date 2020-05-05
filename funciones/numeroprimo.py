#!/usr/bin/env python3


def es_primo(numero):
    divisor = 2
    while ((numero % divisor) != 0) and (divisor <= numero/2):
        divisor += 1
    if (numero >1 ) and (divisor > numero/2):
        primo = True
    else:
        primo = False
    
    return primo

