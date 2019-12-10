"""Escribe un programa que pida un número (límite) y
luego te pida números hasta que la suma de los números
introducidos supere el límite inicial.
El programa termina escribiendo la lista de números.

Escribe límite: 50
Escribe un valor: 10
Escribe otro valor: 25
Escribe otro valor: 7
Escribe otro valor: 14
El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56
Sergio Torres Cano
"""

numero=int(input("Escribe límite: "))
otro=int(input("Escribe un valor: "))
lista=[]
suma=otro
while suma<=numero:
    lista+=[otro]
    otro=int(input("Escribe un valor: "))
    suma+=otro
print ("El limite a superar es 50. La lista creada es ",end='')
for i in range(len(lista)):
    if i<(len(lista)-1):
        print (lista[i], end=', ')
    else:
        print (lista[i], end=' ')
print ("ya que la suma de estos números es: %d" %(suma))
