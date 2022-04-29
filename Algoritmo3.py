#Algoritmo 3
#print("Ingrese un número")
nro=input("Ingrese un número:")
if(nro.isdigit()):
    nro=int(nro)
    if(nro%2==0):
        print("El número es par")
    else:
        print("El número es impar")
else:
    print("Por favor, ingrese un número válido")