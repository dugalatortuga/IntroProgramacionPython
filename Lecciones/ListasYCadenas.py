#C:\Users\Diego\00-EOI\IntroProgramacionPython>py
#Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> colores=["red","yellow","green"]
#>>> print(colores)
#['red', 'yellow', 'green']
#>>> colores.insert(2,"orange")
#>>> print(colores)
#['red', 'yellow', 'orange', 'green']
#>>> colores.append("black")
#>>> print(colores)
#['red', 'yellow', 'orange', 'green', 'black']
#>>> print("La posición del color yellow es: ",colores.index("yellow"))
#La posición del color yellow es:  1
#>>> colores.remove("yellow")
#>>> print(colores)
#['red', 'orange', 'green', 'black']
#>>> print(colores[3])
#black
#>>>

---
colores=["red","yellow","green"]
print(colores[1])
colores.append("black")
colores.insert(2,"orange")
print("lista de colores: ",colores)
try:
    color=input("Inserte el color para saber su posición")
    print("La posición del color en la lista es: ",colores,index(color))
except ValueError:
    print("el color no está en la lista")
colores.remove("yellow") #ValueError si el elemento no está en la lista.
print("color en la posición 2:",colores[2])
print("lista de colores actualizada: ",colores)

colores_alternativos=["magenta","blue","pink"]
colores.extend(colores_alternativos)
print("Lista de colores actualizada después del extend: ",colores)

colores.pop(2) #borrará green
print("Lista de colores actualizada después del pop: ",colores)

colores.sort() #ordena alfabéticamente de forma ascendente
print("Lista de colores actualizada después del sort: ",colores)

colores.sort(reverse=True) #ordena alfabéticamente de forma descendente
print("Lista de colores actualizada después del inverso de sort: ",colores)

print(colores*2) #duplicará la lista

----
#Tuplas:
numeros=(17,89,21,988,42,328,657)
print(numeros)
print(numeros[0])
print(max(numeros))
print(min(numeros))
print(sum(numeros))
print(numeros*3) #se triplicará la tupla
print(list(enumerate(numeros))) #nos indicará la posición de cada elemento seguido del propio elemento.

dias=("lunes",'martes','miercoles','jueves','viernes','sabado','domingo')
for dia in dias:
    print(dia)

for dia_numero in enumerate (dias, 1):
    print(dia_numero)


#letras=('a','b','c','d','e','f','g','h
letras=('abcdefghijklmnñopqrstuvwxyz')

letrasalfabeto=tuple(x for x in letras)
for letra in letrasalfabeto:
    print('letra:',letra)

letrasalfabeto=tuple(x for x in letras)
for letra in enumerate(letrasalfabeto,40):
    print('letra',letra)


#También podemos desempaquetar los valores de la tupla:
postres='tiramisu','flan casero','pudin')
#unpacking: asignamos una variable a cada elemento de la tupla. Hay que asignar el mismo numero de variables que de elementos de la tupla.
postrea,postreb,postrec=postres

print('Postres en la tupla:',postres)
print('Valores Unpacking: ',postrea,postreb,postrec)



#qué hacemos si necesitamos añadir un elemento, borrarlo o modificarlo? Habría que crear la tupla de nuevo.

#cómo se ordenan las listas en orden descendente?

#utilizamos tuplas cuando sabemos que no queremos cambiar el contenido, y listas si lo queremos cambiar.
-----------------
#Podemos convertir una lista a tupla o a coleeción y viceversa
ciudades={'madrid','albacete','vigo','palencia','Sevilla','sevilla','vigo'}
print(ciudades) #nos elimina los duplicados. No diferencia entre mayúsculas y minúsculas.
ciudades.add('valencia')
ciudades.add('Gijón')
for ciudad in ciudades:
    print(ciudad)

ciudades.discard('palencia')
print(ciudades)

-----------------
dicColores={'red':'rojo','blue':'azul','green':'verde'}
print('Diccionario inicial',dicColores)
dicColores['black']='negro' #añadimos una entrada del diccionario dando su clave.
print('Diccionario tras añadir el color negro:',dicColores)
dicColores.pop('green')     #quitar un elemento del diccionario dando su clave.
print('Diccionario después de quitar el color verde',dicColores)

print("Red en castellano: ",dicColores['red'])
print("Blue en castellano: ",dicColores['blue'])

for key in dicColores:
    print(key,'->',dicColores[key])
-----------------

fruits = ['apple','banana','cherry','kiwi','mango']
newlist = []
for x in fruits:
    if 'a' in x:
        newlist.append(x)
print('Nueva lista a partir de recorrer la primera:',newlist)

newlist = [x for x in fruits if 'a' in x]
print('Nueva lista con LC',newlist)

