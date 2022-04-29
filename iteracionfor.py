#SENTENCIA DE REPETICIÓN FOR (bucle)
#for numero in range(1,11,3):
    #print(numero)

#argumentos de la función RANGE: inicio, final y paso.

contadordenumerosenlaserie=0
for numero in range(1,21,2):
    contadordenumerosenlaserie+=1
    if(contadordenumerosenlaserie<=5):
        continue #salte a la linea del for
    print(numero)
