import csv

print("")
class Productos:

    def listarProductos(self)-> bool:
        print("")
        try:
            with open('productos.csv', 'r') as file:
                reader = csv.reader(file)
                
                # Itera sobre cada fila del archivo CSV e imprime cada celda
                for row in reader:
                    for cell in row:
                        print(cell, end=' | ')
                    print()
            print("")
            return False
        except Exception as e: # Atrapa cualquier excepcion
                print(f"Error listarProductos() :{e.args}") # Muestra en consola el error que ocurrio
                return False # Regresa False si ocurrio un error en el metodo
        

    def insertarProducto(self)-> bool:
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

    def buscarProducto(self): # Metodo para buscar un producto
        # TODO programar el método buscarProducto()
        print("buscarProductos") # Imprime buscarProductos
        return False # Regresa False si ocurrio un error en el metodo

    def borrarProducto(self) -> bool: # Metodo para borrar un producto
            with open('productos.csv', 'r', newline='') as archivo, open('temp.csv', 'w', newline='') as archivo_temp: # abre dos archivos en modo de lectura y escritura respectivamente, utilizando la función open() de Python.

                lector_csv = csv.reader(archivo)  # se crea un objeto csv.reader que permite iterar por cada fila del archivo CSV y se asigna a la variable lector_csv

                escritor_csv = csv.writer(archivo_temp)  # También se crea un objeto csv.writer que permite escribir en el archivo temporal y se asigna a la variable escritor_csv
                sku = input("Inserte SKU: ") # Input para borrar el sku correspondiente
                for fila in lector_csv: 
                    if fila[0] != sku: # si la fila no contiene el producto que deseas borrar, escribirla en el archivo de salida
                        escritor_csv.writerow(fila)
                    

            import os
            os.replace('temp.csv', 'productos.csv') # reemplazar el archivo original con el archivo de salida

            print("")
            print("Producto borrado con exito")
            print("")

    def actualizarProducto(self) -> bool: # Metodo para actualizar un producto
        # TODO programar el método actualizarProducto()
        print("borrarProductos")
        return False # Regresa False si ocurrio un error en el metodo


productos = Productos()
