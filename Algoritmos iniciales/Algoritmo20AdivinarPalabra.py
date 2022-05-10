palabra1 = "suerte"
print("Adivine la palabra (N para salir): ")
while True:
    palabra2 = input().lower() # Ahorrando asignar palabra2 = palabra2.lower()
    if palabra2 == palabra1:
        break # Ahorrando tener una variable boolean comprobando el estado
    elif palabra2== "N":
        break
    print("Vuelve a intentarlo (N para salir): ")
print("Felicidades, has adivinado la palabra")




palabra = "Pirata".lower()
countE = 1
count = 0
intento = input("Intenta adivinar palabra: ").lower()
pistas = ["Les Gusta el Oro", "Les Gusta el Mar", "Usan Parches", "Tienen pata de palo"]
while(palabra != intento):
    if(count == len(pistas)):
        count = 0
        print(pistas[count])
    else:
        print(pistas[count])
    intento = input(f"Intenta adivinar palabra llevas {countE} fallos: ").lower()
    countE += 1
    count += 1