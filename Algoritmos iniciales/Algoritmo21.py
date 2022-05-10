#Encontrar si un número es mayor o menor a un número dado.
x=int(6)

print("Introducir un número")
y=int(input())
if(y.isdigit()):
    if(x>=y):
        print(f"{x} es mayor ")
    else:
        print(f"{y} es mayor ")
else:
    print("Entre un número válido")