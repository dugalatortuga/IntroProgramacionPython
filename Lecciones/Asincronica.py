import asyncio

async def saludo():
    print('Hola')
    await asyncio.sleep(4) #espera 4 segundos para ejecutar la siguiente linea.
    print('world')

asyncio.run(saludo())
print('Fin del programa')

asyncio.run(saludo())
print('Fin del programa')

# Utilizaremos estas funciones cuando necesitemos utilizar asincronías.

