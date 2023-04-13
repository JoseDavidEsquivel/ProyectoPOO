from rastreador import Rastreador # Importa el modulo Rastreador

#TODO importar Despensa

class MainRastreador(): # Clase principal

    def __init__(self) -> None: # Constructor de la clase Main
        pass # inicializa el objeto Main

    def menuRastreador(self): # Metodo que muestra el menu del sistema
        rastreador = Rastreador() # Crea un objeto de la clase Rastreador
        while True: # Bucle infinito para mostrar las opciones del sistema
            print("0.- Rastrear Tienda") # Opcion para rastrear tiendas
            print("1.- Comparar distancia entre tiendas") # Opcion para comparar distancias de tiendas
            print("2.- Asignar nuevas coordenadas de usuario") # Opcion para asignar coordenadas de usuario
            print("3.- Mostrar las coordenadas de usuario preestablecidas") # Opcion para mostrar las coordenadas del usuario preestablecidas
            print("4.- Obtener coordenadas de una tienda por medio de ID") # Opcion para obtener las coordenadas de una tienda por medio de ID
            print("s.- Salir del Menu") # Opcion para salir del sistema
            print("") # Espacio de tolerancia
            opcion = input("Seleccione una opcion: ") # Solicita al usuario que seleccione una opcion del menu
            if opcion == "0": # Valida si la opcion elegida es el 0
                rastreador.rastrearTienda() # Llama al metodo rastrearTienda a traves del objeto rastreador
            elif opcion == "1": # Valida si la opcion elegida es el 1              
                rastreador.compararTiendas() # Llama al metodo compararTiendas a traves del objeto rastreador
            elif opcion == "2": # Valida si la opcion elegida es el 2            
                rastreador.asignarCoordenadas() # Llama al metodo asignarCoordenadas a traves del objeto rastreador
            elif opcion == "3": # Valida si la opcion elegida es el 3
                rastreador.leerCoordenadas() # Llama al metodo leerCoordenadas a traves del objeto rastreador
            elif opcion == "4": # Valida si la opcion elegida es el 4
                rastreador.obtenerCoordenadas() #Llama al metodo obtenerCoordenadas a traves del objeto rastreador
            elif opcion == "s": # Valida si la opcion elegida es el 5
                print("") # Espacio de tolerancia
                print("Saliendo del menu") # Avisa que esta saliendo del menu
                print("") # Espacio de tolerancia
                return False
            elif opcion == "S": # Valida si la opcion elegida es el 5
                print("") # Espacio de tolerancia
                print("Saliendo del menu") # Avisa que esta saliendo del menu
                print("") # Espacio de tolerancia
                return False

            # TODO rediseñar el menu para agregar los submenus necesarios


if __name__ == "__main__": # Define el modulo principal
    principalrastreador = MainRastreador() # Crea un objeto de la clase Main
    principalrastreador.menuRastreador() # Llama al metodo menu a traves del objeto principal
    
