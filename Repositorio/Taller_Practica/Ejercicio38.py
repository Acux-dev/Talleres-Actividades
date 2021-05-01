num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
num3 = int(input("Ingrese el numero 3: "))
if num1>num2>num3:
    print("Los numeros estan disminuyendo.")
elif num1<num2<num3:
    print("Los numeros estan aumentando.")
else:
    print("Los numeros no tienen orden.")