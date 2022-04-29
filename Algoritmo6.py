#Algoritmo 6 Divisores de un número
nro=input("Ingrese un número:")
if(nro.isdigit()):
    nro=int(nro)
    div=1
    while(div<=nro):
        if(nro%div==0):
            print(div)
        div+=1 #div=div+1
else:
    print("Por favor, inserte un número válido")