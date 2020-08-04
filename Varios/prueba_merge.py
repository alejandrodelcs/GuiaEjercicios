#!/usr/bin/env python3
from mezcla import merge 

def prueba(lista_archivos):
    pos = 0
    while pos+1<len(lista_archivos):
        archivo1 = lista_archivos[pos]
        archivo2 = (lista_archivos[pos+1:pos+2])[0]
        print(archivo1)
        print(archivo2)
        archivo_aux = 'archivo_aux'
        archivo_nuevo = archivo2[0]
        pos += 1



lista_archivos = ["comentarios1.csv","comentarios2.csv","comentarios3.csv","comentarios4.csv"]
prueba(lista_archivos)