#!/usr/bin/env python3

numero = float(input('Ingrese numero: '))
exponente = float(input('Ingrese exponente: '))

mult = 1

if exponente > 0 and exponente%2 == 0:
    for i in range(1,int(exponente)+1):
        mult=mult*exponente
    print('{}^{} = {}'.format(numero,exponente,mult))
elif exponente >0 and exponente%2 != 0:
    for i in range(1,int(exponente)+1):
        mult=mult*exponente
    print('{}^{} = {}'.format(numero,exponente,mult))
elif exponente < 0:
    conv =  (-1*(exponente))/numero
    print(conv)
    print('{}^({}) = {}'.format(numero,exponente,conv))
elif exponente == 0 and numero!= 0:
    print('{}^{} = {}'.format(numero,exponente,1))
elif exponente == 0 and numero == 0:
    print('MATH ERROR')


'''NO ES OPTIMO LO MEJOR ES HACER UNA FUNCIÓN, TERMINO ACA Y CONTINUO EL SGTE TEMA, 
YA QUE ME PARECE QUE LOS EJERCICIOS A SEGUIR PUEDEN SER OPTIMIZADOS CON OTRAS COSAS'''