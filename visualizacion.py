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

## Van las funciones
gestor = analisis.Gestor_proyecto()

def mostrar_registrar():
    ventana1 = tk.Toplevel(ventana)
    ventana1.title('Registro de proyectos')
    ventana1.geometry('400x300')

    frame_registro = tk.Frame(ventana1, bg="white")
    frame_registro.pack(pady=20)


    tk.Label(frame_registro, text="Nombre del proyecto:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(frame_registro)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)


    tk.Label(frame_registro, text="Longitud:").grid(row=1, column=0, padx=5, pady=5)
    entry_longitud = tk.Entry(frame_registro)
    entry_longitud.grid(row=1, column=1, padx=5, pady=5)


def oe():
    mensaje = tk.Label(ventana, text="Aquí irá el resultado")##Mostrar texto
    mensaje.pack()


ventana = tk.Tk()#inicio la ventana
ventana.title("Pagina de proyectos")#El titulo
ventana.geometry('800x500')#Tamaño

## comezamos a porner bonetes
frame_botones = tk.Frame(ventana, bg="white")
frame_botones.pack(pady=10)

boton1 = tk.Button(frame_botones, text="Registrar", font=("Arial", 12), fg="black", bg="grey", width=12, command=mostrar_registrar)
boton1.grid(row=0, column=0, padx=10, pady=10)

boton2 = tk.Button(frame_botones, text="Mostrar 2", font=("Arial", 12), fg="black", bg="grey", width=12, command=oe)
boton2.grid(row=0, column=1, padx=10, pady=10)

boton3 = tk.Button(frame_botones, text="Mostrar 3", font=("Arial", 12), fg="black", bg="grey", width=12, command=oe)
boton3.grid(row=0, column=2, padx=10, pady=10)

boton4 = tk.Button(frame_botones, text="Mostrar 4", font=("Arial", 12), fg="black", bg="grey", width=12, command=oe)
boton4.grid(row=0, column=3, padx=10, pady=10)









ventana.mainloop()#Para que se mantega abierta




