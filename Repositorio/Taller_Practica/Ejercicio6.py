#ejercicio 6
valor = 0
definitiva = 0
contador = 0
while contador < 5:
    n = float(input("ingrese el valor de la nota: "))
    decimal = float(input("ingrese el valor del decimal a multiplicar: "))
    valor = (n*decimal)
    definitiva = (definitiva + valor)
    contador = contador + 1
print("su definitiva es: ", definitiva)