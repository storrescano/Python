"""Escribe un programa que lea el nombre y los dos apellidos de una persona 
(en tres cadenas de caracteres diferentes), los pase como parámetros a una 
función, y ésta debe unirlos y devolver una única cadena. La cadena final 
la imprimirá el programa por pantalla.

Sergio Torres Cano
"""

nombre=input("Introduzca el nombre: ")
apellido1=input("Introduzca el primer apellido: ")
apellido2=input("Introduzca el segundo apellido: ")
def unir(nombre):
    nombre=nombre+apellido1+apellido2
    print(nombre)
print (unir(nombre))