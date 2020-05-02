#!/usr/bin/env python3

def maximo_comun_divisor(num1, num2):
    if num1>num2:
        resto =  int(num1%num2)
        cociente = int(num1/num2)
        while resto != 0:
            aux = num1
            num1 = num2
            num2 = aux 
            num2 = resto

            cociente = int(num1/resto)
            resto =  int(num1%resto)    
    else:
        num2 = 0   
    return num2
        

def main():
    
    num1 = int(input('Ingrese un numero: '))
    num2 = int(input('Ingrese otro numero: '))
    resultado = maximo_comun_divisor(num1,num2)
    if resultado != 0:
        print('El MCD de {} y {} es: {} '.format(num1,num2,resultado))
        print('EL MCM de {} y {}  es: {}'.format(num1,num2, int(num1*num2/resultado)))
    else:
        print('No es lo que esperaba')

main()