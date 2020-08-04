#!/usr/bin/env python3

def leer(ar_programa):
    linea = ar_programa.readline()

    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = ""
    return devolver 
def listar_archivo():
    ar_programa = open('validacionmail.py','r')
    ar_programa_txt = open('validacion2.txt','r+')
    linea = leer(ar_programa)
    pos = 0
    #Lectura total del archivo linea a linea
    while linea:
        if "#" not in linea[0]:
            ar_programa_txt.write(linea[0]+"\n")
        linea = leer(ar_programa)
    ar_programa.close()
    ar_programa_txt.close()
    
listar_archivo()
