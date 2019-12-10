#Escribe un programa que pida un número y escriba si primo o no
primo=int(input("Introduzca un número primo: "))
resultado=0
for i in range (1,primo):
    if primo%i==0:
        resultado+=1
if resultado==1:
    print ("El número %d es primo." %(primo))
else:
    print ("El número %d no es primo." %(primo))
