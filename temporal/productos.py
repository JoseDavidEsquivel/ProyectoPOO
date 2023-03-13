import csv
import keyboard

print("")
class Productos:

    def listarProductos(self)-> bool:

        try:
            with open('productos.csv', 'r') as file:
                reader = csv.reader(file)

                # Itera sobre cada fila del archivo CSV e imprime cada celda
                for row in reader:
                    for cell in row:
                        print(cell, end=' | ')
                    print()
            return False
        except Exception as e: # Atrapa cualquier excepcion
                print(f"Error listarProductos() :{e.args}") # Muestra en consola el error que ocurrio
                return False # Regresa False si ocurrio un error en el metodo

    def insertarProducto(self)-> bool:
        try:
            with open('productos.csv', mode='a', newline='') as file:
        
                # Crear un objeto writer
                writer = csv.writer(file)
                
                # Agregar la fila de información
                sku = input("Inserte SKU: ")
                nombre = input("Inserte Nombre: ")
                unidad = input("Inserte Unidad: ")
                fila = [sku, nombre, unidad]
                writer.writerow(fila)
        except Exception as e: # Atrapa cualquier excepcion
                print(f"Error insertarProducto() :{e.args}") # Muestra en consola el error que ocurrio
                return False # Regresa False si ocurrio un error en el metodo

    def buscarProducto(self): # Metodo para buscar un producto
        # TODO programar el método buscarProducto()
        print("buscarProductos") # Imprime buscarProductos
        return False # Regresa False si ocurrio un error en el metodo

    def borrarProducto(self) -> bool: # Metodo para borrar un producto
        # TODO programar el método borrarProducto()
        print("borrarProductos") #Imprime borrarProductos
        return False # Regresa False si ocurrio un error en el metodo

    def actualizarProducto(self) -> bool: # Metodo para actualizar un producto
        # TODO programar el método actualizarProducto()
        print("borrarProductos")
        return False # Regresa False si ocurrio un error en el metodo





