# CONTROL DE EXCEPCIONES
# try se usa donde quiero controlar una excepción o un error en el tiempo de ejecución.

numero1=100
numero2=0
try:
    print(numero1/numero2)
except ZeroDivisionError:
    print("Error al dividir por cero.")
except:
    print("Error.")
else:
    print("La división se calculó correctamente.")
finally:
    print("Fin del programa.")
    # Finally se ejecuta siempre, haya errores o no los haya.
