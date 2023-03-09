import csv

class Productos:
    def insertarProducto():
        with open('archivo.csv', mode='a') as file:
            sku = input("Sku: ")
            nombre = input("nombre: ")
            unidad = input("unidad: ")
            writer = csv.writer(file)
            nueva_fila = [sku, nombre, unidad]  # reemplaza con los valores que desees agregar
            writer.writerow(nueva_fila)
        
    # el archivo se cierra automáticamente al salir del bloque with
    def actualizarProducto():


        with open('archivo.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            filas = list(reader)
        
        fila_a_sobrescribir = 1  # el índice de la fila que deseamos sobrescribir
        fila_nueva = ['nuevo_valor1', 'nuevo_valor2', 'nuevo_valor3']  # la lista de valores para la fila nueva
        filas[fila_a_sobrescribir] = fila_nueva  # sobrescribir la fila antigua con la nueva fila

        with open('archivo.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(filas)

producto = Productos()
producto.actualizarProducto

# el archivo se cierra automáticamente al salir del bloque with
