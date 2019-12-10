"""Escribe un programa que lea una frase, y la pase como 
parámetro a un procedimiento. El procedimiento contará 
el número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla.

Sergio Torres Cano"""

def f(frase):
    a=0
    e=0
    j=0
    o=0
    u=0
    for i in range(len(frase)):
        if frase[i]=="a" or frase[i]=="A":
            a+=1
        elif frase[i]=="e" or frase[i]=="E":
            e+=1
        elif frase[i]=="i" or frase[i]=="I":
            j+=1
        elif frase[i]=="o" or frase[i]=="O":
            o+=1
        elif frase[i]=="u" or frase[i]=="U":
            u+=1
    print ("Hay %d vocales a: " %(a))
    print ("Hay %d vocales e: " %(e))
    print ("Hay %d vocales i: " %(j))
    print ("Hay %d vocales o: " %(o))
    print ("Hay %d vocales u: " %(u))

frase=input("Introduzca una frase: ")
print (f(frase))