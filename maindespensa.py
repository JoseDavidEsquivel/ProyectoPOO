from despensa import Despensa # Importa el modulo Despensa
from despensa import obtener_ultimo_id_compra 

#TODO importar Despensa

class MainDespensa(): # Clase principal

    def __init__(self) -> None: # Constructor de la clase Main
        pass # inicializa el objeto Main

    def menuDespensa(self): # Metodo que muestra el menu del sistema
        despensa = Despensa() # Crea un objeto de la clase Despensa
        while True: # Bucle infinito para mostrar las opciones del sistema
            print("0.- Listar despensa") # Opcion para listar los despensa
            print("1.- Insertar despensa") # Opcion para insertar una nueva despensa
            print("2.- Buscar despensa por Fecha") # Opcion para buscar despensa por fecha
            print("3.- Actualizar despensa") # Opcion para actualizar una despensa
            print("4.- Borrar despensa") # Opcion para borrar una despensa
            print("5.- Valor Minimo de un Producto") # Opcion para valor minimo de un producto
            print("6.- Valor Maximo de un Producto") # Opcion para valor maximo de un producto
            print("s.- Salir") # Opcion para salir del sistema
            print("") # Espacio de tolerancia
            opcion = input("Seleccione una opcion: ") # Solicita al usuario que seleccione una opcion del menu
            if opcion == "0": # Valida si la opcion elegida es el 0
                despensa.listarDespensa() # Llama al metodo listarDespensa a traves del objeto Despensa
            elif opcion == "1": # Valida si la opcion elegida es el 1              
                obtener_ultimo_id_compra()
                despensa.insertarDespensa() # Llama al metodo insertarDespensa a traves del objeto Despensa
            elif opcion == "2": # Valida si la opcion elegida es el 2            
                despensa.buscarDespensa() # Llama al metodo buscarDespensa a traves del objeto Despensa
            elif opcion == "3": # Valida si la opcion elegida es el 3
                obtener_ultimo_id_compra()
                despensa.actualizarDespensa() # Llama al metodo actualizarDespensa a traves del objeto Despensa
            elif opcion == "4": # Valida si la opcion elegida es el 4
                despensa.borrarDespensa() #Llama al metodo borrarDespensa a traves del objeto Despensa
            elif opcion == "5": # Valida si la opcion elegida es el 5
                despensa.valorMinimoProducto() #Llama al metodo valorMinimoProducto a traves del objeto Despensa
            elif opcion == "6": # Valida si la opcion elegida es el 6
                despensa.valorMaximoProducto() #Llama al metodo valorMaximoProducto a traves del objeto Despensa
            elif opcion == "s": # Valida si la opcion elegida es el s
                print("") # Espacio de tolerancia
                print("Saliendo del menu") # Avisa que esta saliendo del menu
                print("") # Espacio de tolerancia
                return False
            elif opcion == "S": # Valida si la opcion elegida es el S
                print("") # Espacio de tolerancia
                print("Saliendo del menu") # Avisa que esta saliendo del menu
                print("") # Espacio de tolerancia
                return False

            # TODO rediseñar el menu para agregar los submenus necesarios


if __name__ == "__main__": # Define el modulo principal
    principalDespensa = MainDespensa() # Crea un objeto de la clase Main
    principalDespensa.menuDespensa() # Llama al metodo menu a traves del objeto principal
