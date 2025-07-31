from tkinter import *
import tkinter as tk
from tkinter import ttk

from Interface.test_interface import test_interface

if __name__ == "__main__":
    root = Tk()
    root.title("Sistema de Venta de Aplicaciones")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.attributes('-fullscreen', True)

    def exit_app(event=None):
        root.destroy()

    test_interface(None, root)

    root.bind('<Escape>', exit_app)
    root.mainloop()
