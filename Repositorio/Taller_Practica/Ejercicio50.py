i=1
num = int(input("Ingrese la cantidad de numeros a sumar y promediar: "))
suma=0
while (num+1)>i:
    n= int(input("Ingrese el valor "+str(i)+": "))
    i+=1
    suma+=n
print("La suma es ",suma)
print("El promedio es ",suma/num)