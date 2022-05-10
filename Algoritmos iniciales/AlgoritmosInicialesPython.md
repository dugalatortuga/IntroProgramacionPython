**EJERCICIO 1:** ***Mostrar Hola, mundo!***
```
print("Hola, mundo!")
```
**EJERCICIO 2:** ***A partir de un número ingresado diga si es mayor, menor o igual a 9.***
```
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
```
**EJERCICIO 3:** ***Ingresar un número y determinar si es par o impar.***
```
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
```
**EJERCICIO 4:** ***Ingresar dos números y devuelva el resultado de la suma entre ambos.***
```
um1=input("Inserte el primer número: ")
Num2=input("Inserte el segundo número: ")
if(Num1.isdigit and Num2.isdigit):
    #Num1=int(Num1)
    #Num2=int(Num2)
    #Rta=Num1+Num2
    print(f"El resultado es: {int(Num1)+int(Num2)}")
else:
    print("Los valores introducidos no son números válidos)")
```
**EJERCICIO 5:** ***Sumar todos los números pares entre 2 y 100***
```
suma=0
nro=2
while (nro<=100):
    if(nro%2==0):
        suma+=nro #suma=suma+nro
    #FinSi    
    nro=nro+1
#FinWhile
print(f"La suma de los pares entre 2 y 100 es {suma}")

#Otra forma de conseguir el mismo resultado
suma=0
nro=2
while (nro<=100):
    #if(nro%2==0):
     suma+=nro
    #FinSi    
    nro=nro+2
#FinWhile
print(f"La suma de los pares entre 2 y 100 es {suma}")

#Otra forma de conseguir el mismo resultado
suma = 0
    for i in range(2, 102, 2):
        suma += i
        print(f"La suma de todos los pares entre 2 y 100 es {suma}")
```
**EJERCICIO 6:** ***Mostrar los divisores de un número.***
```
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
```
**EJERCICIO 7:** ***Determinar si un alumno aprueba o suspende.***
```
#print("Ingrese calificación 1")
##cal1=input()
cal1=input("Inserte la primera calificación: ")
cal2=input("Inserte la primera calificación: ")
cal3=input("Inserte la primera calificación: ")
if (cal1.isdigit() and cal2.isdigit() and cal3.isdigit()):
    #validación de calificaciones
    cal1=int(cal1)
    cal2=int(cal2)
    cal3=int(cal3)

    # if((cal1>=0 and cal1<=10) and (cal2>=0 and cal2<=10) and (cal3>=0 and cal3<=10))
    if((cal1 in range(0,11)) and (cal2 in range (0,11)) and (cal3 in range (0,11))):
        prom=((int(cal1)+int(cal2)+int(cal3))/3)
        #prom=((int(cal1)+int(cal2)+int(cal3))//3)
        if (prom>=5):
            print("Aprueba con un ")
        else:
            print("Suspende con un ")
        print(prom)
    else:
        print("El rango de las calificaciones debe estar entre 0 y 10")
else:
    print("Por favor, introduzca números enteros.")
```
**EJERCICIO 8:** ***Repetir un nombre N veces.***
```
nombre=input("Ingresar nombre: ")
num=input("Ingresar cantidad de repeticiones: ")
if(num.isdigit()):
    num=int(num)
    print((f"{nombre}\n")*int(num))
    #while(num>0):
        #print(nombre)
        #num-=1
else:
    print("Por favor, introduzca la cantidad numérica.")

#print((nombre+"\n")*int(num))
```
**EJERCICIO 9:** ***Sumar todos los números naturales entre 1 y 50.***
```
num=1
resul=0
for num in range(1,51):
    resul=resul+num
print(resul)
```
**EJERCICIO 10:** ***Sumar o multiplicar números.***
```
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
```
**EJERCICIO 11:** ***Mostrar Hola, mundo!***
```
```
**EJERCICIO 12:** ***Mostrar Hola, mundo!***
```
num=input("Ingrese un número: "
resul=0
while(num!=0):
    resul+=(num%10)
    num=num//10
print("El resultado es: ",resul)
```