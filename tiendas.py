import csv  # Librería para abrir, leer y escribir archivos CSV


class Tiendas:  # Clase Tiendas

    def __init__(self):  # Construcctor de la clase Tiendas
        pass  # Inicializa el objeto Tiendas

    def listarTiendas(self) -> bool:  # Metodo para listar las tiendas
        # TODO programar el método listarTiendas()
        return False  # Regresa False si ocurrio un error en el metodo

    def insertarTiendas(self) -> bool:  # Metodo para insertar una tienda
        # TODO programar el método insertarTienda()
        return False  # Regresa False si ocurrio un error en el metodo

 def buscarTiendas(self) -> bool: # Metodo para buscar tiendas
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("tiendas.csv", "r") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,

                id_buscar = input("Ingrese el id de la tienda que desea buscar: ") # Pide al usuario el id a buscar
                encontrado = False # Variable para indicar si se encontró la tienda o no

                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    if row['ID'] == id_buscar: # Compara el id buscando
                        print(f"Registro encontrado: {row}") # Imprime la fila encontrada
                        encontrado = True # Marca la tienda como encontrada
                        break # Termina el bucle ya que se encontró el producto

                if not encontrado: # If por si no exista el sku
                    print("Tienda no encontrada") # Imprime el mensaje si la tienda no se encontró

            return True # Retorna True si el método se ejecutó correctamente

        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error buscarTienda(): {e.args}") # Muestra en consola el error que ocurrio
            return False  # Regresa False si ocurrio un error en el metodo


    def borrarTiendas(self, direccion: str) -> bool:  # Metodo para borrar tiendas por direccion
        with open('tiendas.csv', 'r', newline='') as archivo, open('temp.csv', 'w', newline='') as archivo_temp:
            # abre dos archivos en modo de lectura y escritura respectivamente, utilizando la función open() de Python.

            lector_csv = csv.reader(archivo) 
            # se crea un objeto csv.reader que permite iterar por cada fila del archivo CSV y se asigna a la variable lector_csv

            escritor_csv = csv.writer(archivo_temp) 
            # También se crea un objeto csv.writer que permite escribir en el archivo temporal y se asigna a la variable escritor_csv

            for fila in lector_csv:
                # si la fila no contiene la tienda que deseas borrar, escribirla en el archivo de salida
                if fila[1] != direccion:
                    escritor_csv.writerow(fila)

        # reemplazar el archivo original con el archivo de salida
        import os
        os.replace('temp.csv', 'tiendas.csv')

    def actualizarTiendas(self) -> bool:  # Metodo para actualizar los datos de un tienda
        # TODO programar el método actualizarTienda()
        return False  # Regresa False si ocurrio un error en el metodo

    tiendas = Tiendas()
tiendas.borrarTiendas("Calle 123")
tiendas.buscarTiendas() # Llama al metodo buscarTiendas()
