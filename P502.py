primero=int(input("Introduce un número: "));
segundo=int(input("Introduce otro número: "));
if primero<segundo:
    for i in range (primero, segundo):
        if i%2==0:
            print ("El número %d es par" %(i));
        else:
            print ("El número %d es impar" %(i));
elif segundo<primero:
    for i in range (segundo, primero):
        if i%2==0:
            print ("El número %d es par" %(i));
        else:
            print ("El úmero %d es impar" %(i));
else:
    print ("Los números son iguales");
