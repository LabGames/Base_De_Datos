from tkinter import *
import tkinter as tk
from tkinter import ttk

from Dependencies.Conection import ConexionDB
from Interface.Interface_Switcher import InterfaceSwitcher
from Interface.Interface_system import FormularioClientes
from Interface.Interface_system_2 import FormularioTareas

if __name__ == "__main__":
    db = ConexionDB("localhost", "root", "", "gestiontarea")
    db.conectar()
    usuarios = db.obtener_usuarios()
    print(usuarios)

    root = Tk()
    root.title("Sistema de Venta de Aplicaciones")
    root.geometry("1085x245")
    root.resizable(False, False)

    switcher = InterfaceSwitcher(root)
    switcher.set_db(db)

    def exit_app(event=None):
        db.cerrar()
        root.destroy()

    root.bind('<Escape>', exit_app)

    switcher.show_clientes()

    root.mainloop()