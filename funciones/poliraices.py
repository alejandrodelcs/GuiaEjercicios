#!/usr/bin/env python3

def raices_polinomio(coef_cuadra, coef_lineal, termino_indep):
    resultante =  pow(2,coef_lineal)-4*coef_cuadra*termino_indep

    if resultante > 0:
        raices_reales = True
    else:
        raices_reales = False

    return raices_reales
