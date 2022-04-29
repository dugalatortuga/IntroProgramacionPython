# Escribir tres números
#print("Ingrese el primer número")
num1=input("Ingrese el primer número: "+"\n")
#print("Ingrese el segundo número")
num2=input("Ingrese el segundo número: "+"\n")
#print("Ingrese el tercer número")
num3=input("Ingrese el tercer número: "+"\n")
try:
    num1=float(num1)
    num2=float(num2)
    num3=float(num3)
    if(num1<0):
        resul=num1*num2*num3
    else:
        resul=num1+num2+num3
    print(resul)
except ValueError:
    print("Los datos deben ser numéricos.")
except:
    print("Error")