#!/usr/bin/env python3
""" 
    Ejercicio 2
    Solicite al usuario el ingreso de un texto.
    Considerar que el usuario solo ingresa palabras separadas por blancos,
    sin ningún otro tipo de caracteres. De las palabras ingresadas,
    descartar las que tienen tres letras o menos y las que tienen 10 letras
    o más, además de las repetidas.
    Luego, mostrar una lista de las palabras que quedaron ordenadas,
    en primer lugar por cantidad de letras (de menor a mayor) y,
    a igual cantidad de letras, alfabéticamente.
"""

def ingreso_palabras():
    texto = input("Ingrese texto: ")
    return texto.split()

def validacion_texto(texto):
    for palabra in texto:
        if len(palabra)<= 3 or len(palabra)>=10 or texto.count(palabra) > 1:
            texto.remove(palabra)
    return text



    
            

    
            

texto = ingreso_palabras()
texto_modificado = validacion_texto(texto)
print(texto_modificado)

            
