"""Escribe un programa que pida primero dos números (máximo y mínimo)
y que después te pida números intermedios. Para terminar de escribir números,
escribe un número que no esté comprendido entre los dos valores iniciales.
El programa termina escribiendo la lista de números.

Escribe un número: 6
Escribe un número mayor que 6: 4
4 no es mayor que 6. Vuelve a probar: 50
Escribe un número entre 6 y 50: 45
Escribe otro número entre 6 y 50: 13
Escribe otro número entre 6 y 50: 4
Los números situados entre 6 y 50 que has escrito son: 45, 13
Sergio Torres Cano
"""
minimo=int(input("Escribe un número: "))
maximo=int(input("EScribe un número mayor que %d: " %(minimo)))
lista=[]
while minimo==maximo or minimo>maximo:
    maximo=int(input("%d no es mayor que%d. Vuelve a probar: " %(maximo,minimo)))
if minimo<maximo:
    entre=int(input("Escribe un número entre %d y %d: " %(minimo,maximo)))
    lista+=[entre]
    while entre<maximo and entre>minimo:
        entre=int(input("Escribe otro número entre %d y %d: " %(minimo,maximo)))
        if entre<maximo and entre>minimo:
            lista+=[entre]
print ("Los números entre %d y %d que has escrito son: " %(minimo,maximo),end='')
for i in range (len(lista)):
    if i<(len(lista)-1):
        print (lista[i], end=', ')
    else:
        print (lista[i])
    
        

