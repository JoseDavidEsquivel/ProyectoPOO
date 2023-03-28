import csv  # Librería para abrir, leer y escribir archivos CSV


class Despensa:  # Clase Despensa

    def __init__(self): # Constructor de la clase
        pass # Inicializa el objeto

    def listarDespensa(self) -> bool: # Metodo para listarDespensa()
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("despensa.csv", "r") as file: # Abre el archivo para tener acceso a los 
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,
                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    print(f"Registro: {row}") # imprime los datos del registro como un diccionario
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error listarCompras() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo

    def insertarDespensa(self) -> bool: # Metodo para insertarDespesa()
        id_compra = input("Ingresa el numero de compra: ")
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
        
        fecha_dia= input("Ingrese el numero de dia de la compra: ")
        fecha_mes= input("Ingrese el numero del mes de la compra: ")
        fecha_año= input("Ingrese el año de la compra: ")

        fecha = fecha_dia+"/"+fecha_mes+"/"+fecha_año
        precio_unitario = float(input("Inserte el precio unitario (si es decimal, porfavor de usar punto.): ")) # Input para recibir el nombre para agregarlo
        cantidad = int(input("Inserte la cantidad de productos comprados: "))
        precio_total = precio_unitario*cantidad

        fila = [id_compra, id_tienda, sku, fecha, precio_unitario, cantidad, precio_total] # La variable "fila" es asignada con los valores anteriormente dados de "sku", "nombre", "unidad"
        with open('despensa.csv', 'a', newline='') as file: # Abre el archivo para poder agregar filas de informacion
            writer = csv.writer(file) # Crear un objeto writer
            writer.writerow(fila) # Utiliza el objeto "writer" para poder sobreescribir la fila de informacion del csv con el metodo de la libreria CSV "writerow()"
            print("La compra ha sido añadida correctamente") # Le informa al usuario que el producto a sido añadido de forma exitosa
            print("") # Espacio de tolerancia a la hora de imprimir el programa




    def buscarDespensa(self,id:int) -> None: # Metodo para buscarDespesa()
        # TODO programar el método buscarDespensa()
        # buscar despensa por id
        return False # Regresa False si ocurrio un error en el metodo

    def borrarDespensa(self,id:int) -> None: # Metodo para borrarDespensa()
        # TODO programar el método borrarDespensa()
        return False # Regresa False si ocurrio un error en el metodo

    def actualizarDespensa(self) -> None: # Metodo para actualizarDespensa()
        # TODO programar el método actualizarDespensa()
        return False # Regresa False si ocurrio un error en el metodo

    def valorMinimoProducto(self,sku:str) -> None: # Metodo para mostrar el valor minimo de un producto
        # TODO programar el método valorMinimoProducto()
        return False # Regresa False si ocurrio un error en el metodo

    def valorMaximoProducto(self,sku:str) -> None: # Metodo para mostrar el valor minimo de un producto
        # TODO programar el método valorMinimoProducto()
        return False # Regresa False si ocurrio un error en el metodo

despensa = Despensa()
despensa.insertarDespensa()
