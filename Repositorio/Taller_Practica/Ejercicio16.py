X1 = int(input("ingrese el valor de la coordenada X1: "))
X2 = int(input("ingrese el valor de la coordenada X2: "))
Y1 = int(input("ingrese el valor de la coordenada Y1: "))
Y2 = int(input("ingrese el valor de la coordenada Y2: "))
if X1 > X2 and Y1 > Y2 :
    D = ((X1-X2)+(Y1-Y2))**0.5
if X1 > X2 and Y2 > Y1 :
    D = ((X1-X2)+(Y2-Y1))**0.5
if X2 > X1 and Y1 > Y2 :
    D = ((X2-X1)+(Y1-Y2))**0.5
if X2 > X1 and Y2 > Y1 :
    D = ((X2-X1)+(Y2-Y1))**0.5
print("La distancia entre las 2 coordenadas son ", D)
  