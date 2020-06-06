#!/usr/bin/env python3

def cant_letras_numeros(clave):
    num_cadena = [x for x in clave if x.isdigit()]
    let_cadena = [y for y in set(clave.lower()) if y.isalpha()]
    if len(let_cadena) > len(num_cadena):
        valido = True
    else:
        valido = False 

def caracteres_validacion(clave):
    if clave[:1].isdigit() == True and clave[-3:len(clave)].isdigit() == False:
        valido = True
    else:
        valido = False 

def sumar_numeros(clave):
    suma = 0
    if cant_letras_numeros(clave) == True and caracteres_validacion(clave) == True:
        for caracter in clave: 
            if caracter.isdigit():
                suma += int(caracter)
    return suma 


def ingreso_clave(clave):

    if len(clave) >=8 and len(clave)<=12 and sumar_numeros(clave)<35:
        valido = True
    else:
        valido = False 

    return valido

clave = '123654'
print(ingreso_clave(clave))