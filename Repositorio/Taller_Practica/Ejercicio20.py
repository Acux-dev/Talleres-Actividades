Dinero = int(input("Ingrese la cantidad de dinero a analizar, en miles: "))
C1 = C2 = C3 = C4 = C5 = C6 = C7 = 0
while Dinero >= 100:
    C1 = C1 + 1
    Dinero = Dinero - 100
    if Dinero < 100:
      break
while Dinero >= 50:
    C2 = C2 + 1
    Dinero = Dinero - 50
    if Dinero < 50:
      break
while Dinero >= 20:
    C3 = C3 + 1
    Dinero = Dinero - 20
    if Dinero < 20:
      break
while Dinero >= 10:
    C4 = C4 + 1
    Dinero = Dinero - 10
    if Dinero < 10:
      break
while Dinero >= 5:
    C5 = C5 + 1
    Dinero = Dinero - 5
    if Dinero < 5:
      break
while Dinero >= 2:
    C6 = C6 + 1
    Dinero = Dinero - 2
    if Dinero < 2:
      break
while Dinero >= 1:
    C7 = C7 + 1
    Dinero = Dinero - 1
    if Dinero < 1:
      break
print("La menor cantidad de billetes de cada denominación que se puede entregar son: ")
print(C1, " billete(s) de 100k")
print(C2, " billete(s) de 50k")
print(C3, " billete(s) de 20k")
print(C4, " billete(s) de 10k")
print(C5, " billete(s) de 5k")
print(C6, " billete(s) de 2k")
print(C7, " billete(s) de 1k")