#!/usr/bin/env python3
def leer_archivos_csv (archivocsv):
    """Autor : Alejandro"""
    """Ayuda : leer archivos .csv y devuelve una lista de ellos para un mejor estudio"""
    linea = archivocsv.readline()
    return linea.rstrip('\n').split(',') if linea else ""
def grabar_nuevo (archivo,linea):
    """Autor : Alejandro"""
    """Ayuda : genera un archivo unificado, es decir archivo2.csv+archivo1.csv"""
    archivo.write(",".join(linea)+"\n")
def tipo_archivos (archivo):
    """Autor : Alejandro"""
    """Ayuda : valida si el archivo recibido es comentarios o fuente_unico"""
    if "comentarios" in archivo:
        archivo_unico = "comentarios_unificado.csv"
    else:
        archivo_unico = "fuente_unificado.csv"
    return archivo_unico
    
def merge (archivos):
    """Autor : Alejandro"""
    """Ayuda : unifica archivo1.csv y archivo2.csv en un solo archivo"""
    pos = 0
    archivo_x = tipo_archivos(archivos[0])
    while pos+1<len(archivos):
        archivo_1 = archivos[pos]
        archivo_2 = (archivos[pos+1:pos+2])[0]
        archivo_aux = "archivo_aux.csv"
        with open(archivo_1,"r") as archivo1, open(archivo_2,"r") as archivo2,\
            open(archivo_aux,"w") as archivo_mezcla:
                linea_archivo1 = leer_archivos_csv(archivo1)
                linea_archivo2 = leer_archivos_csv(archivo2)
                while linea_archivo1 and linea_archivo2:
                    if linea_archivo1[0] ==  linea_archivo2[0]:
                        grabar_nuevo(archivo_mezcla,linea_archivo1)
                        grabar_nuevo(archivo_mezcla,linea_archivo2)
                        linea_archivo1 = leer_archivos_csv(archivo1)
                        linea_archivo2 = leer_archivos_csv(archivo2)
                    elif linea_archivo1[0] < linea_archivo2[0]:
                        grabar_nuevo(archivo_mezcla,linea_archivo1)
                        linea_archivo1 =leer_archivos_csv(archivo1)
                    else:
                        grabar_nuevo(archivo_mezcla,linea_archivo2)
                        linea_archivo2 = leer_archivos_csv(archivo2)
                while linea_archivo1:
                    grabar_nuevo(archivo_mezcla,linea_archivo1)
                    linea_archivo1 =leer_archivos_csv(archivo1)
                while linea_archivo2:
                    grabar_nuevo(archivo_mezcla,linea_archivo2)
                    linea_archivo2 =leer_archivos_csv(archivo2)
                
        pos += 1
lista_archivos = ["comentarios1.csv","comentarios2.csv","comentarios3.csv"]
merge(lista_archivos)



        


    
