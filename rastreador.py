import openrouteservice # Importa la libreria de OpenRouteService
import csv # Importa la libreria CSV

class Rastreador: # Crea la clase Rastreador

    def rastrearTienda(self): # Metodo que rastrea las tiendas
        encontrado = False # Asigna un False a la variable "encontrado" para que pueda servir como un determinante para el while
        while not encontrado: # Mientras "encontrado" tenga el valor de false va a seguir haciendo este bloque de codigo
            print("") # espacio de tolerancia
            id_tienda = input("Ingresa el ID de la tienda: ") # Input donde se ingresa el id de la tienda
            with open('tiendas.csv', newline='') as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file) # Crea un objeto para poder leer el archivo
                for row in reader: # Se encarga de buscar un ID en el CSV
                    if row['id_tienda'] == id_tienda: # Si el id de la tienda coincide con la variable dada anteriormente hacer lo siguiente
                        encontrado = True # darle el valor de True a "encontrado" para que pueda terminar el bucle y siga con el codigo
                        latitud_tienda = float(row['latitud']) # Extrae el dato de la latitud del csv y lo guarda en la variable
                        longitud_tienda = float(row['longitud']) # Extrae el dato de la longitud del csv y lo guarda en la variable
                        break # Rompe con el bucle
                if not encontrado: # En caso de que no coincida el id de la tienda con alguna de la base de datos hace lo siguiente
                    print("No se encontró una tienda con ese ID.") # Notifica al usuario que no existe la id

        with open('coordenadas.csv', newline='') as file: # Abre el archivo para poder leer filas de informacion
            reader = csv.reader(file) # Crea un objeto para poder leer el archivo
            # Obtiene las coordenadas del archivo y las guarda en dos variables
            for row in reader: # Se encarga de buscar las coordenadas del csv
                latitud_usuario = float(row[0]) # Extrae el dato de la latitud del csv y lo guarda en la variable
                longitud_usuario = float(row[1]) # Extrae el dato de la longitud del csv y lo guarda en la variable

        coords = ((latitud_usuario,longitud_usuario),(latitud_tienda,longitud_tienda)) # En el primer parentesis va las coordenadas de inicio y en el segundo van las coordenadas del final

        client = openrouteservice.Client(key='5b3ce3597851110001cf6248019ddc51fa504a2899b6cc783504c4c5') # Se especifica la clave personal dada por OpenRoute 

        verificador_de_input = False # Variable la cual nos va a ayudar a verificar si es que el input que se va a dar mas adelante es correcto 
        while not verificador_de_input: # Mientras "Verificador_de_input" tenga el valor de false va a seguir haciendo este bloque de codigo
            print("") # espacio de tolerancia
            print("Seleccione el medio de transporte que se quiera utilizar") # Nos notifica que tenemos que seleccionar algunas de las opciones siguientes
            print("0.- Automovil Convencional") # Si se coloca 0 el medio de transporte va a ser un Automovil Convencional
            print("1.- Vehiculo de Carga Pesada") # Si se coloca 1 el medio de transporte va a ser un Vehiculo de Carga Pesada
            print("2.- A pie") # Si se coloca 2 medio de transporte va a ser ir a pie
            print("") # espacio de tolerancia
            selector_vehiculo = input() # Se inserta la opcion seleccionada

            if selector_vehiculo == "0": # Si se coloco 0 hace este proceso
                routes = client.directions(coords, profile='driving-car') # Esta linea de codigo arroja un JSON que se utilizara mas adelante (con el perfil de driving-car)
                print("") # espacio de tolerancia
                print("Por medio de un automovil") # Nos menciona este mensaje
                verificador_de_input = True # Se le da el valor de True para que se pueda salir del blucle while
            elif selector_vehiculo == "1": # Si se coloco 1 hace este proceso
                routes = client.directions(coords, profile='driving-hgv') # Esta linea de codigo arroja un JSON que se utilizara mas adelante (con el perfil de driving-hgv)
                print("") # espacio de tolerancia
                print("Por medio de un vehiculo de carga pesada") # Nos menciona este mensaje
                verificador_de_input = True # Se le da el valor de True para que se pueda salir del blucle while
            elif selector_vehiculo == "2": # Si se coloco 2 hace este proceso
                routes = client.directions(coords, profile='foot-walking') # Esta linea de codigo arroja un JSON que se utilizara mas adelante (con el perfil de foot-walking)
                print("") # espacio de tolerancia
                print("Trasladandote a pie") # Nos menciona este mensaje
                verificador_de_input = True # Se le da el valor de True para que se pueda salir del blucle while
            else: # En caso de no insertar alguno de los valores anteriores
                print("La opción seleccionada no es válida. Por favor, seleccione una opción válida.") # Notifica al usuario que inserte una opcion valida


        distancia = float(routes['routes'][0]['summary']['distance']) # Extrae del JSON el valor de la distancia
        duracion = float(routes['routes'][0]['summary']['duration']) # Extrae del JSON el valor de la duracion o tiempo

        distancia = distancia/1000 # Ya que en el JSON se maneja por metros, se divide entre 1000 para que se conviertan a kilometros

        horas = int(duracion/3600) # Ya que en el JSON se maneja por segundos, se divide entre 3600 para que se conviertan a horas
        modulo_minutos = duracion % 3600 # Ahora los segundos restantes se van al valor de la variable
        minutos = int(modulo_minutos/60) # Se divide entre 60 para que se conviertan esos segundos a minutos
        segundos = int(modulo_minutos%60) # Se extraen los segundos residuales de la operacion anterior
        
        print("La distancia de esta tienda es de", distancia, "kms") # Imprime el mensaje de cuanta distancia hay entre las coordenadas del usuario a las coordenadas de la tienda
        print("La duracion del trayecto es de",horas,"hrs", minutos, "min", segundos, "s") # Imprime el mensaje de cuanto tiempo se tarda en hacer este recorrido
        
    def compararTiendas(self): # Metodo para comparar distancias y tiempos entre tiendas
        encontrado = False # Asigna un False a la variable "encontrado" para que pueda servir como un determinante para el while
        while not encontrado: # Mientras "encontrado" tenga el valor de false va a seguir haciendo este bloque de codigo
            print("") # espacio de tolerancia 
            id_tienda_1 = input("Ingresa el ID de la primer tienda a comparar: ")  # Input donde se ingresa el id de la primer tienda
            with open('tiendas.csv', newline='') as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file) # Crea un objeto para poder leer el archivo
                for row in reader: # Se encarga de buscar un ID en el CSV
                    if row['id_tienda'] == id_tienda_1:  # Si el id de la tienda coincide con la variable dada anteriormente hacer lo siguiente
                        encontrado = True # darle el valor de True a "encontrado" para que pueda terminar el bucle y siga con el codigo
                        latitud_tienda_1 = float(row['latitud']) # Extrae el dato de la latitud del csv y lo guarda en la variable
                        longitud_tienda_1 = float(row['longitud']) # Extrae el dato de la longitud del csv y lo guarda en la variable
                        break # Rompe con el bucle for
                if not encontrado: # En caso de que no coincida el id de la tienda con alguna de la base de datos hace lo siguiente
                    print("No se encontró una tienda con ese ID.") # Notifica al usuario que no existe la id

        encontrado = False # Asigna un False a la variable "encontrado" para que pueda servir como un determinante para el while
        while not encontrado: # Mientras "encontrado" tenga el valor de false va a seguir haciendo este bloque de codigo
            print("") # espacio de tolerancia
            id_tienda_2 = input("Ingresa el ID de la segunda tienda a comparar: ") # Input donde se ingresa el id de la segunda tienda
            with open('tiendas.csv', newline='') as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file) # Crea un objeto para poder leer el archivo
                for row in reader: # Se encarga de buscar un ID en el CSV
                    if row['id_tienda'] == id_tienda_2 and id_tienda_1 != id_tienda_2: # Si el id de la tienda coincide con la variable dada anteriormente hacer lo siguiente, mas a parte checa si la id de la primera tienda no sea el mismo que el de la segunda
                        encontrado = True # darle el valor de True a "encontrado" para que pueda terminar el bucle y siga con el codigo
                        latitud_tienda_2 = float(row['latitud']) # Extrae el dato de la latitud del csv y lo guarda en la variable
                        longitud_tienda_2 = float(row['longitud']) # Extrae el dato de la longitud del csv y lo guarda en la variable
                        break # Rompe con el bucle
                if not encontrado: # En caso de que no coincida el id de la tienda con alguna de la base de datos o que sean iguales las 2 ID dadas hara lo siguiente
                    print("No se encontró una tienda con ese ID o es igual a la primera tienda ingresada.") # Notifica al usuario que no existe la id o esta duplicada

        with open('coordenadas.csv', newline='') as file: # Abre el archivo para poder leer filas de informacion
            reader = csv.reader(file) # Crea un objeto para poder leer el archivo
            # Obtiene las coordenadas del archivo y las guarda en dos variables
            for row in reader: # Se encarga de buscar las coordenadas del csv
                latitud_usuario = float(row[0]) # Extrae el dato de la latitud del csv y lo guarda en la variable
                longitud_usuario = float(row[1]) # Extrae el dato de la longitud del csv y lo guarda en la variable

        coords_1 = ((latitud_usuario,longitud_usuario),(latitud_tienda_1,longitud_tienda_1)) # En el primer parentesis va las coordenadas de inicio y en el segundo van las coordenadas del final (Para calcular distancia de la primer tienda)
        coords_2 = ((latitud_usuario,longitud_usuario),(latitud_tienda_2,longitud_tienda_2)) # En el primer parentesis va las coordenadas de inicio y en el segundo van las coordenadas del final (Para calcular distancia de la segunda tienda)

        client = openrouteservice.Client(key='5b3ce3597851110001cf6248019ddc51fa504a2899b6cc783504c4c5') # Se especifica la clave personal dada por OpenRoute 

        verificador_de_input = False # Variable la cual nos va a ayudar a verificar si es que el input que se va a dar mas adelante es correcto 
        while not verificador_de_input: # Mientras "Verificador_de_input" tenga el valor de false va a seguir haciendo este bloque de codigo
            print("") # espacio de tolerancia
            print("Seleccione el medio de transporte que se quiera utilizar") # Nos notifica que tenemos que seleccionar algunas de las opciones siguientes
            print("0.- Automovil Convencional") # Si se coloca 0 el medio de transporte va a ser un Automovil Convencional
            print("1.- Vehiculo de Carga Pesada") # Si se coloca 1 el medio de transporte va a ser un Vehiculo de Carga Pesada
            print("2.- A pie") # Si se coloca 2 medio de transporte va a ser ir a pie
            print("") # espacio de tolerancia
            selector_vehiculo = input() # Se inserta la opcion seleccionada

            if selector_vehiculo == "0": # Si se coloco 0 hace este proceso
                routes1 = client.directions(coords_1, profile='driving-car') # Esta linea de codigo arroja un JSON de la ruta de la primer tienda que se utilizara mas adelante (con el perfil de driving-car)
                routes2 = client.directions(coords_2, profile='driving-car') # Esta linea de codigo arroja un JSON de la ruta de la segunda tienda que se utilizara mas adelante (con el perfil de driving-car)
                print("") # espacio de tolerancia
                print("Por medio de un automovil") # Nos menciona este mensaje
                verificador_de_input = True # Se le da el valor de True para que se pueda salir del blucle while

            elif selector_vehiculo == "1": # Si se coloco 1 hace este proceso
                routes1 = client.directions(coords_1, profile='driving-hgv') # Esta linea de codigo arroja un JSON de la ruta de la primer tienda que se utilizara mas adelante (con el perfil de driving-hgv)
                routes2 = client.directions(coords_2, profile='driving-hgv') # Esta linea de codigo arroja un JSON de la ruta de la segunda tienda que se utilizara mas adelante (con el perfil de driving-hgv)
                print("") # espacio de tolerancia
                print("Por medio de un vehiculo de carga pesada") # Nos menciona este mensaje
                verificador_de_input = True # Se le da el valor de True para que se pueda salir del blucle while

            elif selector_vehiculo == "2": # Si se coloco 2 hace este proceso
                routes1 = client.directions(coords_1, profile='foot-walking') # Esta linea de codigo arroja un JSON de la ruta de la primer tienda que se utilizara mas adelante (con el perfil de foot-walking)
                routes2 = client.directions(coords_2, profile='foot-walking') # Esta linea de codigo arroja un JSON de la ruta de la segunda tienda que se utilizara mas adelante (con el perfil de foot-walking)
                print("") # espacio de tolerancia
                print("Trasladandote a pie") # Nos menciona este mensaje
                verificador_de_input = True # Se le da el valor de True para que se pueda salir del blucle while

            else: # En caso de no insertar alguno de los valores anteriores
                print("La opción seleccionada no es válida. Por favor, seleccione una opción válida.") # Notifica al usuario que inserte una opcion valida

        distancia_1 = float(routes1['routes'][0]['summary']['distance']) # Extrae del JSON el valor de la distancia de la ruta de la tienda 1
        duracion_1 = float(routes1['routes'][0]['summary']['duration']) # Extrae del JSON el valor de la duracion o tiempo de la ruta de la tienda 1

        distancia_2 = float(routes2['routes'][0]['summary']['distance']) # Extrae del JSON el valor de la distancia de la ruta de la tienda 2
        duracion_2 = float(routes2['routes'][0]['summary']['duration']) # Extrae del JSON el valor de la duracion o tiempo de la ruta de la tienda 2

        if distancia_1 > distancia_2 and duracion_1 > duracion_2: # Si la distancia y el tiempo de duracion de la tienda 1 es mayor al de la tienda 2 se hace lo siguiente
            distancia_total = distancia_1 - distancia_2 # Se hace la operacion para sacar la diferencia de distancias entre las rutas de las tiendas
            duracion_total = duracion_1 - duracion_2 # Se hace la operacion para sacar la diferencia de tiempo de recorrido entre las rutas de las tiendas

            distancia_total = distancia_total/1000 # Ya que en el JSON se maneja por metros, se divide entre 1000 para que se conviertan a kilometros

            horas = int(duracion_total/3600) # Ya que en el JSON se maneja por segundos, se divide entre 3600 para que se conviertan a horas
            modulo_minutos = duracion_total % 3600 # Ahora los segundos restantes se van al valor de la variable
            minutos = int(modulo_minutos/60) # Se divide entre 60 para que se conviertan esos segundos a minutos
            segundos = int(modulo_minutos%60) # Se extraen los segundos residuales de la operacion anterior
            print("La tienda",id_tienda_2,"es mas cercana a tu ubicacion que la tienda",id_tienda_1,"por una diferencia de:") # Notifica el siguiente mensaje
            print(distancia_total, "kms de distancia") # Muestra la distancia de diferencia
            print("Y",horas,"hrs", minutos, "min", segundos, "s de tiempo de trayecto") # Y el tiempo de diferencia 

        elif distancia_2 > distancia_1 and duracion_2 > duracion_1: # Si la distancia y el tiempo de duracion de la tienda 2 es mayor al de la tienda 1 se hace lo siguiente
            distancia_total = distancia_2 - distancia_1 # Se hace la operacion para sacar la diferencia de distancias entre las rutas de las tiendas
            duracion_total = duracion_2 - duracion_1 # Se hace la operacion para sacar la diferencia de tiempo de recorrido entre las rutas de las tiendas

            distancia_total = distancia_total/1000 # Ya que en el JSON se maneja por metros, se divide entre 1000 para que se conviertan a kilometros

            horas = int(duracion_total/3600) # Ya que en el JSON se maneja por segundos, se divide entre 3600 para que se conviertan a horas
            modulo_minutos = duracion_total % 3600 # Ahora los segundos restantes se van al valor de la variable
            minutos = int(modulo_minutos/60) # Se divide entre 60 para que se conviertan esos segundos a minutos
            segundos = int(modulo_minutos%60) # Se extraen los segundos residuales de la operacion anterior
            print("La tienda",id_tienda_1,"es mas cercana a tu ubicacion que la tienda",id_tienda_2,"por una diferencia de:") # Notifica el siguiente mensaje
            print(distancia_total, "kms de distancia") # Muestra la distancia de diferencia
            print("Y",horas,"hrs", minutos, "min", segundos, "s de tiempo de trayecto") # Y el tiempo de diferencia 
        
    def asignarCoordenadas(self): # Metodo para asignar coordenadas de usuario
        # Pide la latitud y longitud al usuario
        latitud = input("Ingresa la latitud: ") # Input en donde pide la nueva latitud
        longitud = input("Ingresa la longitud: ") # Input en donde pide la nueva longitud

        with open('coordenadas.csv', 'w', newline='') as file: # Abre el csv en modo de write
            writer = csv.writer(file) # Crea un onjeto para sobreescribir en el archivo csv
            writer.writerow([latitud, longitud]) # Sobreescribe la linea del csv con los valores dados

        print("Las coordenadas han sido guardadas correctamente.") # Notifica que las coordenadas han sido guardadas correctamente

    def leerCoordenadas(self): # Metodo para obtener las coordenadas que estan guardadas para el usuario
        with open('coordenadas.csv', newline='') as file: # Abre el archivo para poder leer filas de informacion
            reader = csv.reader(file) # Crea un objeto para poder leer el archivo

            for row in reader: # Se encarga de buscar las coordenadas del csv
                latitud_usuario = float(row[0]) # Extrae el dato de la latitud del csv y lo guarda en la variable
                longitud_usuario = float(row[1]) # Extrae el dato de la longitud del csv y lo guarda en la variable

        print("Las coordenadas establecidas son:") # Muestra el mensaje que notifica que las coordenadas fueron encontradas
        print("Latitud: ", latitud_usuario) # Muestra la latitud
        print("Longitud: ", longitud_usuario) # Muestra la longitud


    def obtenerCoordenadas(self): # Metodo para obtener las coordenadas de una tienda
        encontrado = False # Asigna un False a la variable "encontrado" para que pueda servir como un determinante para el while
        while not encontrado: # Mientras "encontrado" tenga el valor de false va a seguir haciendo este bloque de codigo
            id_tienda = input("Ingresa el ID de la tienda: ") # Input donde se ingresa el id de la tienda
            with open('tiendas.csv', newline='') as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file) # Crea un objeto para poder leer el archivo
                for row in reader: # Se encarga de buscar un ID en el CSV
                    if row['id_tienda'] == id_tienda: # Si el id de la tienda coincide con la variable dada anteriormente hacer lo siguiente
                        encontrado = True # darle el valor de True a "encontrado" para que pueda terminar el bucle y siga con el codigo
                        latitud = float(row['latitud']) # Extrae el dato de la latitud del csv y lo guarda en la variable
                        longitud = float(row['longitud']) # Extrae el dato de la longitud del csv y lo guarda en la variable
                        print("Las coordenadas de la tienda son:") # Muestra el mensaje que notifica que las coordenadas fueron encontradas
                        print("Latitud:", latitud) # Muestra la latitud
                        print("Longitud:", longitud) # Muestra la longitud
                        break # Rompe con el bucle
                if not encontrado: # En caso de que no coincida el id de la tienda con alguna de la base de datos hace lo siguiente
                    print("No se encontró una tienda con ese ID.") # Notifica al usuario que no existe la id




rastreador = Rastreador() # Crea el objeto rastreador para poder llamar a los metodos
#rastreador.asignarCoordenadas()
#rastreador.leerCoordenadas()
#rastreador.obtenerCoordenadas()
#rastreador.rastrearTienda()
#rastreador.compararTiendas()
