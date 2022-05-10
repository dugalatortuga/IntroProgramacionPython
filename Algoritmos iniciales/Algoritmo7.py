# Algoritmo 7. Aprobado o suspenso.

#print("Ingrese calificación 1")
#cal1=input()
cal1=input("Inserte la primera calificación: ")
cal2=input("Inserte la primera calificación: ")
cal3=input("Inserte la primera calificación: ")
if (cal1.isdigit() and cal2.isdigit() and cal3.isdigit()):
    #validación de calificaciones
    cal1=int(cal1)
    cal2=int(cal2)
    cal3=int(cal3)

    # if((cal1>=0 and cal1<=10) and (cal2>=0 and cal2<=10) and (cal3>=0 and cal3<=10))
    if((cal1 in range(0,11)) and (cal2 in range (0,11)) and (cal3 in range (0,11))):
        prom=((int(cal1)+int(cal2)+int(cal3))/3)
        #prom=((int(cal1)+int(cal2)+int(cal3))//3)
        if (prom>=5):
            print("Aprueba con un ")
        else:
            print("Suspende con un ")
        print(prom)
    else:
        print("El rango de las calificaciones debe estar entre 0 y 10")
else:
    print("Por favor, introduzca números enteros.")