from tkinter import *
import tkinter as tk
from tkinter import ttk

def test_interface(self, root):
    etiqueta_cliente = tk.Label(root, text="Nombre del Cliente:")
    etiqueta_cliente.pack()
    entrada_cliente = tk.Entry(root)
    entrada_cliente.pack()

    boton_confirmar = tk.Button(root, text="Confirmar Venta", command=lambda: print("Venta realizada"))
    boton_confirmar.pack()