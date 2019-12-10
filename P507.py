"""Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
****
***
**
*
"""
altura=int(input("Introduzca la altura del triangulo: "))
for i in range (altura,0,-1):
    for j in range (i):
        print ("*", end='')
    print("")
    
    
