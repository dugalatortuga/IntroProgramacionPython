def ProcesoInicial():
    print('Paso 1: buscar una hoja de papel') #esta función no tiene argumentos,a sí que el valor asignado no depende del parámetro.
def ProcesoDos():
    print('Paso 1: doblar la hoja')

def SaludarATodos(*nombres): #con el asterisco indicamos que no sabemos cuántos parámetros vamos a meter.
    for i in nombres:
        print(f'Hola, {i}')

def SaludarATodosDicc(**nombres):
    for i in nombres:
        print(f'Hola: {i}{nombres[i]}')

def Ciudades(Pais,ciudad='Oslo'):
    print(Pais,'',ciudad)

ProcesoInicial()
ProcesoDos()
colores=['azul','rojo','amarillo']
SaludarATodos('Olga')
SaludarATodos('Rafaela','Carla','Pedro')
SaludarATodos('Diego','Cynthia','Álvaro','Emiliano')
SaludarATodos(345,'Miryam',True)
SaludarATodos()
SaludarATodos(colores) #también saluda a los colores

SaludarATodosDicc(nombre='Billy',apellidos='Vanegas')

Ciudades('Colombia','Bogotá')
Ciudades() # al dejarlo vacío nos da un error porque no le hemos dado argumento
Ciudades('México','México DF',)
Ciudades('Noruega','Oslo',)


# Las funciones se definen con del al principio del programa.
# Tienen un nombre y argumentos.
# Pueden devolvernos un valor también con return.
# Argumento es el valor enviado a la función.
# Parámetro es el valor entre paréntesis de la función.