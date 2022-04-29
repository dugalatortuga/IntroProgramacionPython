#Algoritmo 8: Repetir Nombre N veces
nombre=input("Ingresar nombre: ")
num=input("Ingresar cantidad de repeticiones: ")
if(num.isdigit()):
    num=int(num)
    print((f"{nombre}\n")*int(num))
    #while(num>0):
        #print(nombre)
        #num-=1
else:
    print("Por favor, introduzca la cantidad numérica.")

#print((nombre+"\n")*int(num))