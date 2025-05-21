import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
import csv
import random
import math
import pandas as pd
import os
import analisis
class Gestor_proyecto:
    def __init__(self, archivo='proyecto.csv'):
        self.archivo = archivo
        self.campos = ['id', 'nombre', 'angulo', 'resultado']
        if not os.path.isfile(self.archivo):
            with open(self.archivo, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.campos)
                writer.writeheader()
    
    def registrar_proyecto(self, nombre, longitud):
        try:
            longitud = float(longitud)
        except ValueError:
            raise ValueError("La longitud debe ser un número.")
        
        angulo = random.uniform(30, 60)
        resultado = math.tan(math.radians(angulo)) * longitud

        # Cargar y generar ID
        proyectos = self.cargar_todos()
        nuevo_id = len(proyectos)

        with open(self.archivo, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.campos)
            writer.writerow({
                'id': nuevo_id,
                'nombre': nombre,
                'angulo': round(angulo, 2),
                'resultado': round(resultado, 2),
                'Longitud': longitud,
            })

    def cargar_todos(self):
        return pd.read_csv(self.archivo)

    def ver_proyectos(self, numero):
        df = self.cargar_todos()
        try:
            return df.iloc[int(numero)].to_dict()
        except (ValueError, IndexError):
            raise ValueError("Número de proyecto no válido.")
        
    def eliminar_proyecto(self, numero):
        df = self.cargar_todos()
        try:
            df = df.drop(int(numero))
            df.to_csv(self.archivo, index=False)
        except (ValueError, IndexError):
            raise ValueError("Número de proyecto no válido.")
        
    def actualizar_proyecto(self, dataframe):
        if isinstance(dataframe, pd.DataFrame):
            dataframe.to_csv(self.archivo, index=False)
        else:
            raise ValueError("El argumento debe ser un DataFrame de pandas.")
