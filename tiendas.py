import csv  # Librería para abrir, leer y escribir archivos CSV
import os  # Importa el modulo os


class Tiendas:  # Clase Tiendas

    def __init__(self):  # Construcctor de la clase Tiendas
        pass  # Inicializa el objeto Tiendas

    def listarTiendas(self) -> bool: # Metodo para listar los productos registrados
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa

            with open("tiendas.csv", "r") as file: # Abre el archivo para tener acceso a los registros
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,

                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    print(f"Registro: {row}") # imprime los datos del registro como un diccionario
                    
            print("") # Espacio de tolerancia a la hora de imprimir el programa
            return True # Regresa True si el metodo se ejecuto correctamente
        
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error listarTiendas() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo
        
    def insertarTienda(self)-> bool:
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            while True: # Bucle infinito para mostrar las opciones del sistema
                id = input("Inserte el ID de la tienda: ") # Input para recibir el SKU para agregarlo
                with open('tiendas.csv', 'r', newline='') as file: # Abre el archivo para poder leer filas de informacion
                    reader = csv.reader(file) # Crear un objeto reader

                    for row in reader:  # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                        if row and row[0] == id: # Si el sku ya existe en la lista de sku, se imprime el mensaje y se continúa con el ciclo while
                            print("Tienda ya existente") # Notifica al usuario que el sku ya esta en uso
                            break # Break para romper el bluce "for"

                    else: # else por si no exista ese sku y pueda seguir con el programa
                        with open('tiendas.csv', 'a', newline='') as file: # Abre el archivo para poder agregar filas de informacion
                            writer = csv.writer(file) # Crear un objeto writer
                    
                            # Agregar la fila de información

                            nombre = input("Inserte Nombre de la tienda: ") # Input para recibir el nombre para agregarlo
                            altitud = input("Inserte la Altitud de la tienda: ") # Input para recibir el altitud para agregarlo
                            latitud = input("Inserte la Latitud de la tienda: ") # Input para recibir la latitud para agregarlo
                            direccion = input("Inserte la Direccion de la tienda: ") # Input para recibir la direccion para agregarlo
                            fila = [id, nombre, altitud, latitud, direccion] # La variable "fila" es asignada con los valores anteriormente dados de "sku", "nombre", "unidad"
                            writer.writerow(fila) # Utiliza el objeto "writer" para poder sobreescribir la fila de informacion del csv con el metodo de la libreria CSV "writerow()"
                            print("") # Espacio de tolerancia a la hora de imprimir el programa
                            print("Tienda agregada con exito")
                            print("") # Espacio de tolerancia a la hora de imprimir el programa
                            break

                
        except Exception as e: # Atrapa cualquier excepcion
                print(f"Error insertarProducto() :{e.args}") # Muestra en consola el error que ocurrio
                return False # Regresa False si ocurrio un error en el metodo


    def buscarTienda(self) -> bool: # Metodo para buscar tiendas
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("tiendas.csv", "r") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,

                id_buscar = input("Ingrese el id de la tienda que desea buscar: ") # Pide al usuario el id a buscar
                encontrado = False # Variable para indicar si se encontró la tienda o no

                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    if row['id'] == id_buscar: # Compara el id buscando
                        print(f"Registro encontrado: {row}") # Imprime la fila encontrada
                        encontrado = True # Marca la tienda como encontrada
                        break # Termina el bucle ya que se encontró el producto

                if not encontrado: # If por si no exista el sku
                    print("Tienda no encontrada") # Imprime el mensaje si la tienda no se encontró

            return True # Retorna True si el método se ejecutó correctamente

        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error buscarTienda(): {e.args}") # Muestra en consola el error que ocurrio
            return False  # Regresa False si ocurrio un error en el metodo

    def borrarTienda(self) -> bool: # Metodo para borrar tiendas por direccion
        with open('tiendas.csv', 'r', newline='') as archivo, open('temp.csv', 'w', newline='') as archivo_temp: # abre dos archivos en modo de lectura y escritura respectivamente, utilizando la función open() de Python.
                lector_csv = csv.reader(archivo)  # se crea un objeto csv.reader que permite iterar por cada fila del archivo CSV y se asigna a la variable lector_csv
                escritor_csv = csv.writer(archivo_temp)  # También se crea un objeto csv.writer que permite escribir en el archivo temporal y se asigna a la variable escritor_csv

                id = input("Inserte ID de la tienda: ") # Input para borrar el sku correspondiente
                for fila in lector_csv: # Recorre todos los registros de "productos.csv"
                    if fila[0] != id: # si la fila no contiene el producto que deseas borrar, escribirla en el archivo de salida
                        escritor_csv.writerow(fila) # Utiliza el objeto "writer" para poder sobreescribir la fila de informacion del csv con el metodo de la libreria CSV "writerow()"
                    

        import os # Importa el modulo os
        os.replace('temp.csv', 'tiendas.csv') # reemplazar el archivo original con el archivo de salida

        print("") # Espacio de tolerancia a la hora de imprimir el programa
        print("Tienda borrada con exito")
        print("") # Espacio de tolerancia a la hora de imprimir el programa

    def actualizarTienda(self)-> bool: # Metodo para actualizar una Tienda
        id = input("Ingresa la ID de la tienda a reemplazar: ") # Input para borrar el id correspondiente
        while True: # Bucle que lo que hace es buscar el valor "id" en la tabla CSV
            encontrado = False # Se utiliza para determinar si la ID ingresado por el usuario existe en el archivo CSV
            with open("tiendas.csv") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file) # se crea un objeto con la valriable "reader"
                for row in reader: #Se encarga de buscar un sku en el CSV
                    if row['id'] == id: # condicion de si el valor de la columna "ID" es igual a el valor del ID dado por el usuario pasa lo siguiente
                        encontrado = True # la variable "encontrado" cambia de valor a True, dando como encontrado una ID en el csv
                        break # break con la funcion de terminar con el if y pasar al siguiente paso
            if encontrado: # condicion de que si encontrado esta en True
                break # si se cumple la condicion del if, el break se activa pasando al siguiente paso
            else: # else para la condicion if por si no se cumple
                id = input("La ID ingresada no existe en el archivo, por favor ingresa una ID válida: ") # le imprime al usuario el mensaje presentado y le pide que inserte nuevamente un ID hasta que haya una coincidencia entre el valor dado y el CSV
        
        id_nuevo = input("Ingresa el nuevo valor de la ID: ") # input para preguntar el nuevo valor de la ID
        while True: # Bucle que lo que hace es buscar el valor "ID" en la tabla CSV
            if id_nuevo == id: # Condicion que dicta que si id_nuevo es igual a sku
                break # Pasar al siguiente paso del codigo, rompiendo con el if
            else: # en caso de que id_nuevo no es igual a sku
                encontrado = False # Se utiliza para determinar si el SKU ingresado por el usuario existe en el archivo CSV
                with open("tiendas.csv") as file: # Abre el archivo para poder leer filas de informacion
                    reader = csv.DictReader(file) # se crea un objeto con la valriable "reader"
                    for row in reader:  # Se encarga de buscar un sku en el CSV
                        if row['id'] == id_nuevo: # condicion de si el valor de la columna "id" es igual a el valor de la variable id_nuevo dado por el usuario pasa lo siguiente
                            encontrado = True # la variable "encontrado" cambia de valor a True, dando como encontrado una ID en el csv
                            break # break con la funcion de terminar con el if y pasar al siguiente paso
                if encontrado: # condicion de que si encontrado esta en True
                    sku_nuevo = input("La ID ingresada ya existe en el archivo, por favor ingresa una ID válida: ") # le imprime al usuario el mensaje presentado y le pide que inserte nuevamente una ID hasta que NO haya una coincidencia entre el valor dado y el CSV
                else: # en caso de que no exista el sku dado en la tabla del CSV
                    break # break con la funcion de terminar con el if y pasar al siguiente paso
        
        nombre_nuevo = input("Ingresa el nuevo nombre de la tienda: ") # input para preguntar el nuevo nombre de la tienda
        altitud_nuevo = input("Ingrese la nueva altitud: ") # input para preguntar la nueva altitud de la tienda
        laltitud_nuevo = input("Ingrese la nueva laltitud: ") # input para preguntar la nueva laltitud de la tienda
        direccion_nuevo = input("Ingrese la nueva direccion: ") # input para preguntar la nueva direccion de la tienda
        with open("tiendas.csv", "r") as f: # Abre el archivo para poder leer filas de informacion
            reader = csv.reader(f) # se crea un objeto con la variable "reader"
            rows = list(reader) # se crea un objeto con la variable "rows" para leer las columnas del CSV
        
        with open("tiendas.csv", "w", newline='') as f: # Abre el archivo para poder sobreescribir filas de informacion
            writer = csv.writer(f) # se crea un objeto con la variable "writer" para poder sobreescribir filas de informacion
            for row in rows: #Se encarga de leer las columnas del CSV
                if row[0] == id: # Condicion que dicta que entre los valores que hay en la columna del CSV numero 0 se encuentra el valor de la ID
                    row[0] = id_nuevo # Asignacion de valor a la columna 0 en la fila correspondiente del CSV
                    row[1] = nombre_nuevo # Asignacion de valor a la columna 1 en la fila correspondiente del CSV
                    row[2] = altitud_nuevo # Asignacion de valor a la columna 2 en la fila correspondiente del CSV
                    row[3] = laltitud_nuevo # Asignacion de valor a la columna 3 en la fila correspondiente del CSV
                    row[4] = direccion_nuevo # Asignacion de valor a la columna 3 en la fila correspondiente del CSV
                writer.writerow(row) # Finalmente sobreescribe con este metodo la fila de informacion de la tienda
        
        print("La tienda fue actualizada de forma exitosa") # Notifica con un print de que la tienda fue actualizado de forma exitosa

tiendas = Tiendas()
#tiendas.borrarTienda() # Llamada al metodo para borrar una tienda
#tiendas.insertarTienda() # Llamada al metodo para insertar una tienda
#tiendas.listarTienda() # Llamada al metodo para listar una tienda
#tiendas.buscarTienda() # Llamada al metodo para buscar una tienda
#tiendas.actualizarTienda() # Llamada al metodo para actualizar una tienda


