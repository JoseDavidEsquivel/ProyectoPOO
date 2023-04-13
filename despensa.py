import csv  # Librería para abrir, leer y escribir archivos CSV

def obtener_ultimo_id_compra(): # Metodo para obtener el ultimo id de la compra
    with open("despensa.csv") as file: # Abre el archivo para tener acceso a los registros
        reader = csv.reader(file) # Crer un objeto reader para leer los registros
        ultimo_id_compra = 0 # Le asigna el valor 0 a la variable
        for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
            ultimo_id_compra = row[0] # Este le asigna el valor de la ultima id_compra
        return int(ultimo_id_compra) + 1 # Convierte a entero el valor de la id_compra y le suma 1

class Despensa:  # Clase Despensa

    def __init__(self): # Constructor de la clase
        pass # Inicializa el objeto

    def listarDespensa(self) -> bool: # Metodo para listar compras registradas
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("despensa.csv", "r") as file: # Abre el archivo para tener acceso a los registros
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,
                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    print(f"Registro: {row}") # imprime los datos del registro como un diccionario
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error listarProductos() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo
        return False # Regresa False si ocurrio un error en el metodo # Regresa False si ocurrio un error en el metodo

    def insertarDespensa(self) -> bool: # Metodo para insertarDespesa()
        id_compra = str(obtener_ultimo_id_compra()) # Le asigna el valor de el metodo "obtener_ultimo_id_compra" a la variable
        
        sku = input("Ingresa el valor del SKU: ") # Input para buscar el sku en el productos.csv
        while True: # Bucle que lo que hace es buscar el valor "sku" en la tabla CSV
            encontrado = False # Se utiliza para determinar si el SKU ingresado por el usuario existe en el archivo CSV
            with open("productos.csv") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file) # se crea un objeto con la valriable "reader"
                for row in reader: #Se encarga de buscar un sku en el CSV
                    if row['sku'] == sku: # condicion de si el valor de la columna "sku" es igual a el valor del sku dado por el usuario pasa lo siguiente
                        encontrado = True # la variable "encontrado" cambia de valor a True, dando como encontrado un sku en el csv
                        break # break con la funcion de terminar con el if y pasar al siguiente paso
            if encontrado: # condicion de que si encontrado esta en True
                break # si se cumple la condicion del if, el break se activa pasando al siguiente paso
            else: # else para la condicion if por si no se cumple
                sku = input("El SKU ingresado no existe en la base de datos, por favor ingresa un SKU existente: ") # le imprime al usuario el mensaje presentado y le pide que inserte nuevamente un sku hasta que haya una coincidencia entre el valor dado y el CSV

        id_tienda = input("Ingresa la id de la tienda: ") # Input para buscar el sku en el productos.csv
        while True: # Bucle que lo que hace es buscar el valor "sku" en la tabla CSV
            encontrado = False # Se utiliza para determinar si el SKU ingresado por el usuario existe en el archivo CSV
            with open("tiendas.csv") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file) # se crea un objeto con la valriable "reader"
                for row in reader: #Se encarga de buscar un sku en el CSV
                    if row['id_tienda'] == id_tienda: # condicion de si el valor de la columna "sku" es igual a el valor del sku dado por el usuario pasa lo siguiente
                        encontrado = True # la variable "encontrado" cambia de valor a True, dando como encontrado un sku en el csv
                        break # break con la funcion de terminar con el if y pasar al siguiente paso
            if encontrado: # condicion de que si encontrado esta en True
                break # si se cumple la condicion del if, el break se activa pasando al siguiente paso
            else: # else para la condicion if por si no se cumple
                id_tienda = input("La tienda ingresada no existe en la base de datos, por favor ingresa una tienda existente: ") # le imprime al usuario el mensaje presentado y le pide que inserte nuevamente un sku hasta que haya una coincidencia entre el valor dado y el CSV
        
        fecha_dia= input("Ingrese el numero de dia de la compra (Ejemplo: 4, 30, 24): ") # Pregunta por el dia de la compra
        fecha_mes= input("Ingrese el numero del mes de la compra (Ejemplo: 3, 10, 12): ") # Pregunta por el mes de la compra
        fecha_año= input("Ingrese el año de la compra (Ejemplo: 2022, 2030, 2024): ") # Pregunta por el año de la compra

        fecha = fecha_dia+"/"+fecha_mes+"/"+fecha_año # Concatena los valores dados separandolos por "/" para dar un valor a la variable fecha similar a "23/03/2023"
        precio_unitario = float(input("Inserte el precio unitario (si es decimal, porfavor de usar punto.): ")) # Input para recibir el nombre para agregarlo
        cantidad = int(input("Inserte la cantidad de productos comprados: ")) #Inserta la cantidad de productos comprados
        precio_total = precio_unitario*cantidad # Hace la operacion de precio_unitario por cantidad para hacer el calculo de precio_total

        fila = [id_compra, id_tienda, sku, fecha, precio_unitario, cantidad, precio_total] # La variable "fila" es asignada con los valores anteriormente dados de "sku", "nombre", "unidad"
        with open('despensa.csv', 'a', newline='') as file: # Abre el archivo para poder agregar filas de informacion
            writer = csv.writer(file) # Crear un objeto writer
            writer.writerow(fila) # Utiliza el objeto "writer" para poder sobreescribir la fila de informacion del csv con el metodo de la libreria CSV "writerow()"
            print("La compra ha sido añadida correctamente") # Le informa al usuario que el producto a sido añadido de forma exitosa
            print("") # Espacio de tolerancia a la hora de imprimir el programa

    def buscarDespensa(self) -> bool: # Metodo para buscar despensa
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("despensa.csv", "r") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,

                fecha_dia= input("Ingrese el numero de dia de la compra (Ejemplo: 4, 30, 24): ") # Pregunta por el dia de la compra
                fecha_mes= input("Ingrese el numero del mes de la compra (Ejemplo: 3, 10, 12): ") # Pregunta por el mes de la compra
                fecha_año= input("Ingrese el año de la compra (Ejemplo: 2022, 2030, 2024): ") # Pregunta por el año de la compra

                fecha_buscar = fecha_dia+"/"+fecha_mes+"/"+fecha_año # Concatena los valores dados separandolos por "/" para dar un valor a la variable fecha similar a "23/03/2023"
                
                encontrado = False # Variable para indicar si se encontró la despensa o no

                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    if row['fecha'] == fecha_buscar: # Compara la fecha buscada
                        print(f"Registro encontrado: {row}") # Imprime la fila encontrada
                        encontrado = True # Marca la despensa como encontrada
                        break # Termina el bucle ya que se encontró la despensa

                if not encontrado: # If por si no exista la fecha de compra
                    print("Despensa no encontrada") # Imprime el mensaje si la despensa no se encontró

            return True # Retorna True si el método se ejecutó correctamente

        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error buscarDespensa(): {e.args}") # Muestra en consola el error que ocurrio
            return False  # Regresa False si ocurrio un error en el metodo

    def borrarDespensa(self) -> None: # Metodo para borrarDespensa()
       
            with open('despensa.csv', 'r', newline='') as archivo, open('temp.csv', 'w', newline='') as archivo_temp: # abre dos archivos en modo de lectura y escritura respectivamente, utilizando la función open() de Python.
                lector_csv = csv.reader(archivo)  # se crea un objeto csv.reader que permite iterar por cada fila del archivo CSV y se asigna a la variable lector_csv
                escritor_csv = csv.writer(archivo_temp)  # También se crea un objeto csv.writer que permite escribir en el archivo temporal y se asigna a la variable escritor_csv

                id = input("Inserte ID: ") # Input para borrar el sku correspondiente
                for fila in lector_csv: # Recorre todos los registros de "productos.csv"
                    if fila[0] != id: # si la fila no contiene el producto que deseas borrar, escribirla en el archivo de salida
                        escritor_csv.writerow(fila) # Utiliza el objeto "writer" para poder sobreescribir la fila de informacion del csv con el metodo de la libreria CSV "writerow()"

            import os#importa al modo os
            os.replace('temp.csv', 'despensa.csv') # reemplazar el archivo original con el archivo de salida

            print("") # Espacio de tolerancia a la hora de imprimir el programa
            print("despensa borrada con exito") # Notifica de que la despensa fue borrada con exito
            print("") # Espacio de tolerancia a la hora de imprimir el programa
            
    def actualizarDespensa(self) -> None: # Metodo para actualizarDespensa()
        id_compra_busqueda = input("Ingresa el ID de la compra a reemplazar: ") # Input para borrar el id_compra correspondiente
        while True: # Bucle que lo que hace es buscar el valor "id_compra_busqueda" en la tabla CSV
            encontrado = False # Se utiliza para determinar si el SKU ingresado por el usuario existe en el archivo CSV
            with open("despensa.csv") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file) # se crea un objeto con la valriable "reader"
                for row in reader: #Se encarga de buscar un sku en el CSV
                    if row['id_compra'] == id_compra_busqueda: # condicion de si el valor de la columna "id_compra" es igual a el valor del sku dado por el usuario pasa lo siguiente
                        encontrado = True # la variable "encontrado" cambia de valor a True, dando como encontrado un sku en el csv
                        break # break con la funcion de terminar con el if y pasar al siguiente paso
            if encontrado: # condicion de que si encontrado esta en True
                break # si se cumple la condicion del if, el break se activa pasando al siguiente paso
            else: # else para la condicion if por si no se cumple
                id_compra_busqueda = input("El ID ingresado no existe en el archivo, por favor ingresa un ID existente: ") # le imprime al usuario el mensaje presentado y le pide que inserte nuevamente un id hasta que haya una coincidencia entre el valor dado y el CSV

        sku = input("Ingresa el valor del SKU: ") # Input para buscar el sku en el productos.csv
        while True: # Bucle que lo que hace es buscar el valor "sku" en la tabla CSV
            encontrado = False # Se utiliza para determinar si el SKU ingresado por el usuario existe en el archivo CSV
            with open("productos.csv") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file) # se crea un objeto con la valriable "reader"
                for row in reader: #Se encarga de buscar un sku en el CSV
                    if row['sku'] == sku: # condicion de si el valor de la columna "sku" es igual a el valor del sku dado por el usuario pasa lo siguiente
                        encontrado = True # la variable "encontrado" cambia de valor a True, dando como encontrado un sku en el csv
                        break # break con la funcion de terminar con el if y pasar al siguiente paso
            if encontrado: # condicion de que si encontrado esta en True
                break # si se cumple la condicion del if, el break se activa pasando al siguiente paso
            else: # else para la condicion if por si no se cumple
                sku = input("El SKU ingresado no existe en la base de datos, por favor ingresa un SKU existente: ") # le imprime al usuario el mensaje presentado y le pide que inserte nuevamente un sku hasta que haya una coincidencia entre el valor dado y el CSV

        id_tienda = input("Ingresa la id de la tienda: ") # Input para buscar el sku en el productos.csv
        while True: # Bucle que lo que hace es buscar el valor "sku" en la tabla CSV
            encontrado = False # Se utiliza para determinar si el SKU ingresado por el usuario existe en el archivo CSV
            with open("tiendas.csv") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file) # se crea un objeto con la valriable "reader"
                for row in reader: #Se encarga de buscar un sku en el CSV
                    if row['id_tienda'] == id_tienda: # condicion de si el valor de la columna "sku" es igual a el valor del sku dado por el usuario pasa lo siguiente
                        encontrado = True # la variable "encontrado" cambia de valor a True, dando como encontrado un sku en el csv
                        break # break con la funcion de terminar con el if y pasar al siguiente paso
            if encontrado: # condicion de que si encontrado esta en True
                break # si se cumple la condicion del if, el break se activa pasando al siguiente paso
            else: # else para la condicion if por si no se cumple
                id_tienda = input("La tienda ingresada no existe en la base de datos, por favor ingresa una tienda existente: ") # le imprime al usuario el mensaje presentado y le pide que inserte nuevamente un sku hasta que haya una coincidencia entre el valor dado y el CSV
        
        fecha_dia= input("Ingrese el numero de dia de la compra (Ejemplo: 4, 30, 24): ") # Pregunta por el dia de la compra
        fecha_mes= input("Ingrese el numero del mes de la compra (Ejemplo: 3, 10, 12): ") # Pregunta por el mes de la compra
        fecha_año= input("Ingrese el año de la compra (Ejemplo: 2022, 2030, 2024): ") # Pregunta por el año de la compra

        fecha = fecha_dia+"/"+fecha_mes+"/"+fecha_año # Concatena los valores de las fechas y agrega entremedias un "/" para su reemplazo en la tabla
        precio_unitario = float(input("Inserte el precio unitario (si es decimal, porfavor de usar punto.): ")) # Input para recibir el precio por pieza del producto
        cantidad = int(input("Inserte la cantidad de productos comprados: ")) # Input para recibir la cantidad productos comprados
        precio_total = precio_unitario*cantidad # Hace la operacion de precio_unitario por cantidad para hacer el calculo de precio_total

        #fila = [id_compra_busqueda, id_tienda, sku, fecha, precio_unitario, cantidad, precio_total] # La variable "fila" es asignada con los valores anteriormente dados de "sku", "nombre", "unidad"
        with open("despensa.csv", "r") as f: # Abre el archivo para poder leer filas de informacion
            reader = csv.reader(f) # se crea un objeto con la variable "reader"
            rows = list(reader) # se crea un objeto con la variable "rows" para leer las columnas del CSV

        with open("despensa.csv", "w", newline='') as f: # Abre el archivo para poder sobreescribir filas de informacion
            writer = csv.writer(f) # se crea un objeto con la variable "writer" para poder sobreescribir filas de informacion
            for row in rows: #Se encarga de leer las columnas del CSV
                if row[0] == id_compra_busqueda: # Condicion que dicta que entre los valores que hay en la columna del CSV numero 0 se encuentra el valor del sku
                    row[0] = id_compra_busqueda # Asignacion de valor a la columna 0 en la fila correspondiente del CSV
                    row[1] = id_tienda # Asignacion de valor a la columna 1 en la fila correspondiente del CSV
                    row[2] = sku # Asignacion de valor a la columna 2 en la fila correspondiente del CSV
                    row[3] = fecha # Asignacion de valor a la columna 3 en la fila correspondiente del CSV
                    row[4] = precio_unitario # Asignacion de valor a la columna 4 en la fila correspondiente del CSV
                    row[5] = cantidad # Asignacion de valor a la columna 5 en la fila correspondiente del CSV
                    row[6] = precio_total # Asignacion de valor a la columna 6 en la fila correspondiente del CSV
                writer.writerow(row) # Finalmente sobreescribe con este metodo la fila de informacion del producto
        
        print("La despensa fue actualizada de forma exitosa") # Notifica con un print de que el producto fue actualizado de forma exitosa

    def valorMinimoProducto(self,sku:str) -> None: # Metodo para mostrar el valor minimo de un producto
        # TODO programar el método valorMinimoProducto()
        return False # Regresa False si ocurrio un error en el metodo

   def valorMaximoProducto(sku):
     
        sku = input("Inserte el producto a checar ")
        with open('despensa.csv') as file: # Abrir el archivo CSV
            reader = csv.DictReader(file) # Leer el archivo CSV
            precio_maximo = None # Inicializar el precio máximo como el precio de la primera fila que coincide con el SKU
            filas_precio_maximo = [] # Inicializar la lista de filas correspondientes al precio máximo como vacía
            
            for row in reader: # Iterar sobre cada fila del archivo CSV
                if row['sku'] == sku and (precio_maximo is None or float(row['precio_unitario']) > precio_maximo): # Si el SKU de la fila coincide con el SKU proporcionado y el precio máximo no ha sido inicializado
                    precio_maximo = float(row['precio_unitario']) # Actualizar el precio máximo
                    filas_precio_maximo = [row] # Limpiar la lista de filas correspondientes al precio máximo y añadir la fila actual
                elif row['sku'] == sku and float(row['precio_unitario']) == precio_maximo: # Si el SKU de la fila coincide con el SKU proporcionado y el precio es igual al precio máximo
                    filas_precio_maximo.append(row) # Añadir la fila actual a la lista de filas correspondientes al precio máximo

            if filas_precio_maximo: # Si se encontró algún precio máximo
                for fila_precio_maximo in filas_precio_maximo: # Imprimir todas las filas correspondientes al precio máximo
                    print(fila_precio_maximo) # Imprime las filas que contengan el precio maximo

            else: # En caso
                # Si no se encontró ningún SKU, imprimir un mensaje de error
                print(f"No se encontró ningún SKU {sku}") # Mensaje de error
                
despensa = Despensa() # Crea un objeto de la clase despensa
#despensa.listarDespensa() # Llama al metodo listarDespensa()
#despensa.buscarDespensa() # Llama al metodo buscarDespensa()
#despensa.borrarDespensa() # Llama al metodo borrarDespensa()
despensa.ValormaximiProducto()# llama al metodo Valor maximo
