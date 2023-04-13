from tiendas import Tiendas # Importa el modulo Tiendas
from productos import Productos # Importa el modulo Productos
from despensa import Despensa # Importa el modulo Despensas
from rastreador import Rastreador # Importa el modulo Rastreador
from maintiendas import MainTiendas # Importa el modulo MainTiendas
from mainproductos import MainProductos # Importa el modulo MainProductos
from maindespensa import MainDespensa # Importa el modulo MainDespensa
from mainrastreador import MainRastreador # Importa el modulo MainRastreador

#TODO importar Despensa

class Main(): # Clase principal

    def __init__(self) -> None: # Constructor de la clase Main
        pass # inicializa el objeto Main

    def menu(self): # Metodo que muestra el menu del sistema
        principaltiendas = MainTiendas() # Crea un objeto de la clase Main Tiendas
        principalproductos = MainProductos() # Crea un objeto de la clase Main Productos
        principaldespensa = MainDespensa() # Crea un objeto de la clase Main Despensa
        principalrastreador = MainRastreador() # Crea un objeto de la clase Main Rastreador
        
        while True: # Bucle infinito para mostrar las opciones del sistema
            print("0.- Ingresar al menu de Tiendas") # Menciona la opcion para entrar al menu de Tiendas
            print("1.- Ingresar al menu de Productos") # Menciona la opcion para entrar al menu de Producots
            print("2.- Ingresar al menu de Despensa") # Menciona la opcion para entrar al menu de Despensa
            print("3.- Ingresar al menu de Rastrear") # Menciona la opcion para entrar al menu de Rastrear
            
            print("s.- Salir") # Opcion para salir del sistema
            print("") # Espacio de tolerancia
            opcion = input("Seleccione una opcion: ") # Solicita al usuario que seleccione una opcion del menu
            if opcion == "0": # Valida si la opcion elegida es el 0
                principaltiendas.menuTiendas() # Llama al metodo menu a traves del objeto principal
            elif opcion == "1": # Valida si la opcion elegida es el 1              
                principalproductos.menuProductos() # Llama al metodo menu a traves del objeto principal
            elif opcion == "2": # Valida si la opcion elegida es el 2              
                principaldespensa.menuDespensa() # Llama al metodo menu a traves del objeto principal
            elif opcion == "3": # Valida si la opcion elegida es el 3              
                principalrastreador.menuRastreador() # Llama al metodo menu a traves del objeto principal
            elif opcion == "s": # Valida si la opcion elegida es el s
                print("") # Espacio de tolerancia
                print("Saliendo del programa") # Notificacion de salida de programa
                print("") # Espacio de tolerancia
                return False # Regresa un "False" para terminar con el bucle
            elif opcion == "S": # Valida si la opcion elegida es el S
                print("") # Espacio de tolerancia
                print("Saliendo del programa") # Notificacion de salida de programa
                print("") # Espacio de tolerancia
                return False # Regresa un "False" para terminar con el bucle

            # TODO rediseñar el menu para agregar los submenus necesarios


if __name__ == "__main__": # Define el modulo principal
    principal = Main() # Crea un objeto de la clase Main
    principal.menu() # Llama al metodo menu a traves del objeto principal
