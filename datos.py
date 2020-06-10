import calendar
import random 

def validacion_temperatura():
    
    temp_minima = None
    temp_maxima = None
    while temp_minima == None and temp_maxima == None:
        try:
            temp_minima =  random.randint(1, 45)
            temp_maxima = random.randint(1, 45)
        except ValueError:
            print('¡Error!. Ingreso una letra y se pide un numero')

    return temp_minima,temp_maxima


def cargar_datos(mes,anio):
    lista_meses = ['Enero', 'Febrero', 'Marzo', 'Abril','Mayo',
                    'Junio','Julio','Agosto','Septiembre','Octubre',
                    'Noviembre', 'Diciembre']
    dicc = {}
    tupla_mes = calendar.monthrange(anio,mes)
    nombre_ciudad = input('Ingrese nombre ciudad: ')
    while nombre_ciudad != '':
        print(lista_meses[mes-1])
        for num in range(1,tupla_mes[1]+1):
            print(num)
            print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
            temp = validacion_temperatura()
            print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
            if nombre_ciudad not in dicc:
                dicc[nombre_ciudad] = [[num,temp[0],temp[1]]]
            else:
                    dicc[nombre_ciudad].append([num,temp[0],temp[1]])
        nombre_ciudad = input('Ingrese nombre ciudad: ')
        

    return dicc
    