# Ingresar dos números y devuelva el resultado de la suma entre ambos.
Num1=input("Inserte el primer número: ")
Num2=input("Inserte el segundo número: ")
if(Num1.isdigit and Num2.isdigit):
    #Num1=int(Num1)
    #Num2=int(Num2)
    #Rta=Num1+Num2
    print(f"El resultado es: {int(Num1)+int(Num2)}")
else:
    print("Los valores introducidos no son números válidos)")