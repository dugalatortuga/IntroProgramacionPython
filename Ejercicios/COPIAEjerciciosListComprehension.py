# EJERCICIO 1: Cree una lista idéntica a partir de la primera lista utilizando la comprensión de listas.

lst1=[1,2,3,4,5]
lst2=[n for n in list1]
print(lst2)

lst1=[1,2,3,4,5]
lst2=[]
for n in lst1:
    lst2.append(n)
print(lst2)

# EJERCICIO 2: Crear una lista a partir de los elementos de un rango de 1200 a 2000 con pasos de 130, utilizando la comprensión de listas.

list1=range(1200,2001,130)
list2=[n for n in list1]
print(list2)


list1=range(1200,2001,130)
list2=[]
for n in list1:
    list2.append(n)
print(list2)


rng=[]
for n in range (1200,2001,130):
    rng.append(n)
print(rng)

# EJERCICIO 3: Use la comprensión de listas para construir una nueva lista, pero agregue 6 a cada elemento.

list1=[44,54,64,74,104]
list2=[]
for n in list1:
    list2.append(n+6)
print(list2)

list2=[n+6 for n in list1]
print(list2)

# EJERCICIO 4: Utilizando la comprensión de listas, construya una lista a partir de los cuadrados de cada elemento de la lista.

list1=[2,4,6,8,10,12,14]
list2=[n**2 for n in list1]
print(list2)


list1=[2,4,6,8,10,12,14]
list2=[]
for n in list1:
    list2.append(n**2)
print(list2)

# EJERCICIO 5: Utilizando la comprensión de listas, construya una lista a partir de los cuadrados de cada elemento de la lista, si el cuadrado es mayor que 50.

list1=[2,4,6,8,10,12,14]
list2=[(n**2) for n in list1 if (n**2>50)]
print(list2)


list1=[2,4,6,8,10,12,14]
list2=[]
for n in list1:
    if n**2>50:
        list2.append(n**2)
print(list2)

# EJERCICIO 6: El diccionario dado consta de vehículos y sus pesos en kilogramos. Construya una lista de nombres de vehículos con peso inferior a 1300 kilogramos. En la misma lista de comprensión, haga que los nombres de las claves estén en mayúsculas.

dict={"Susuke Ignis": 985, "Chevrolet park Activ": 1100, "Volkswagen CrossUP": 1245, "Masda CX-3": 1254, "Susuki Vitara": 1245, "Nissan Kicks": 1310, "Mazda CX-5": 1672, "Ford Escape": 1625}
list=[]
for n in dict:
    if dict[n]<1300:
        list.append(n.upper())
print(list)

dict={"Susuke Ignis": 985, "Chevrolet park Activ": 1100, "Volkswagen CrossUP": 1245, "Masda CX-3": 1254, "Susuki Vitara": 1245, "Nissan Kicks": 1310, "Mazda CX-5": 1672, "Ford Escape": 1625}
list=[n.upper() for n in dict if dict[n]<1300]
print(list)

# EJERCICIO 7: Cree un diccionario de la lista con los mismos pares clave:valor, como: {"clave": "clave"}.

lst=["NY", "FL", "CA", "VT"]
dic={n:n for n in lst}
print(dic)

lst=["NY", "FL", "CA", "VT"]
dict={}
for n in lst:
    dict[n]=n
    dict.setdefault(n,n)

# EJERCICIO 8: Cree un rango de 100 a 160 con paso 10. Utilizando la comprensión de listas, cree un diccionario en el que cada número del rango sea la clave y cada elemento dividido por 100 sea el valor.

rng=range(100,160,10)
dict={}
for n in rng:
    dict[n]=(n/100)
print(dict)

rng=range(100,161,10)
dict={n:(n/100) for n in rng}
print(dict)

# EJERCICIO 9: Usando la comprensión de listas y un argumento condicional, cree un diccionario a partir del diccionario actual donde solo los pares clave:valor con un valor superior a 2000 se toman en el nuevo diccionario.

dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={}
for n in dict1:
    if dict1[n]>2000:
        dict2[n]=dict1[n]
print(dict2)

dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={n:dict1[n] for n in dict1 if dict1[n]>2000}
print(dict2)