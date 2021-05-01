A = int(input("Ingrese el coeficiente de la variable cuadrática(A): "))
B = int(input("Ingrese el coeficiente de la variable lineal(B): "))
C = int(input("Ingrese el término independiente(C): "))
if ((B**2)-4*A*C) < 0:
      print("La solución de la ecuación es con numeros complejos: ")
else:
  X1 = ((-B+((B**2-(4*A*C))**0.5))/(2*A))
  X2 = ((-B-((B**2-(4*A*C))**0.5))/(2*A))
  print("Las soluciones de la ecuación son: ")
  print(X1)
  print(X2)