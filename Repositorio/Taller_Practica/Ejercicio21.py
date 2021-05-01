numero = int(input("Ingresa un numero de 4 cifras: "))
n1 = numero%10
n2 = int((numero%100)/10)
n3 = int((numero%1000)/100)
n4 = int((numero-(numero%1000))/1000)
print(n1,n2,n3,n4)