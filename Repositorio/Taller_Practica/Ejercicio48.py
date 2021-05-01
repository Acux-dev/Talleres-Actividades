n = int(input("Ingrese el valor de n: "))
m = int(input("Ingrese el valor de m: "))
suma = 0
if m>n:
    for i in range(n+1,m):
        suma+=i
else:print("Los valores ingresados no son validos, m es menor que n")
print(suma)