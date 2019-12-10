a=int(input("Introduce el primer número: "))
b=int(input("Introduce el segundo número: "))
c=int(input("Introduce el tercer número: "))
d=int(input("Introduce el cuarto número: "))
e=int(input("Introduce el quinto número: "))
if a<b<c<d<e:
    print ("Estos números están en orden creciente.")
elif a>b>c>d>e:
    print ("Estos números están en orden decreciente.")
else:
    print ("EStos números están desordenados.")
    
