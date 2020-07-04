"""
Escribir una función que reciba dos cadenas de caracteres y si la primer cadena se encuentra dentro de la segunda cadena,
debe devolver la posicion del caracter de la segunda cadena, en la cual comienza la primer cadena.
Si en cambio, la primer cadena no se encuentra en la segunda cadena, debe devolver -1.

No puede utilizar para esta solución, ninguno de los métodos provistos por el lenguaje para el tratamiento de cadenas, como: find, index, rindex, etc.

Deberá comprobar el correcto funcionamiento, mediante los siguientes casos de prueba usando la librería doctest.

Para ("ritmo", "Algoritmos"), debe devolver 4
Para ("Pre", "Presidente"), debe devolver 0
Para ("ción", "Estación"), debe devolver 4
Para ("ato", "Patos"), debe devolver 1
Para ("s", "Patos"), debe devolver 4
Para ("M", "M"), debe devolver 0
Para ("Cuarentena", "Cua"), debe devolver -1
Para ("juicios", "Prejuicio"), debe devolver -1
Para ("pa", "preparación"), debe devolver 3

"""

def validar_clave(cadena_uno, cadena_dos):
    
    """ Casos de Prueba:

    >>> validar_clave("ritmo", "Algoritmos")
    4
    >>> validar_clave("Pre", "Presidente")
    0
    >>> validar_clave("ción", "Estación")
    4
    >>> validar_clave("ato", "Patos")
    1
    >>> validar_clave("s", "Patos")
    4
    >>> validar_clave("M", "M")
    0
    >>> validar_clave("Cuarentena", "Cua")
    -1
    >>> validar_clave("juicios", "Prejuicio")
    -1
    >>> validar_clave("pa", "preparación")
    3
    """
    condicion = True
    indice_dos = 0
    
    
    while condicion and indice_dos < len(cadena_dos):
        if cadena_uno in cadena_dos[:indice_dos]:
            condicion = False
        else:
            indice_dos += 1
            
    return indice_dos - len(cadena_uno)
    
    
    
    
    
    
        
    
    
    

            
        
        
        
          
    
  
        
    
    
    





import doctest
doctest.testmod()
    
        

