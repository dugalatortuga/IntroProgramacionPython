#Operadores
a=10
b=20
if(a>b):
    print(f"el número mayor es {a}")
else:
    if (b>a):
        print(f"El número mayor es {b}")
    else:
        print("los dos números son iguales")

# elif implica un else if
# Python no tiene la estructura según caso

if(a>b):
    print(f"el número mayor es {a}")
elif (b>a):
    print(f"El número mayor es {b}")
else:
    print("los dos números son iguales")


#SENTENCIA DE REPETICIÓN FOR (bucle)
lenguajes=['python','c','c++','java']
for lenguaje in lenguajes:
    print(lenguaje)
for numero in range(3):
    print(numero)

#argumentos de la función RANGE: inicio, final y paso.
