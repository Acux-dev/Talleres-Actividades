num = int(input("Ingrese un numero del 1 al 7 para representar un dia de la semana: "))
if num<0 and num>7:
    exit()

if num==1:
    print("lunes")
elif num==2:print("Martes")
elif num==3:print("Miercoles")
elif num==4:print("Jueves")
elif num==5:print("Viernes")
elif num==6:print("Sabado")
elif num==7:print("Domingo")