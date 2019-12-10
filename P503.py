primero=int(input("Introduce un número: "))
segundo=int(input("Introduce otro número:"))
sumatorio=0
if primero<segundo:
    for i in range (primero, segundo):
        sumatorio+=i;
    print (sumatorio)
elif segundo<primero:
    for i in range (segundo, primero):
        sumatorio+=i;
    print (sumatorio)
else:
    print ("Los números introducidos son iguales")
