Indicado = int(input("Escriba la candidad de segundos a indicar: "))
S = Indicado
M = Indicado
H = Indicado
while S >= 60:
    S = S-60
    if S < 60:
      break
M = int(M/60)
while M >= 60:
    M = M-60
    if M < 60:
      break
H = int(H/3600)
while H >= 60:
    H = H-60
    if H < 60:
      break
print(H, ":", M, ":", S)