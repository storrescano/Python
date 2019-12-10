"""Desarrolla un programa utilizando la metodología “pair programming”, 
que nos sirva para gestionar nuestros contactos (la información a 
gestionar será el teléfono, nombre, apellido1, apellido2 y correo electrónico. 
El programa tendrá un menú, con las siguientes opciones: añadir contacto, 
consultar contacto a partir de la clave, consultar todos los contactos 
y eliminar contacto. Aprovecha lo que has aprendido hasta el momento 
(diccionarios, funciones, procedimientos…).

Sergio Torres Cano
"""

def añadir(d):
    tel=int(input("Introduzca un número de télefono: "))
    dat=input("Introduzca los datos (nombre, apellidos y correo eléctronico: ")
    d[tel]=dat
def contacto1(d):
    tel=(input("Introduzca el número de télefono del contacto que busca: "))
    elem=d.get(tel)
    return elem
def contacto2(d):
    for i,j in d.items():
        print (f"{d[i]},{d[j]}")
d=dict()
b=""
while b=="":
    ask=input("¿Que desea hacer?\
        \n1.Añadir contacto\
        \n2.Consultar un contacto mediante una clave\
        \n3.Consultar todos los contactos \
        \n4.Eliminar un contacto \
        \n5.Pulse enter para salir.\
        \nRespuesta: ")
    if ask=="1":
        añadir(d)
    elif ask=="2":
        print(contacto1(d))
        
        