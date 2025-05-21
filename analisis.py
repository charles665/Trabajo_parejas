import csv
import random
import math
import os
import pandas as pd
#modulo para la gestion de proyectos
class Gestor_proyecto:
    def __init__(self, archivo = 'proyecto.csv'): #para la gestion de proyectos
        self.archivo = archivo
        self.campos = ['id', 'nombre', 'angulo', 'resultado'] #nombres de los campos
        if not os.path.isfile(self.archivo): #si el archivo no existe, lo crea
            with open(self.archivo, 'w', newline='') as f: #para abrir el archivo
                #se crea el archivo
                writer = csv.DictWriter(f, fieldnames=self.campos)
                writer.writeheader()
    
    def registrar_proyecto(self, nombre, angulo, resultado): #para registrar un proyecto
        try:
            longitud = float(longitud)
        except ValueError:
            raise ValueError("La longitud debe ser un número.") #para comprobar que la longitud es un numero
        
        angulo = random.uniform(30, 60) #angulo aleatorio
        resultado = math.tan(math.radians(angulo)) * longitud #resultado de la tangente
        
        
    def ver_proyectos(self, numero): #para ver los proyectos
        df = self.cargar_todos() #para cargar todos los proyectos
        try:
            return df.iloc[int(numero)].to_dict() #para ver los proyectos
        except (ValueError, IndexError):
            raise ValueError("Número de proyecto no válido.")
