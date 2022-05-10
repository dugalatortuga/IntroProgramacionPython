# Algoritmo 11: Si un número ingresado es primo o no. (Un número es primo si es divisible únicamente por 1 y por sí mismo).
# Además vamos a sacar los 10 primeros números primos.

num=input("Ingrese un número \n")
if(num.isdigit()):
    num=int(num) #convertimos la entrada tipo texto "valor" a número.
    div=2
    band=True

    if num==1:
        print("Es primo")
    else:
        while band and (num>div): #band es una variable booleana (True o False) #while band==True
            if (num % div)==0:
                band==False
                break
            #FinSi
            div+=1 #div=div+1
        #FinMientras
        if band: #es lo mismo que if band==True
            print("Es primo")
        else:
            print("No es primo")
        #FinSi
    #FinSi
else:
    print("Por favor, introduzca un número válido")