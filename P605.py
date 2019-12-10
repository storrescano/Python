"""Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. Para acabar de escribir los números, escribe un número que no sea mayor que el anterior. El programa termina escribiendo la lista de números:
Escribe un número: 6
Escribe un número mayor que 6: 10
Escribe un número mayor que 10: 12
Escribe un número mayor que 12: 25
Escribe un número mayor que 25: 9
Los números que has escrito son: 6, 10, 12, 25  (Comentario si os fijáis ya no se imprime la lista tal cual, hay que imprimir uno por uno los valores de la lista, haced esto así a partir de ahora)
Sergio Torres Cano
"""
numero=int(input("Escribe un número: "))
lista=[numero]
i=0
numero=int(input("Escribe un número mayor que %d: " %(lista[i])))
if numero>lista[i]:
    lista+=[numero]
    while numero>lista[i]:
        i+=1
        numero=int(input("Escribe un número mayor que %d: " %(lista[i])))
        if numero>lista[i-1]:
            lista+=[numero]
print ("Los números escritos son: ", end='')
for i in range(len(lista)):
    if i<(len(lista)-1):
        print (lista[i], end=', ')
    else:
        print (lista[i], end='')
    
               
