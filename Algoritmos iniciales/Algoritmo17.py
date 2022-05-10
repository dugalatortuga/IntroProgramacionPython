#Algoritmo17: volumen y área de un cilindro.
from cmath import pi
#import math
radio=input("Inserte el radio del círculo.")
altura=input("Inserte la altura del cilindro.")
if (radio.isdigit) and altura.isdigit():
    radio=int(radio)
    altura=int(altura)
    area=2*pi*radio*altura
    volumen=pi*radio*radio*altura
    #print(f"El área son {area} cm cuadrados")
    print("El área del cilindro es: {n:1.2f}".format(n=area))
    print("El volumen del cilindro es: {n:1.2f}".format(n=volumen))
else:
    print("Introduce un número válido.")