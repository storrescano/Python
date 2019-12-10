notas=float(input("Introduzca una nota: "))
lista=[]
while notas<=10 and notas>=0:
    lista+=[notas]
    notas=float(input("Introduzca una nota: "))
print ("Las notas que has escrito son: ", end='')
print (lista)
