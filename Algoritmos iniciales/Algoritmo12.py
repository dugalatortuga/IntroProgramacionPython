# Algoritmo 12:Sumar los dígitos de un número ingresado. Ejemplo: Si se ingresa 123, debería devolver 6.
num = input("Ingrese un número: ")
resul=0
if (num.isdigit()):
    num=int(num)
    while num != 0:
        resul += num % 10
        num = num//10
    #FinMientras
    print("El resultado es: ",resul)
else:
    print("Ingrese un número válido.")
#FinAlgoritmo