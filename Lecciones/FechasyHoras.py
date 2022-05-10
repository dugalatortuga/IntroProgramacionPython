from datetime import datetime
    #con este comando importamos datetime. lo hacemos cada vez que iniciemos Py.

datenow1 = datetime.now().date()
print("Fecha: ",datenow1)
    #devuelve fecha completa
datenow2 = datetime.now()
    #devuelve fecha y hora completa
print("Fecha: ", datenow2)
print("Año: ",datenow2.year)
print("Mes: ",datenow2.month)
print("Día: ",datenow2.day)
print("año Fecha2: ",datenow2.year)
print("mes Fecha2: ",datenow2.month)
print("hora Fecha2: ",datenow2.hour)
print("minutos Fecha2: ",datenow2.minute)
print("segundos Fecha2: ",datenow2.second)
print("microsegundo Fecha2: ",datenow2.microsecond)
datenow3= datetime.now()
print("microsegundos Fecha3: ",datenow3.microsecond)


# SINTAXIS Y ESTRUCTURAS DE CONTROL:

from datetime import datetime
    #con este comando importamos datetime. lo hacemos cada vez que iniciemos Py.

fecha ="10-11-2022"
obj=datetime.strptime(fecha,'%m-%d-%Y').date
print(obj)


