from tkinter import *
import tkinter as tk
from tkinter import ttk

from Dependencies.Conection import ConexionDB
from Interface.Interface_Switcher import InterfaceSwitcher

if __name__ == "__main__":
    db = ConexionDB("localhost", "root", "", "gestiontarea")
    db.conectar()

    root = Tk()
    root.title("Sistema de Venta de Aplicaciones")
    

    switcher = InterfaceSwitcher(root)
    switcher.set_db(db)

    def exit_app(event=None):
        db.cerrar()
        root.destroy()

    root.bind('<Escape>', exit_app)
    switcher.show_clientes()

    x = 0
    y = 0

    def update():
        InterfaceSwitcher.set_size(x, y)
        
        root.after(16, update)

    update()

    root.geometry("{x}x{y}+0+0")

    root.mainloop()

    
