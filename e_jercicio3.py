#!/usr/bin/env python3

'''Ejercicio 3
Escribir una función que reciba una dirección de mail, y devuelva True ó False, en función de haber evaluado que dicha dirección está bien formada.
Escribir una función que reciba una cadena de caracteres que representa una dirección de mail. La función deberá devolver True ó False, en función de  haber evaluado que dicha dirección está bien formada.
Se debe controla que: 
a.	Que no contenga blancos
b.	Que sólo se utilicen letras y/o números para la parte del nombre, delante de la @
c.	Que haya exactamente una arroba'''

def validacion_mail(email):
    if ' ' in email:
        valido = False 
    elif email.count('@') != 1:
        print(email.count('@'))
        valido = False
    elif not (email[email.index('@'):]).isalnum():
        valido = False
    elif email[email.index('@'):] !=  '@fi.uba.ar' and email[email.index('@'):] !=  '@gmail.com':
        print('no es dominio')
        valido = False
    else:
        valido = True

    return valido
    

def main():
    mail = input('Ingrese mail: ')
    print(validacion_mail(mail))


main()