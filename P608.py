"""Escribe un programa que te pida primero un número
y luego te pida números hasta que la suma de los números
introducidos coincida con el número inicial.
El programa termina escribiendo la lista de números.

Escribe límite: 50
Escribe un valor: 10
Escribe otro valor: 45
45 es demasiado grande. Escribe otro valor: 1
Escribe otro valor: 39
El límite a alcanzar es 50. La lista creada es: 10, 1, 39
Sergio Torres Cano
"""
limite=int(input("Escribe límite: "))
numero=int(input("Escribe un valor: "))
lista=[numero]

suma=numero
while suma!=limite:
    if suma>limite:
        suma-=numero
        numero=int(input("%d es demasiado grande. Escribe otro valor: " %(numero)))
        if (suma+numero)<=limite:
            lista+=[numero]
    else:
        numero=int(input("Escribe otro valor: "))
        if (suma+numero)<=limite:
            lista+=[numero]
    suma+=numero
print ("El límite a alcanzar es %d. La lista creada es: " %(limite), end='')
for i in range(len(lista)):
    if i<(len(lista)-1):
        print (lista[i], end=', ')
    else:
        print (lista[i])
    
