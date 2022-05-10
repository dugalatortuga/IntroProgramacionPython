#Algoritmo 16: Realizar las cuatro operaciones básicas (Suma, Resta, Multiplicación, División)
#    num1=input("Inserte un número.")
#    num2=input("Inserte otro número.")
#    if(num1.isdigit and num2.isdigit):
#        print(f"El resultado es: {int(num1)+int(num2)}")
#        print(f"El resultado es: {int(num1)-int(num2)}")
#        print(f"El resultado es: {int(num1)*int(num2)}")
#        print(f"El resultado es: {int(num1)/int(num2)}")

i=0     #flag o bandera en castellano
while (i==0):
    try:
        e=float(input("Qué operación realizo 0. Suma, 1. Resta, 2. Multiplicación o 3. División"))
        x=float(input("Qué valor asignamos a número1?"))
        y=float(input("Qué valor asignamos a número2?"))
        if x.replace(".","",1).isdigit() and y.replace(".","",1).isdigit():
            #x=float(x)
            #e=float(e)
            #y=float(y)
            if(e==0):
                z=x+y
                print(f"El resultado de sumar {str(x)} y {str(y)} es: {str(z)}")
            elif(e==1):
                z=x-y
                print(f"El resultado de restar {str(x)} y {str(y)} es: {str(z)}")
            elif(e==2):
                z=x*y
                print(f"El resultado de multiplicar {str(x)} y {str(y)} es: {str(z)}")
            elif(e==3):
                if(y==0):
                    print(f"El valor de num2 no puede ser {y}")
                else:
                    z=x/y
                    print(f"El resultado de dividir {str(x)} y {str(y)} es: {str(z)}")
    except ValueError:
        print("Por favor, escriba un valor numérico válido.")