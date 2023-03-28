import csv  # Librería para abrir, leer y escribir archivos CSV


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
        # TODO programar el método insertarDespensa()
        return False # Regresa False si ocurrio un error en el metodo

  def buscarDespensa(self) -> bool: # Metodo para buscar despensa
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("despensa.csv", "r") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,

                fecha_buscar = input("Ingrese la fecha de la compra que desea buscar: ") # Pide al usuario la fecha para la busqueda 
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
    
despensa = Despensa() # Crea un objeto de la clase despensa
despensa.listarDespensa() # Llama al metodo listarDespensa()
despensa.buscarDespensa() # Llama al metodo buscarDespensa()
