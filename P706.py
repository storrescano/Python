"""Escribe un programa que lea el nombre de una persona y un carácter, 
le pase estos datos a una función que comprobará si dicho carácter 
está en su nombre. El resultado de dicha función lo imprimirá 
el programa principal por pantalla.

Sergio Torres Cano
"""

def t(nombre,caracter):
    j=0
    retorno=False
    for i in range (len(nombre)):
        if nombre[i] in caracter:
            j+=1
        if j>=1:
            retorno=True
    return retorno
nombre=input("Introduzca un nombre: ")
caracter=input("Introduzca un carácter: ")
print (t(nombre,caracter))