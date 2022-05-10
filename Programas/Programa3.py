#Hacer un programa que procese un total de 100 personas y establecer cuantas son mujeres mayores de edad y cuantos hombres menores de edad. Deberá sacar el hombre y la mujer con menor edad, el hombre y la mujer con mayor edad, promedio de edades de las mujeres y promedio de edades de los hombres.

from random import randint
#def run():
genero=[]
edad=[]
listadoM=[]
listadoH=[]
menores=[]
mayores=[]
aux=[]
for u in range (0,100):
    genero=randint(0,1)
    if (genero==0): listadoM.append(genero)
    else: listadoH.append(genero)
    edad=randint(0,100)
    if (edad<18): menores.append(edad)
    else: mayores.append(edad)
    diccionario={
        'genero': [genero],
        'edad':[edad]
        }
    print(diccionario)
    #print(genero[0])
"""
print(diccionario)
if (genero==0) and (edad<18):
    aux.append(diccionario)
print(len(aux))
"""
   
for x in diccionario:
    if (genero==0) and (edad>=18):
        print(f'El número de mujeres mayores de edad es: {x}')

#print(len(genero))
#elif (genero==0) and (edad<18): MujMen(count):

print(listadoM)
print(f'En el listado hay: {len(listadoM)} mujeres')
print(listadoH)
print(f'En el listado hay: {len(listadoH)} hombres')
print(menores)
print((f'En el listado hay: {len(menores)} menores'))
print(mayores)
print(f'En el listado hay: {len(mayores)} mayores')



#if __name__ == '__main__':
    #run()

# si el valor de la primera clave es igual a 0 (mujeres) y el valor de la segunda clave es >=18: imprimir su longitud.
# si el valor de la primera clave es igual a 1 (hombres) y el valor de la segunda clave es <18: imprimir su longitud.
# encontrar el mín(genero==0)
# encontrar el mín(genero==1)
# encontrar el max(genero==0)
# encontrar el max(genero==1)
# segregar por sexos y buscar sumar todos los valores de las edades y dividirlo entre el total.

