A = float(input("Ingrese el valor de la aceleracion, en metros por segundo al cuadrado: "))
V = float(input("Ingrese el valor de la velocidad inicial, en metros por segundo: "))
T = float(input("Ingrese el valor del tiempo, en segundos: "))
X = (V*T)+(1/2*A*(T**2))
print("La distancia recorrida es ", X, " metros")