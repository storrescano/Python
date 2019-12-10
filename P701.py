"""Escribe un programa que pida un texto por pantalla, 
este texto lo pase como parámetro a un procedimiento, 
y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.

Sergio Torres Cano
"""
def m(texto):
    print(texto.lower())
    print(texto.upper())
texto=input("Introduzca una frase: ")
print (m(texto))
