# FACTORIAL RECURSIVO
"""
def Factorial(N):
    if N<=0:
        raise
        #pass
    if (N<=1):
        print('return 1')
        return 1 #caso base para evitar la recursividad infinita
    else:
        print('return {} Factorial({}-1)'.format(N,N))
        return N * Factorial(N-1)

n=input('Introduzca el número a factorizar: \n')
try:
    n=int(n)
    r=Factorial(n)
    print(f'El factorial de:', n, 'es', r)
except TypeError:
    print('Entre un número válido')
except ValueError:
    print('Numero no válido')
except:
    print('No se permiten valores menores que 0')
"""

#FIBONACCI RECURSIVO
"""
def Fibonacci(N):
    if (N==1):
        return 0
    elif(N==2):
        return 1
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)

n=input('Introduzca la posición de Fibonacci:\n')
try:
    n=int(n)
    serie_fibonacci=[]
    for i in range(1,n+1):
        r=Fibonacci(i)
        serie_fibonacci.append(r)
    print(f'El número es {r}')
    print('La serie es:',serie_fibonacci) #podríamos hacerlo desempaquetando mediante *serie_fibonacci, que indica que imprima la variable entera
    print('La serie es:',*serie_fibonacci)
except TypeError:
    print('Número no válido')
except:
    print('Falso')
"""

