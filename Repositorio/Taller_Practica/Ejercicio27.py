listanotas=[]
i=1
Cantidad=5
while Cantidad>0:
    Num=(float(input('Digite su nota '+str(i)+(': '))))
    if Num>=5.1:
        print('no se admiten valores mayores a 5')
        break   
    i+=1
    listanotas.append(Num)
    Cantidad-=1
Total=(listanotas[0]*0.15)+(listanotas[1]*0.2)+(listanotas[2]*0.15)+(listanotas[3]*0.3)+(listanotas[4]*0.2)
print('Su definitiva es:',Total)
if Total<2:
    print('No puede habilitar')
elif Total<3:
    print('Reprobo')
elif Total>=3 and Total<=4.5:
    print("aprobo")
elif Total>4.5:
    print("felicitaciones!!!")