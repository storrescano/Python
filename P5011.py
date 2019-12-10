#Escribe un programa que pida un número e imprima todos sus divisores.
divisores=int(input("Introduzca un número para sacar sus divisores: "))
print ("Los divisores de %d son: " %(divisores), end='')
for i in range (1,divisores):
    if divisores%i==0:
        print (i, end=' ')
