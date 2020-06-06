#!/usr/bin/env python3
# Búsqueda secuencial / Linear search 

def busq_binaria(pajar, aguja):
    n = len(pajar)
    
    min = 0
    max = n
    
    res = None
    
    while (min < max and res == None):
        med = (min+max)//2
        if pajar[med] == aguja:
            res = med
        elif pajar[med] < aguja:
            min = med + 1
        else: # pajar[med] > aguja
            max = med - 1      
    return res



l = [1, 2, 3, 4, 5]  # ordenado!
print(busq_binaria(l, 5))