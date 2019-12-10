"""
Escribe un programa que te pida una palabra o número, 
pase por parámetro estos datos a una función, y ésta te diga 
si es o no palíndroma o capicúa. El programa principal 
imprimirá el resultado de la función:

Sergio Torres Cano
"""

def f(a):
    b=""
    for i in range (len(a)-1,-1,-1):
        b+=a[i]
    if b==a:
        print ("%s es capicúa o palíndroma." %(a))
        return True
    else:
        print ("%s no es capicúa o palíndroma." %(a))
        return True

algo=input("Dime algo: ")
print (f(algo))