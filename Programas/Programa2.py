#Hacer un programa que procese las edades de 100 personas. Deberá decir cuantas tienen más de (≥18) y cuál es la persona con menor edad y cuál es la persona con mayor edad. También deberá mostrar el porcentaje de edades de las 100 personas.

from random import randint

edadeshasta18=[]
edadesdesde18=[]

for i in range(0,100):
    personas=randint(0,100)
    if (personas<18): edadeshasta18.append(personas)
    else: edadesdesde18.append(personas)
    # personas = [randint(0,100) for i in range(0,100)]

"""
clasificacion_edades={edad:0 for edad in personas}
for n in (edadeshasta18 + edadesdesde18):
    clasificacion_edades[n]+=1
print(clasificacion_edades)
"""

"""
print(edadeshasta18) # CheckPoint
print(edadesdesde18) # CheckPoint
"""
total = (edadesdesde18 + edadeshasta18)
#print(total.sort())
#print(total)
print(f'Hay {total.count(38)} personas con 38 años, siendo el {total.count(38)/len(total)*100} %')

print(f'La edad media de la muestra es: {sum(total) / len(total)} años')
print(f'Los menores de edad son el {len(edadeshasta18)} %')
print(f'Los mayores de edad son el {len(edadesdesde18)} %')
print(f'La mayor edad de la muestra es: {max(edadesdesde18)} años')
print(f'La menor edad de la muestra es: {min(edadeshasta18)} años')

#print(f'Hay un {len(listadoM)} % de mujeres en la muestra')