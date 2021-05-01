año = int(input("ingrese el año a analizar: "))
if año%4!=0:
    print("no es bisiesto")
elif año%4 ==0 and año%100!=0:
    print("es bisiesto")
elif año%4==0 and año%100==0 and año%400!=0:
    print("no es bisisesto")
elif año%4==0 and año%100==0 and año%400==0:
    print("es bisisesto")