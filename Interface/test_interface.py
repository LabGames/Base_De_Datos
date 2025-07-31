from tkinter import *
import tkinter as tk
from tkinter import ttk

def test_interface(self, root):
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    etiqueta_cliente = tk.Label(frame, text="Nombre del Cliente:")
    etiqueta_cliente.pack()
    entrada_cliente = tk.Entry(frame)
    entrada_cliente.pack()

    boton_confirmar = tk.Button(frame, text="Confirmar Venta", command=lambda: print("Venta realizada"))
    boton_confirmar.pack()

    def destruir_interface():
        frame.destroy()

    return destruir_interface