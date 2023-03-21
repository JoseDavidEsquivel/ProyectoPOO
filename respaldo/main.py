from tiendas import Tiendas # Importa el modulo Tiendas
from productos import Productos # Importa el modulo Productos
from maintiendas import MainTiendas # Importa el modulo MainTiendas
from mainproductos import MainProductos # Importa el modulo MainProductos

#TODO importar Despensa

class Main(): # Clase principal

    def __init__(self) -> None: # Constructor de la clase Main
        pass # inicializa el objeto Main

    def menu(self): # Metodo que muestra el menu del sistema
        principaltiendas = MainTiendas() # Crea un objeto de la clase Main
        principalproductos = MainProductos() # Crea un objeto de la clase Main
        
        while True: # Bucle infinito para mostrar las opciones del sistema
            print("0.- Ingresar al menu de Tiendas") # Opcion para listar los prodcutos
            print("1.- Ingresar al menu de Productos") # Opcion para insertar un nuevo producto
            
            print("s.- Salir") # Opcion para salir del sistema
            print("") # Espacio de tolerancia
            opcion = input("Seleccione una opcion: ") # Solicita al usuario que seleccione una opcion del menu
            if opcion == "0": # Valida si la opcion elegida es el 0
                principaltiendas.menuTiendas() # Llama al metodo menu a traves del objeto principal
            elif opcion == "1": # Valida si la opcion elegida es el 1              
                principalproductos.menuProductos() # Llama al metodo menu a traves del objeto principal
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
    principal = Main() # Crea un objeto de la clase Main
    principal.menu() # Llama al metodo menu a traves del objeto principal