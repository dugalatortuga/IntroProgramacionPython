#Factorial de un número
n=input("ingrese un número")
f=1
if (n.isdigit()):
    n=int(n)
    while n>1:
        f=f*n
        # print(f"{n} {f}") con esta linea veríamos en un paso intermedio el avance del algoritmo en las multiplicaciones. NO es necesario.
        n=n-1
    print("el factorial es: ",f)
else:
    print("ingrese numero valido")

#RESPUESTA
#ingrese un número5
# 5 5
# 4 20
# 3 60
# 2 120
# el factorial es:  120