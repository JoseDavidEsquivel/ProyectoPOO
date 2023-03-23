import csv  # Librería para abrir, leer y escribir archivos CSV


print("") # Espacio de tolerancia a la hora de imprimir el programa

class Productos:  # Clase Productos

    def __init__(self): # Constructor de la clase Productos
        pass # Inicializa el objeto de la clase Productos

    def listarProductos(self) -> bool: # Metodo para listar los productos registrados
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("productos.csv", "r") as file: # Abre el archivo para tener acceso a los registros
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,
                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    print(f"Registro: {row}") # imprime los datos del registro como un diccionario
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error listarProductos() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo

    def insertarProducto(self) -> bool: # Metodo para insertar productos
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            while True: # Bucle infinito para mostrar las opciones del sistema
                sku = input("Inserte SKU: ") # Input para recibir el SKU para agregarlo
                with open('productos.csv', 'r', newline='') as file: # Abre el archivo para poder leer filas de informacion
                    reader = csv.reader(file) # Crear un objeto reader

                    for row in reader:  # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                        if row and row[0] == sku: # Si el sku ya existe en la lista de sku, se imprime el mensaje y se continúa con el ciclo while
                            print("Producto ya existente") # Notifica al usuario que el sku ya esta en uso
                            break # Break para romper el bluce "for"

                    else: # else por si no exista ese sku y pueda seguir con el programa
                        nombre = input("Inserte Nombre: ") # Input para recibir el nombre para agregarlo
                        while True: # Bucle infinito para mostrar las opciones del sistema

                            print("Inserte que tipo de unidad quiere") # Pregunta al usuario que tipo de unidad quiere (Dado a que hay dos tipos de unidad existentes en el sistema "pieza" y "paquete")
                            print("") # Espacio de tolerancia a la hora de imprimir el programa
                            print("0.- Pieza") # Muestra la opcion de pieza relacionado con el numero 0
                            print("1.- Paquete") # Muestra la opcion de paquete relacionado con el numero 1
                            valorunidad = input("") # Input para recibir la opcion elegida por el usuario entre 0 y 1

                            if valorunidad == "0": # If que dicta que si el valor es 0 hace lo siguiente

                                unidad = "pieza" # Le da el valor de "pieza" a la variable unidad
                                fila = [sku, nombre, unidad] # La variable "fila" es asignada con los valores anteriormente dados de "sku", "nombre", "unidad"
                                with open('productos.csv', 'a', newline='') as file: # Abre el archivo para poder agregar filas de informacion
                                    writer = csv.writer(file) # Crear un objeto writer
                                    writer.writerow(fila) # Utiliza el objeto "writer" para poder sobreescribir la fila de informacion del csv con el metodo de la libreria CSV "writerow()"
                                print("El producto ha sido añadido correctamente") # Le informa al usuario que el producto a sido añadido de forma exitosa
                                print("") # Espacio de tolerancia a la hora de imprimir el programa
                                return False # Regresa False para terminar el bucle while que daba como condicion un True para seguir funcionando
                            
                            elif valorunidad == "1": # If que dicta que si el valor es 1 hace lo siguiente

                                unidad = "paquete" # Le da el valor de "paquete" a la variable unidad
                                fila = [sku, nombre, unidad] # La variable "fila" es asignada con los valores anteriormente dados de "sku", "nombre", "unidad"
                                with open('productos.csv', 'a', newline='') as file: # Abre el archivo para poder agregar filas de informacion
                                    writer = csv.writer(file) # Crear un objeto writer
                                    writer.writerow(fila) # Utiliza el objeto "writer" para poder sobreescribir la fila de informacion del csv con el metodo de la libreria CSV "writerow()"
                                print("El producto ha sido añadido correctamente") # Le informa al usuario que el producto a sido añadido de forma exitosa
                                print("") # Espacio de tolerancia a la hora de imprimir el programa
                                return False # Regresa False para terminar el bucle while que daba como condicion un True para seguir funcionando
                            
                            else: # Else que dicta que si no se inserto el valor de 0 o 1, hace lo siguiente
                                print("Inserte una opcion valida") 
                                print("") # Espacio de tolerancia a la hora de imprimir el programa
                                continue  # saltar a la siguiente iteración del bucle
                    continue # saltar a la siguiente iteración del bucle

        except Exception as e: # Atrapa cualquier excepcion
                print(f"Error insertarProducto() :{e.args}") # Muestra en consola el error que ocurrio
                return False # Regresa False si ocurrio un error en el metodo

    def buscarProducto(self) -> bool: # Metodo para buscar productos
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("productos.csv", "r") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,

                sku_buscar = input("Ingrese el SKU del producto que desea buscar: ") # Pide al usuario el SKU a buscar
                encontrado = False # Variable para indicar si se encontró el producto o no

                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    if row['sku'] == sku_buscar: # Compara el SKU buscado con el SKU de la fila actual
                        print(f"Registro encontrado: {row}") # Imprime la fila encontrada
                        encontrado = True # Marca el producto como encontrado
                        break # Termina el bucle ya que se encontró el producto

                if not encontrado: # If por si no exista el sku
                    print("Producto no encontrado") # Imprime el mensaje si el producto no se encontró

            return True # Retorna True si el método se ejecutó correctamente

        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error buscarProducto(): {e.args}") # Muestra en consola el error que ocurrio
            return False  # Regresa False si ocurrio un error en el metodo

    def borrarProducto(self) -> bool: # Metodo para borrar un producto
            with open('productos.csv', 'r', newline='') as archivo, open('temp.csv', 'w', newline='') as archivo_temp: # abre dos archivos en modo de lectura y escritura respectivamente, utilizando la función open() de Python.
                lector_csv = csv.reader(archivo)  # se crea un objeto csv.reader que permite iterar por cada fila del archivo CSV y se asigna a la variable lector_csv
                escritor_csv = csv.writer(archivo_temp)  # También se crea un objeto csv.writer que permite escribir en el archivo temporal y se asigna a la variable escritor_csv

                sku = input("Inserte SKU: ") # Input para borrar el sku correspondiente
                for fila in lector_csv: # Recorre todos los registros de "productos.csv"
                    if fila[0] != sku: # si la fila no contiene el producto que deseas borrar, escribirla en el archivo de salida
                        escritor_csv.writerow(fila) # Utiliza el objeto "writer" para poder sobreescribir la fila de informacion del csv con el metodo de la libreria CSV "writerow()"
                    

            import os # Importa el modulo os
            os.replace('temp.csv', 'productos.csv') # reemplazar el archivo original con el archivo de salida

            print("") # Espacio de tolerancia a la hora de imprimir el programa
            print("Producto borrado con exito")
            print("") # Espacio de tolerancia a la hora de imprimir el programa
            
    def actualizarProducto(self)-> bool: # Metodo para actualizar un producto
        sku = input("Ingresa el valor del SKU a reemplazar: ") # Input para borrar el sku correspondiente
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
                sku = input("El SKU ingresado no existe en el archivo, por favor ingresa un SKU válido: ") # le imprime al usuario el mensaje presentado y le pide que inserte nuevamente un sku hasta que haya una coincidencia entre el valor dado y el CSV
        
        sku_nuevo = input("Ingresa el nuevo valor del SKU: ") # input para preguntar el nuevo valor del sku
        while True: # Bucle que lo que hace es buscar el valor "sku" en la tabla CSV
            if sku_nuevo == sku: # Condicion que dicta que si sku_nuevo es igual a sku
                break # Pasar al siguiente paso del codigo, rompiendo con el if
            else: # en caso de que sku_nuevo no es igual a sku
                encontrado = False # Se utiliza para determinar si el SKU ingresado por el usuario existe en el archivo CSV
                with open("productos.csv") as file: # Abre el archivo para poder leer filas de informacion
                    reader = csv.DictReader(file) # se crea un objeto con la valriable "reader"
                    for row in reader:  # Se encarga de buscar un sku en el CSV
                        if row['sku'] == sku_nuevo: # condicion de si el valor de la columna "sku" es igual a el valor de la variable sku_nuevo dado por el usuario pasa lo siguiente
                            encontrado = True # la variable "encontrado" cambia de valor a True, dando como encontrado un sku en el csv
                            break # break con la funcion de terminar con el if y pasar al siguiente paso
                if encontrado: # condicion de que si encontrado esta en True
                    sku_nuevo = input("El SKU ingresado ya existe en el archivo, por favor ingresa un SKU válido: ") # le imprime al usuario el mensaje presentado y le pide que inserte nuevamente un sku hasta que NO haya una coincidencia entre el valor dado y el CSV
                else: # en caso de que no exista el sku dado en la tabla del CSV
                    break # break con la funcion de terminar con el if y pasar al siguiente paso
        
        nombre_nuevo = input("Ingresa el nuevo nombre del producto: ") # input para preguntar el nuevo nombre del producto
        
        unidad_nueva = None # asignacion del valor none a la variable unidad_nueva
        while unidad_nueva not in ['0', '1']: # Bucle que dicta que mientras unidad_nueva no tenga los valores 0 o 1, se repita
            print("Ingresa el nuevo tipo de unidad") # imprime el mensaje "Ingresa el nuevo tipo de unidad" al usuario
            print("0.- Pieza") # imprime la primera opcion si inserta como valor 0
            print("1.- Paquete") # imprime la segunda opcion si inserta como valor 1
            unidad_nueva = input("") # input para ingresar la seleccion de la unidad
        
        with open("productos.csv", "r") as f: # Abre el archivo para poder leer filas de informacion
            reader = csv.reader(f) # se crea un objeto con la variable "reader"
            rows = list(reader) # se crea un objeto con la variable "rows" para leer las columnas del CSV
        
        with open("productos.csv", "w", newline='') as f: # Abre el archivo para poder sobreescribir filas de informacion
            writer = csv.writer(f) # se crea un objeto con la variable "writer" para poder sobreescribir filas de informacion
            for row in rows: #Se encarga de leer las columnas del CSV
                if row[0] == sku: # Condicion que dicta que entre los valores que hay en la columna del CSV numero 0 se encuentra el valor del sku
                    row[0] = sku_nuevo # Asignacion de valor a la columna 0 en la fila correspondiente del CSV
                    row[1] = nombre_nuevo # Asignacion de valor a la columna 1 en la fila correspondiente del CSV
                    if unidad_nueva == '0': # Condicion que dicta que si unidad_nueva es igual a '0'
                        row[2] = 'pieza' # Asignacion de valor a la columna 2 en la fila correspondiente del CSV
                    else: # En caso contrario a la condicion
                        row[2] = 'paquete' # Asignacion de valor a la columna 2 en la fila correspondiente del CSV
                writer.writerow(row) # Finalmente sobreescribe con este metodo la fila de informacion del producto
        
        print("El producto fue actualizado de forma exitosa") # Notifica con un print de que el producto fue actualizado de forma exitosa
                                
productos = Productos() # Crea un objeto de la clase Productos

# Metodos que estan presentes en el programa

#productos.insertarProducto() #Llama al metodo insertarProductos()
#productos.listarProductos() # Llama al metodo listarProductos()
#productos.borrarProducto() # Llamar al método borrarProductos() 
#productos.actualizarProducto() # Llamar al método actualizarProductos() 
#productos.buscarProducto() # Llama al metodo buscarProductos()
