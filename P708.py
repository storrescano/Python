"""
Escribe un programa que pida una frase, y pase la frase 
como parámetro a una función que debe eliminar los espacios en 
blanco (compactar la frase). El programa principal imprimirá 
por pantalla el resultado final.

Sergio Torres Cano
"""

def f(frase):
    final=""
    for i in range (len(frase)):
        if frase[i]!=" ":
            final+=frase[i]
    return final
frase=input("Introduzca una frase: ")
print (f(frase))