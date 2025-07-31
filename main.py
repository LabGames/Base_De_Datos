from tkinter import *
import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = Tk()
    root.title("Sistema de Venta de Aplicaciones")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.attributes('-fullscreen', True)

    def exit_app(event=None):
        root.destroy()

    etiqueta_cliente = tk.Label(root, text="Nombre del Cliente:")
    etiqueta_cliente.pack()
    entrada_cliente = tk.Entry(root)
    entrada_cliente.pack()

    boton_confirmar = tk.Button(root, text="Confirmar Venta", command=lambda: print("Venta realizada"))
    boton_confirmar.pack()

    root.bind('<Escape>', exit_app)
    root.mainloop()
