import json
# cuando importamos Json haríamos jsonventas = json.loads("ORIGIN DE LOS DATOS DEL JSON")
Jsonventas= '{"departamento":8,"nombredpto":"ventas","director":"juan rodriguez"}'
#segundojson= "{'departamento':8,'nombredpto':'ventas','director':'juan rodriguez'}"
#tercerJson="{\"departamento\":8,\"nombredpto\":\"ventas\",\"director\":\"juan rodriguez\"}"

print(Jsonventas)
datosdepartamento=json.dumps(Jsonventas)
#datossegundodpto=json.dumps(segundojson)
#datostercerdpto=json.dumps(tercerJson)

print("Json 1: ",Jsonventas)
#print("Json 2: ",datossegundodpto)
#print("Json 3: ",datostercerdpto)

print(type(datosdepartamento)) #para que nos muestre el tipo de variable: str (string)

#Conclusión:
# la variable que debo utilizar para procesar el JSON  como una colección compleja/compuesta es el desrealizado (loads) porque es el contenedor de los elementos.
for val in Jsonventas:
    print(val,Jsonventas[val])

for val in datosdepartamento:
    print(val)

