from productos import Productos # Importa el modulo Productos

#TODO importar Despensa

class MainProductos(): # Clase principal

    def __init__(self) -> None: # Constructor de la clase Main
        pass # inicializa el objeto Main

    def menuProductos(self): # Metodo que muestra el menu del sistema
        productos = Productos() # Crea un objeto de la clase Prodcutos
        while True: # Bucle infinito para mostrar las opciones del sistema
            print("0.- Listar productos") # Opcion para listar los prodcutos
            print("1.- Insertar producto") # Opcion para insertar un nuevo producto
            print("2.- Buscar producto por SKU") # Opcion para buscar productos por SKU
            print("3.- Actualizar producto") # Opcion para actualizar un producto
            print("4.- Borrar producto") # Opcion para borrar un producto
            print("s.- Salir") # Opcion para salir del sistema
            print("") # Espacio de tolerancia
            opcion = input("Seleccione una opcion: ") # Solicita al usuario que seleccione una opcion del menu
            if opcion == "0": # Valida si la opcion elegida es el 0
                productos.listarProductos() # Llama al metodo listarProductos a traves del objeto productos
            elif opcion == "1": # Valida si la opcion elegida es el 1              
                productos.insertarProducto() # Llama al metodo insertarProductos a traves del objeto productos
            elif opcion == "2": # Valida si la opcion elegida es el 2            
                productos.buscarProducto() # Llama al metodo buscarProductos a traves del objeto productos
            elif opcion == "3": # Valida si la opcion elegida es el 3
                productos.actualizarProducto() # Llama al metodo actualizarProductos a traves del objeto productos
            elif opcion == "4": # Valida si la opcion elegida es el 4
                productos.borrarProducto() #Llama al metodo borrarProductos a traves del objeto productos 
            elif opcion == "s": # Valida si la opcion elegida es el 5
                print("")
                print("Saliendo del programa")
                print("")
                return False
            elif opcion == "S": # Valida si la opcion elegida es el 5
                print("")
                print("Saliendo del programa")
                print("")
                return False

            # TODO rediseñar el menu para agregar los submenus necesarios


if __name__ == "__main__": # Define el modulo principal
    principalproductos = MainProductos() # Crea un objeto de la clase Main
    principalproductos.menuProductos() # Llama al metodo menu a traves del objeto principal