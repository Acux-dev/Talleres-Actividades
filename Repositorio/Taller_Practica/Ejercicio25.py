valor = int(input("Ingrese el valor de la compra: "))
if valor>150000:
    valor = (valor*1.19)
    valor = valor*0.95
else:
    valor = valor*1.19
print("El valor final a pagar es: ", valor)