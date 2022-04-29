#Algoritmo 5: Suma de números pares entre 2 y 100
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
        