"""
Escribir un programa que lea una frase, y pase ésta como parámetro a una 
función que debe contar el número de palabras que contiene. 
Debe imprimir el programa principal el resultado. Asumir que cada palabra 
está separada por un solo blanco:

a.Asumir que cada palabra está separada por un solo blanco.
b.No se sabe cómo están separadas las palabras. 
Pueden estar separadas por más de un blanco o por signos de puntuación.

Sergio Torres Cano
"""

def f(a):
    o=1
    posibilidades=" ,.¿?!¡;:"
    for i in range (len(frase)):
        if i>0 and i<len(frase)-1:
            if frase[i]in posibilidades and frase[i+1] in posibilidades:
                o=o
            elif frase[i] in posibilidades:
                o+=1
    return o
frase=(input("Dime una frase: "))
print (f(frase))