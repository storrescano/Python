a=int(input("Introduzca un número: "))
if a>=1000 or a<=-1000:
    print ("ERROR: El número %d tiene más de tres cifras." %(a))
else:
    print ("El número introducido es %d" %(a))
