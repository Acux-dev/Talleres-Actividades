numero=int(input("Ingrese el numero a revisar: "))
if numero == 0:
    print("el numero es 0")
elif numero > 0:
    print("el numero es positivo")
else:
    print("el numero es negativo")
if (numero%2) == 0:
    print("y el numero es par")
else:
    print("y el numero es impar")