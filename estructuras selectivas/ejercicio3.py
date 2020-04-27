#!/usr/bin/env python3
hora_par = 20
min_par=10
seg_par=3

hora_lleg=50
min_lleg=20
seg_lleg=8

conv_hora_part=hora_par+min_par/60+seg_par/3600
conv_hora_lleg=hora_lleg+min_lleg/60+seg_lleg/3600

dist = float(input('Ingrese distancia: '))

velocidad = dist/(conv_hora_lleg-conv_hora_part)

print('Velocidad del móvil: {} km/h'.format(velocidad))