#argumentos de la función RANGE: inicio, final y paso.

contadordenumerosenlaserie=0
for numero in range(1,21,2):
    contadordenumerosenlaserie+=1
    if(contadordenumerosenlaserie>5):
        break #salte a la linea del for
    print(numero)
print("Numeros de la serie",contadordenumerosenlaserie)
