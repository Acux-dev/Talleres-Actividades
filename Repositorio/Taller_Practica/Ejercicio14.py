V = float(input("Ingrese el valor de la velocidad inicial, en metros por segundo: "))
A = float(input("Ingrese el valor de la aceleración inicial, en metros por segundo al cuadrado: "))
T = float(input("Ingrese el valor del tiempo que se le quiere revisar la velocidad, en segundos: "))
V0 = V + A*T
print("La velocidad actual que tiene el objeto despues de ", T, " segundos es ", V0, "metros por segundo")