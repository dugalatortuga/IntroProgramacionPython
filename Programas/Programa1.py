from random import randint

listadoH=[]
listadoM=[]
for i in range (0,100):
    genero=randint(0,1)
    if (genero==0): listadoM.append(genero) #listadoM.append('M')
    else: listadoH.append(genero) #listadoH.append('H')

print(f'Hay un {len(listadoH)} % de hombres en la muestra') #print(f'El número de chicos es: {listadoH.count('H')}')
print(f'Hay un {len(listadoM)} % de mujeres en la muestra')

if len(listadoH)>50:
    print('Los hombres son mayoría')
elif len(listadoM)>50:
    print('Las mujeres son mayoría')
else:
    print('Estamos ante una muestra equilibrada')



#AlgoritmoEstadística
#Hacer un programa que procese 100 mujeres y hombres (M/H). Mostrar el porcentaje de hombres y mujeres y si hay más mujeres que hombres, si hay igualdad o si hay más hombres que mujeres.
#Entrada
        #Leemos los datos de cada persona uno a uno o si generamos los datos a partir de listas. Si los generamos estaría bien que los datos fuesen aleatorios.
            #0=mujeres
            #1=hombres
        #asignar esa generación a una colección.
        #preguntar cuántas chicas y chicos hay.


#Salida
    #Escribir el resultado de las chicas y de los chicos.
    #Mostrar de qué tipo hay más registros.



#FinAlgoritmo