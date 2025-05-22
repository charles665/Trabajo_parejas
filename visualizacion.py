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
    def registrar():
     nombre = entry_nombre.get()
     longitud = entry_longitud.get()
     gestor.registrar_proyecto(nombre, longitud)
     tk.Label(ventana1, text="Proyecto registrado", fg="green").pack()


    boton_registrar = tk.Button(frame_registro, text="Registrar", command=registrar)
    boton_registrar.grid(row=2, column=1, padx=5, pady=5)

def mostrar_datos():
    ventana2 = tk.Toplevel(ventana)
    ventana2.title('Resumen de proyectos')
    ventana2.geometry('600x400')

    df = gestor.cargar_todos()

    texto = tk.Text(ventana2, wrap='none')
    texto.insert(tk.END, df.to_string(index=False))  
    texto.pack(padx=10, pady=10, fill='both', expand=True)

def mostrar_proyecto():

    ventana3 = tk.Toplevel(ventana)
    ventana3.title("Ver proyecto por número")
    ventana3.geometry("400x200")

    tk.Label(ventana3, text="Ingrese el número del proyecto:").pack(pady=10)
    entry_numero = tk.Entry(ventana3)
    entry_numero.pack(pady=5)

    resultado = tk.Label(ventana3, text="")
    resultado.pack(pady=10)

    def buscar():
        numero = entry_numero.get()
        try:
            proyecto = gestor.ver_proyectos(numero)
            texto = ""
            for clave, valor in proyecto.items():
                texto += f"{clave}: {valor}\n"
            resultado.config(text=texto, fg="black")
        except:
            resultado.config(text="Número de proyecto no válido")

    tk.Button(ventana3, text="Buscar", command=buscar).pack(pady=5)



def oe():
    print('hola')
  

ventana = tk.Tk()#inicio la ventana
ventana.title("Pagina de proyectos")#El titulo
ventana.geometry('800x500')#Tamaño

## comezamos a porner botones
frame_botones = tk.Frame(ventana, bg="white")
frame_botones.pack(pady=10)

boton1 = tk.Button(frame_botones, text="Registrar", font=("Arial", 12), fg="black", bg="grey", width=12, command=mostrar_registrar)
boton1.grid(row=0, column=0, padx=10, pady=10)

boton2 = tk.Button(frame_botones, text="Mostrar datos", font=("Arial", 12), fg="black", bg="grey", width=12, command=mostrar_datos)
boton2.grid(row=0, column=1, padx=10, pady=10)

boton3 = tk.Button(frame_botones, text="Mostrar proyecto", font=("Arial", 8), fg="black", bg="grey", width=12, command=mostrar_proyecto)
boton3.grid(row=0, column=2, padx=10, pady=10)

boton4 = tk.Button(frame_botones, text="Mostrar 4", font=("Arial", 12), fg="black", bg="grey", width=12, command=oe)
boton4.grid(row=0, column=3, padx=10, pady=10)









ventana.mainloop()#Para que se mantega abierta




