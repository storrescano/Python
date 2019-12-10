"""Escribe un programa que pida una frase, y le pase como parámetro 
a una función dicha frase. La función debe sustituir todos los espacios 
en blanco de una frase por un asterisco, y devolver el resultado 
para que el programa principal la imprima por pantalla.

Sergio Torres Cano
"""

def t(frase):
    final=""
    for i in range (len(frase)):
        if frase[i]==" ":
            final+="*"
        else:
            final+=frase[i]
    return final

frase=input("Introduzca una frase: ")
print (t(frase))