"""Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura de un triángulo: 5
   *
   ***
  *****
 *******
*********
"""
altura=int(input("Introduzca la altura del triángulo: "))
for i in range(altura):
    print (" "*(altura-i-1),((i*2)+1)*"*")
    
