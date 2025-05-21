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
    
