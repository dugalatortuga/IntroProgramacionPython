
#EJERCICIO 1 #Imprimir "Hola, mundo!"

print("Hola, mundo!")


#EJERCICIO 2 #A partir de un número ingresado diga si es mayor, menor o igual a 9.
N=0
print("Escriba un número:")
if(N.isdigit()):
    N=int(input())
    if(N==9):
        print("El número es igual a 9")
    else:
        if (int(N>9)):
            print("Su número es mayor que 9")
        else:
            print("El número es menor que 9")
else:
    print("Por favor, inserte un valor numérico.")

#input: entrada