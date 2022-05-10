import json

citricos=['limon','naranja','pomelo','lima']

citricosJSON=json.dumps(citricos)
print(type(citricosJSON)) #para que nos muestre el tipo de variable: str (string)
print('Json de cítricos: ',citricosJSON)
    #respuesta: Json de cítricos:  ["limon", "naranja", "pomelo", "lima"]

#Hasta ahora hemos serializado nuestros objetos a un Json. (hidratar)
#A continuación vamos a deserializar. (deshidratar)

listacitricos=json.loads(citricosJSON)

print(listacitricos)
    #respuesta: ['limon', 'naranja', 'pomelo', 'lima']
#Es importante que las comillas de fuera y las de dentro sean distintas para que el programa las pueda diferenciar.
