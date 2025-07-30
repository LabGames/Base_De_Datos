from tkinter import *
from tkinter import ttk

if __name__ == "__main__":
    root = Tk()
    root.title("App de Base de Datos")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.attributes('-fullscreen', True)
    root.mainloop()
