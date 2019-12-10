"""Escribe un programa que lea una frase, y la pase como parámetro 
a un procedimiento, y éste debe mostrar la frase con un carácter en cada línea.

Sergio Torres Cano
"""

def t(frase):
    for i in range (len(frase)):
        print (frase[i])

frase=input("Introduzca una frase: ")
print (t(frase))