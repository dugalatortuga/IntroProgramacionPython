
# SINTAXIS Y ESTRUCTURAS DE CONTROL:

from datetime import datetime
#con este comando importamos datetime. lo hacemos cada vez que iniciemos Py.

fecha ="10-11-2022"
fecha1=datetime.strptime(fecha,'%m-%d-%Y').date()
print(fecha1)
#hemos indicado el formato de fecha que queremos que nos muestre.
fecha2=datetime.strptime(fecha,'%m-%d-%Y')
print(fecha2)

print(f"FEcha1 {fecha1.day}/{fecha1.month}/{fecha1.year}")


#FORMATOS DE FECHAS en diferentes culturas y países
print("FORMATO DE FECHA")
fecha3=datetime.now()
print(fecha3)
print(fecha3.strftime("%A %d %b %Y"))
#nuestro programa ha cogido la fecha actual y la ha formateado al formato indicado.


