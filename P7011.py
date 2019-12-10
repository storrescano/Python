"""
Escribe un programa que te pida una frase, y pase la frase 
como parámetro a una función. Ésta debe devolver si es palíndroma o no , 
y el programa principal escribirá el resultado por pantalla:

Sergio Torres Cano
"""

def f(a):
    b=""
    c=""
    for i in range (len(a)-1,-1,-1):
        if a[i]!=" ":
            b+=a[i]
    for i in range (len(a)):
        if a[i]!=" ":
            c+=a[i]
    if c==b:
        print (f"{a} es palíndroma.")
        return True
    else:
        print (f"{a} no es palíndroma.")
        return True

frase=input("Dime una frase: ")
print (f(frase))