def mes(a):
    dia=a[0:2]
    mes=a[3:5]
    año=a[6:]
    d={"01": "Enero",
    "02": "Febrero",
    "03": "Marzo",
    "04": "Abril",
    "05": "Mayo",
    "06": "Junio",
    "07": "Julio",
    "08": "Agosto",
    "09": "Septiembre",
    "10": "Octubre",
    "11": "Noviembre",
    "12": "Diciembre",
    }
    print (f"{dia} de {d[mes]} de {año}")
        


fecha=input("Introduzca una fecha en formato dd/mm/aaaa: ")
print (mes(fecha))