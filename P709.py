"""
Escribe un programa que pida dos palabras las pase 
como parámetro a un procedimiento y diga si riman o no. 
Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman 
un poco y si no, que no riman.

Sergio Torres Cano
"""

def r(a,b):
    if a[-2]==b[-2] and a[-1]==b[-1]:
        if a[-3]==b[-3]:
            print ("Las palabras %s y %s riman" %(a,b))
        else:
            print ("Las palabras %s y %s riman un poco" %(a,b))
    else:
        print ("Las palabras %s y %s no riman" %(a,b))
palabra=input("Dime una palabra: ")
palabra2=input("Dime otra palabra: ")
print (r(palabra,palabra2))