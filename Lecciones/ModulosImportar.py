def saludar(nombre):
    print(f'Hola, {nombre}')
saludar('Olga')

#Cuando tengamos definida esta función, podremos llamarla desde otro programa.
import FuncionSaludar (#tras el import tenemos que poner el nombre del archivo al que llamemos)FuncionSaludar.saludar('Olga')

#Otra forma de importar, pero módulos específicos.
from FuncionSaludar import saludar
saludar('Olga')