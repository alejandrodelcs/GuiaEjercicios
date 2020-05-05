#!/usr/bin/env python3 

import poliraices
import math

def calculo_raices(coef_cuadra, coef_lineal, termino_indep):

    if poliraices.raices_polinomio(coef_cuadra, coef_lineal, termino_indep) == True:
        resultante = pow(2,coef_lineal)-4*coef_cuadra*termino_indep
        resultado_1 = (-1*coef_lineal+ math.sqrt(resultante)) / 2*coef_cuadra
        resultado_2 = (-1*coef_lineal - math.sqrt(resultante)) / 2*coef_cuadra
    else:
        print('No tiene coeficientes reales')
        resultado_1 = 0
        resultado_2 = 0

    return resultado_1,resultado_2

def main():
    coef_cuadra = float(input('Ingrese coeficiente cuadratico: '))
    coef_lineal = float(input('Ingrese coeficiente lineal: '))
    termino_indep = float(input('Ingrese coeficiente independiente: '))

    resultado = calculo_raices(coef_cuadra, coef_lineal, termino_indep)

    print('Resultado: {:.2f},{:.2f} '.format(resultado[0],resultado[1]))

main()