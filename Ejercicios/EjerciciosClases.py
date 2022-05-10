# CLASES

class Persona:
    Nombres=''
    Apellidos=''

    def __init__(self,nombres,apellidos): #self nos hace referencia a ese mismo objeto. Sirve para que podamos hacer cosas cuando creamos ese objeto, que es cuando le asignamos valores o clases.
        self.Nombres = nombres
        self.Apellidos = apellidos

# setter: es el objeto a partir del que se dan valores. Con setter meto valores.
# getter: es el objeto a partir del que se obtienen valores. Con getter saco valores.

    def __str__(self):
        return '{} {}'.format(self.Nombres,self.Apellidos)

    def caminar(self):
        print('caminando')

profesor = Persona('Billy ','Vanegas') #las variab les Nombres y Apellidos de la 2 y 3 linea sobrarían porque en esta linea ya le estamos dando valores. Si no tengo una función constructor los valores tienen que estar en algún sitio, pero también puedo crear esos atributos con la func constructor con la función self.
#profesor.Nombres='Billy' #esto es un setter
#profesor.Apellidos='Vanegas' #esto es un setter

alumno= Persona('Diego ','Rodriguez')
#alumno.Nombres='Diego'
#alumno.Apellidos='Rodriguez'

administrativo=Persona('Oscar','León')
#administrativo.Nombres='Oscar'
#administrativo.Apellidos='León'

administrativo1=Persona('Juan','Ponce')
#administrativo1.Nombres='Juan'
#administrativo1.Apellidos='Ponce'

print('El profesor: {} {}'.format(profesor.Nombres,profesor.Apellidos)) #esto es un getter porque saco valores.
print('El alumno: {} {}'.format(alumno.Nombres,alumno.Apellidos))
print('El administrativo: {} {}'.format(administrativo.Nombres,administrativo.Apellidos))
print('El administrativo1: {} {}'.format(administrativo1.Nombres,administrativo1.Apellidos))

print('El alumno:,',alumno) #viene de la variable de la linea24 de alumno

profesor.caminar()

print('==========='*4)

# EJERCICIO 1

class Jets:
    def __init__(self, name, country):
        self.name = name
        self.origin = country
        
first_item = Jets("F16", "USA")

a=first_item.name
print(a)

# EJERCICIO 2

class Jets:
    model = None
    country = 0

    def __init__(self, name, country):
        self.name = name
        self.origin = country
        
first_item = Jets("F16", "USA")

b=first_item.origin
print(b)

# EJERCICIO 3

class Jets:
    model = None
    country = 0
    def __init__(self, name, country):
        self.name = name
        self.origin = country

    def __str__(self):
        return "{}->{}".format(self.name, self.origin)

   
first_item=Jets("F14","USA")
second_item=Jets("SU33","Russia")
third_item=Jets("AJS37","Sweden")
fourth_item=Jets("Mirage2000","France")
fifth_item=Jets("Mig29","USSR")
sixth_item=Jets("A10","USA")
first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
second_army=['avión:{}'.format(first_item),str(second_item),str(third_item),str(fourth_item),str(fifth_item),str(sixth_item)]
b=[str(first_item),str(second_item),str(third_item),str(fourth_item),str(fifth_item),str(sixth_item)]

print(first_army)
print(second_army)
print(b)
print('Avión: ',first_item)

# EJERCICIO 4

class Jets:
    model = None
    country = 0
    def __init__(self, name, country, cantidad):
        self.name = name
        self.origin = country
        self.cantidad = cantidad
        
first_item=Jets('F14','USA',87)
second_item=Jets('Mirage2000','France',35)

total=first_item.cantidad + second_item.cantidad
print('La cantidad total es',total)

# EJERCICIO 5

class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
nq2018 = Nobel('Chemistry',2018,'Frances H. Arnold')
print(nq2019.category, nq2019.year, nq2019.winner)

# EJERCICIO 6

class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

    def __str__(self):
        return '{} -> {} -> {}'.format(self.category, self.year, self.winner)
        
nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
nq2018 = Nobel('Chemistry',2018,'Frances H. Arnold')

print(str(nq2019.category), str(nq2019.year), str(nq2019.winner))
print(nq2019.category, nq2019.year, nq2019.winner) # obtenemos la misma salida que con la linea anterior.
print(nq2019)
print(nq2018)

# EJERCICIO 7
# Cree una clase llamada myfunc y
# dentro de ella coloque una función muy
# simple llamada "quinta" que toma x y devuelve
# la quinta potencia de x. No se necesitan init
# o atributos de clase.
# Finalmente llame a su función con el número 5
# y asígnela a la variable ans.

class myfunc:
    def quinta(n):
        n5 = (n**5)
        return n5
        
ans=myfunc.quinta(5)
print(ans)

# NO tener en cuenta el siguiente programa aunque funcione, solo es una prueba
class myfunc:
    def quinta(n):
        quinta = (n**5)
        return quinta
        
ans = myfunc.quinta(5)
print(ans)

# EJERCICIO 8
#Ahora hagamos algunos cambios en la clase que creamos
# en el ejercicio anterior de Python.
#Primero haga su función para que tome los
# parámetros: x e y. x será el número que se eleva,
# e será la potencia. ¡Entonces, los usuarios pueden elevar los números a cualquier potencia! También cambiemos el nombre de la función a "ElevarAlaPotencia".
#También agreguemos una representación de cadena rápidamente,
# de modo que cuando un usuario imprima la clase obtenga una
# descripción significativa.
#Puede ser algo como: Esta clase consistirá en operaciones
# matemáticas. Solo tenemos una función llamada
# ElevarAlaPotencia.

class myfunc:
    def ElevarAlaPotencia(x,y):
        elevar = (x**y)
        return elevar
            
    def __str__(self):
        return ('Esta clase consistirá en operaciones matemáticas. Solo tenemos una función llamada ElevarAlaPotencia.')
        
ans=myfunc.ElevarAlaPotencia(2,4)
print(ans)
texto=myfunc.__str__(0) # Obligatoriamente hay que indicarle una posición. Como esta función solo tiene un argumento, podemos darle cualquier valor (en este caso le damos 0).
print(texto)
