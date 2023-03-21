import csv  # Librería para abrir, leer y escribir archivos CSV


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

    def insertarProductos(self): # Metodo para insertar un producto
        try:
            with open('productos.csv', 'a', newline='') as file:
        
                # Crear un objeto writer
                writer = csv.writer(file)
                # Agregar la fila de información
                sku = input("Inserte SKU: ")
                nombre = input("Inserte Nombre: ")
                while True:
                    print("Inserte que tipo de unidad quiere")
                    print("")
                    print("0.- Pieza")
                    print("1.- Paquete")
                    valorunidad = input("")
                    if valorunidad == "0":
                        unidad = "pieza"
                        fila = [sku, nombre, unidad]
                        writer.writerow(fila)
                        print("El producto a sido añadido correctamente")
                        return False
                    elif valorunidad == "1":
                        unidad = "paquete"
                        fila = [sku, nombre, unidad]
                        writer.writerow(fila)
                        print("El producto a sido añadido correctamente")
                        return False
                    else:
                        print("Insete una opcion valida")
                        print("")
                
        except Exception as e: # Atrapa cualquier excepcion
                print(f"Error insertarProducto() :{e.args}") # Muestra en consola el error que ocurrio
                return False # Regresa False si ocurrio un error en el metodo

    def buscarProductos(self): # Metodo para buscar un producto
        # TODO programar el método buscarProducto()
        print("buscarProductos") # Imprime buscarProductos
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

  # Metodo para borrar un producto
       def borrarProducto(self, productos_csv, sku): 
        # define una función llamada borrar_producto que recibe el nombre del archivo, y el sku que es por el cual se va a borrar el producto 

        with open(productos_csv, 'r', newline='') as archivo, open('temp.csv', 'w', newline='') as archivo_temp:
            # abre dos archivos en modo de lectura y escritura respectivamente, utilizando la función open() de Python.

            lector_csv = csv.reader(archivo) 
            # se crea un objeto csv.reader que permite iterar por cada fila del archivo CSV y se asigna a la variable lector_csv

            escritor_csv = csv.writer(archivo_temp) 
            # También se crea un objeto csv.writer que permite escribir en el archivo temporal y se asigna a la variable escritor_csv

            for fila in lector_csv:
                # si la fila no contiene el producto que deseas borrar, escribirla en el archivo de salida
                if fila[0] != sku:
                    escritor_csv.writerow(fila)

        # reemplazar el archivo original con el archivo de salida
        import os
        os.replace('temp.csv', productos_csv)

    def actualizarProductos(self) -> bool: # Metodo para actualizar un producto
        # TODO programar el método actualizarProducto()
        return False # Regresa False si ocurrio un error en el metodo

productos = Productos() # Crea un objeto de la clase Productos
productos.listarProductos() # Llama al metodo listarProductos()
productos.insertarProductos() #Llama al metodo insertarProductos()
productos.buscarProductos() # Llama al metodo buscarProductos()
productos.borrarProductos("productos.csv", "SKU123") # Llamar al método borrarProductos() con los parámetros necesarios
