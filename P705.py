"""Escribe un programa que te pida una frase y una vocal, 
y pase estos datos como parámetro a una función que se encargará 
de cambiar todas las vocales de la frase por la vocal seleccionada. 
Devolverá la función la frase modificada, y el programa principal la imprimirá:

Sergio Torres Cano
"""

def v(frase,vocal):
    vocales="aeiou"
    final=""
    for i in range (len(frase)):
        if frase[i] in vocales:
            final+=vocal
        else:
            final+=frase[i]
    return final
frase=input("Introduzca una frase: ")
vocal=input("Introduzca una vocal: ")
print (v(frase,vocal))