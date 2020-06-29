#!/usr/bin/env python3
from corredores import raners

def promedio_km_corridos(raners):
    cont = 0
    acum = 0
    for nombre in raners:
        acum += raners[nombre][1]
        cont += 1
    return acum/cont

def corredores_ordenados_por_velocidad_prom(raners):
    l_corredores = []
    for nombre in raners:
        velocidad_promedio = raners[nombre][0]/raners[nombre][1]
        l_corredores.append([nombre,velocidad_promedio])
    
    return sorted(l_corredores, key=lambda velocidad:velocidad[1],reverse=True)

promedio = promedio_km_corridos(raners)
print("El promedio corrido por los corredores es: {}".format(promedio))
lista_corredores = corredores_ordenados_por_velocidad_prom(raners)
for pos in lista_corredores:
    print("Nombre: {} - Velocidad: {} (Km/min)".format(pos[0],pos[1]))



