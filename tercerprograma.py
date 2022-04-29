ciudad="madrid"
print(ciudad)

minombre="Diego"
print(len(minombre))

# la función len nos devuelve el número de caracteres de la variable: 5

print(minombre[0])
print(minombre[1])
print(minombre[2])
print(minombre[3])
print(minombre[4])
print(minombre[2])
#muestra las posiciones que le indiquemos de nuestro nombre.

print(minombre[2:])
#muestra a partir de la segunda posición.
print(minombre[:4])
#muestra hasta la cuarta posición.
print(minombre[2:4])
#muestra las posiciones entre la 2 y la 4

print(len(minombre))

print(minombre[-2])
#nos muestra el caracter 2 empezando por el final.

mensaje="dd"
print("hola {}".format(mensaje))
#poniendo las llaves en la concatenación es mucho más eficiente para el compilador. Es más rápido que hacer una concatenación solo con +. Con los corchetes ayudamos a la función implícita .format a que encuentre la información que queremos.

mensaje="dd"
ciudad="Albacete"
print("hola {m} de {c}".format(m=mensaje,c=ciudad))
#print("hola "+mensaje) no es una forma eficiente de concatenar cadenas de caracteres

numero=10/3
print("El número sin formato es: {}".format(numero))
print("El número con formato es: {n:1.2f}".format(n=numero))
#le estamos diciendo que queremos que nos devuelva el número entero y dos decimales: (n:1.2f)

print(f"Hola {mensaje} de {ciudad}")

