dia=int(input("Introduce el dia: "))
mes=int(input("Introduce el mes: "))
año=int(input("Introduce el año: "))
if año<0:
    print ("La fecha %d/%d/%d es incorrecta." %(dia,mes,año))
else:
    if mes == 1 or mes == 3 or mes ==5 or mes == 7 or mes == 8 or mes == 10 or mes ==12:
        if dia>31 or dia<=0:
            print ("La fecha %d/%d/%d es incorrecta." %(dia,mes,año))
        else:
            print ("La fecha %d/%d/%d es correcta." %(dia,mes,año))
    elif mes==2:
        if dia>28 or dia<=0:
            print ("La fecha %d/%d/%d es incorrecta." %(dia,mes,año))
        else:
            print ("La fecha %d/%d/%d es correcta." %(dia,mes,año))
    elif mes==4 or mes == 6 or mes == 9 or mes == 11:
        if dia>30 or dia<=0:
            print ("La fecha %d/%d/%d es incorrecta." %(dia,mes,año))
        else:
            print ("La fecha %d/%d/%d es correcta." %(dia,mes,año))
    else:
        print ("La fecha %d/%d/%d es incorrecta." %(dia,mes,año))
