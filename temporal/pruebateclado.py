import csv
from prettytable import PrettyTable

# Abrir el archivo CSV
with open('archivo.csv', 'r') as archivo_csv:
    # Crear un objeto lector CSV
    reader = csv.reader(archivo_csv)

    # Crear una tabla de datos
    tabla = PrettyTable()

    # Añadir las columnas a la tabla
    tabla.field
