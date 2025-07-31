from tkinter import *
import tkinter as tk
from tkinter import ttk

from Interface.test_interface import test_interface
from Interface.Interface_system import FormularioClientes
from Dependencies.Conection import ConexionDB

if __name__ == "__main__":
    db = ConexionDB()
    db.conectar()
    usuarios = db.obtener_usuarios()
    print(usuarios)

    root = Tk()
    root.title("Sistema de Venta de Aplicaciones")
    root.geometry("1230x245")

    def exit_app(event=None):
        db.cerrar()
        root.destroy()

    root.bind('<Escape>', exit_app)

    formulario_clientes = FormularioClientes()
    # root.bind('<space>', lambda event: destruir_interface())
    destruir_interface = formulario_clientes.Formulario(root)

    root.mainloop()