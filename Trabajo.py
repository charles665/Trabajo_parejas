import csv
import random
import math
import pandas as pd
import os

# Archivo de almacenamiento
archivo_csv = 'registros.csv'

# Función para registrar una nueva entrada
def registrar_entrada(etiqueta, valor_base):
    parametro = ""
    resultado = ""

    fila = {
        'etiqueta': etiqueta,
        'parametro': parametro,
        'valor_base': valor_base,
        'resultado': round(resultado, 2)
    }

    # Verificar si ya existe el archivo
    archivo_existe = os.path.isfile(archivo_csv)

    with open(archivo_csv, 'a', newline='') as f:
        escritor = csv.DictWriter(f, fieldnames=fila.keys())
        if not archivo_existe:
            escritor.writeheader()
        escritor.writerow(fila)

# Función para cargar y mostrar los registros con pandas
def cargar_registros():
    if os.path.isfile(archivo_csv):
        df = pd.read_csv(archivo_csv)
        print(df)
    else:
        print("No hay registros disponibles.")

# Ejemplo de uso
registrar_entrada("Registro A", 7.5)
registrar_entrada("Registro B", 10.0)

cargar_registros()

