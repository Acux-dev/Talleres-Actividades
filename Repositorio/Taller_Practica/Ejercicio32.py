def valor_pagar(km,dias):
    total=km*5000
    return total

km=int(input("Ingrese los km a recorrer: "))
dias=int(input("Ingrese los dias que se quedara: "))

if km<20:
    print("son muy pocos km")
    exit

valor_a_pagar = valor_pagar(km,dias)
print(f'El total a pagar es: {valor_a_pagar}')

if km>=1000 and dias>=7:
    descuento=valor_a_pagar*0.15
    print("se le aplico un descuento de: ",descuento)