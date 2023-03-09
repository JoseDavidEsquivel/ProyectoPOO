import csv

with open('archivo.csv', mode='a') as file:

    sku = input("Sku: ")
    nombre = input("nombre: ")
    unidad = input("unidad: ")
    writer = csv.writer(file)
    nueva_fila = [sku, nombre, unidad]  # reemplaza con los valores que desees agregar
    writer.writerow(nueva_fila)
    