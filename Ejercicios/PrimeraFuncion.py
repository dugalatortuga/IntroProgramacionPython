def saludar(nombre):
    #funcionalidad del tiempo
    print(f'Hola, {nombre}, buenos días!')

def sumar(a,b):
    return (a+b)

def addColores(colores,color):
    try:
        colores.append(color)
        return True
    except AttributeError:
        return False


saludar('Billy')
saludar('Amaia')
saludar('Antonio')
saludar('Bautista')

resultado= sumar(5,5) #=resultado=5+5
print(resultado)
print(sumar(5,5))
print(sumar(7,5))
print(sumar(9,5))
print(sumar(0,5))
print(sumar(4,4))

colores=[]
addColores(colores,'azul')
addColores(colores,'rojo')
addColores(colores,'verde')
addColores(colores,'negro')
addColores(colores,'púrpura')
addColores(colores,'Billy')
saludar(colores)

if (addColores('Billy','naranja')):#ahora mismo nos devuelve el False 'no insertado color' #se convierte en True si le pasamos una colección, no una lista, por ejemplo: if (addColores('colores','naranja')) equivalente a addColores..()==True
    print('Insertado color')
else:
    print('No insertado color')


ciudad='Nairobi'
