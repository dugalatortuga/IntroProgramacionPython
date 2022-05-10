print("Instruccioón antes del while")
valor=0
while(valor<5): #nuestros valores irán desde 0 hasta 5
    valor +=1
    if(valor ==3):
        continue
    print(f"Valor actual: {valor}") #si este print hubiese estado antes de la línea 5, también nos imprimiría el 3.
print("Instrucción después del while")


print("Ahora hacemos BREAK")

print("Instruccioón antes del while")
valor=0
while(valor<5): #nuestros valores irán desde 0 hasta 5
    valor +=1
    if(valor >3):
        break
    print(f"Valor actual: {valor}") #si este print hubiese estado antes de la línea 5, también nos imprimiría el 3.
print("Instrucción después del while")

# CONTINUE y BREAK son funciones que auxiliares de FOR y WHILE

# En Python solo tenemos dos tipos de bucles: FOR y WHILE, no disponemos de Repetir Hasta.
