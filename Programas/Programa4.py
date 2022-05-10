#Hacer un programa que procese las temperaturas mensuales de 20 ciudades. Deberá sacar cuál de las ciudades tiene en promedio anual la temperatura más alta y cual la más baja. También deberá sacar la lista de las 20 ciudades con el promedio de temperaturas anuales desde la más alta hasta la más baja.


def run():
    historico = {
        'ciudad' : ('Sevilla', 'Cordoba' ,'Cadiz','Huelva','Granada','Jaen','Almeria','Malaga','Toledo','Ciudad Real','Cuenca','Guadalajara','Albacete','Madrid','Barcelona','Tarragona','Gerona','Lleida','Murcia','Talavera de la Reina')
        #'mes' : ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
        'temperatura' : [32,32,28,27,31,30,28,25,16,26,19,15,30,15,16,20,20,16,12,13]
    }

if __name__ == '__main__':
    run()


#calcular las temperaturas promedio de las ciudades.
#calcular el máximo anual de cada ciudad.
