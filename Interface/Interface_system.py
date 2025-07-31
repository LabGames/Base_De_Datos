import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Dependencies.Conection import ConexionDB

class FormularioClientes:
    def __init__(self, db):
        self.db = db

    def Formulario(self, root):
        try:
            bg_color = "#9babbb"
            bg_transparent = "#f0f4f800"
            frame_color = "#e0e7ef"
            label_color = "#2d4059"
            entry_bg = "#ffffff"
            button_bg = "#3a7ca5"
            button_fg = "#ffffff"
            groupbox_bg = "#b6c9e2"

            x_base, y_base = 0, 0
            x_groupbox, y_groupbox = 10, 10
            x_groupbox2, y_groupbox2 = 400, 50
            x_label_registrar, y_label_registrar = -10, 7

            base = tk.Frame(root, bg=bg_color)
            base.place(x=x_base, y=y_base, relwidth=1, relheight=1)

            groupBox = LabelFrame(
                base, text="Datos del personal", padx=5, pady=5,
                bg=groupbox_bg, fg=label_color, font=("Segoe UI Semibold", 12, "bold")
            )
            groupBox.place(x=x_groupbox, y=y_groupbox)

            Label(groupBox, text="ID:", width=13, font=("Segoe UI",12), bg=groupbox_bg, fg=label_color).grid(row=0, column=0, padx=5, pady=5)
            textBoxId = Entry(groupBox, bg=entry_bg)
            textBoxId.grid(row=0, column=1, padx=5, pady=5)

            Label(groupBox, text="Nombres:", width=13, font=("Segoe UI",12), bg=groupbox_bg, fg=label_color).grid(row=1, column=0, padx=5, pady=5)
            textBoxNombres = Entry(groupBox, bg=entry_bg)
            textBoxNombres.grid(row=1, column=1, padx=5, pady=5)

            Label(groupBox, text="Apellidos:", width=13, font=("Segoe UI",12), bg=groupbox_bg, fg=label_color).grid(row=2, column=0, padx=5, pady=5)
            textBoxApellidos = Entry(groupBox, bg=entry_bg)
            textBoxApellidos.grid(row=2, column=1, padx=5, pady=5)

            Label(groupBox, text="Sexo:", width=13, font=("Segoe UI",12), bg=groupbox_bg, fg=label_color).grid(row=3, column=0, padx=5, pady=5)
            seleccionSexo = StringVar()
            combo = ttk.Combobox(groupBox, values=["Masculino", "Femenino", "Anonimo"], textvariable=seleccionSexo)
            combo.grid(row=3, column=1, padx=5, pady=5)

            Button(groupBox, text="Guardar", width=10, bg=button_bg, fg=button_fg, command=lambda: self.guardar_usuario(textBoxNombres.get(), textBoxApellidos.get())).grid(row=4, column=0, padx=2, pady=8)
            Button(groupBox, text="Modificar", width=10, bg=button_bg, fg=button_fg, command=lambda: self.modificar_usuario(textBoxId.get(), textBoxNombres.get(), textBoxApellidos.get())).grid(row=4, column=1, padx=2, pady=8)
            Button(groupBox, text="Eliminar", width=10, bg=button_bg, fg=button_fg, command=lambda: self.eliminar_usuario(textBoxId.get())).grid(row=4, column=2, padx=2, pady=8)

            groupBox2 = LabelFrame(
                base, text="Lista del personal", padx=5, pady=5,
                bg=groupbox_bg, fg=label_color, font=("Segoe UI Semibold", 12, "bold")
            )
            groupBox2.place(x=x_groupbox2, y=y_groupbox2)

            style = ttk.Style()
            style.theme_use('default')

            style.configure(
                "Treeview",
                background=frame_color,
                fieldbackground=frame_color,
                foreground=label_color,
                font=("Segoe UI", 10)
            )
            style.configure(
                "Treeview.Heading",
                background=button_bg,
                foreground=button_fg,
                font=("Segoe UI Semibold", 11, "bold")
            )

            self.tree = ttk.Treeview(groupBox2, columns=("ID", "Nombres", "Apellidos", "Sexo"), show='headings', height=5)
            self.tree.column("# 1", anchor=CENTER)
            self.tree.heading("# 1", text="ID")

            self.tree.column("# 2", anchor=CENTER)
            self.tree.heading("# 2", text="Nombres")

            self.tree.column("# 3", anchor=CENTER)
            self.tree.heading("# 3", text="Apellidos")

            self.tree.column("# 4", anchor=CENTER)
            self.tree.heading("# 4", text="Sexo")

            self.tree.pack()

            self.cargar_usuarios(tree)

            label_registrar = tk.Label(
                base,
                text="REGISTRAR PERSONAL",
                bg=bg_color,
                fg=button_bg,
                font=("Segoe UI Semibold", 15, "bold"),
                anchor="e"
            )
            label_registrar.place(relx=1.0, x=x_label_registrar, y=y_label_registrar, anchor="ne")

            self.base = base

        except Exception as error:
            print(f"Error al mostrar la interfaz, error: {error}")

    def destruir_interface(self):
        if hasattr(self, 'base'):
            self.base.destroy()

    def guardar_usuario(self, nombre, email):
        if nombre and email:
            self.db.crear_usuario(nombre, email)
            self.cargar_usuarios(self.tree)
            messagebox.showinfo("Éxito", "Usuario guardado.")
        else:
            messagebox.showerror("Error", "Nombre y correo requeridos.")

    def modificar_usuario(self, user_id, nombre, email):
        if user_id and nombre and email:
            self.db.actualizar_usuario(user_id, nombre, email)
            self.cargar_usuarios(self.tree)
            messagebox.showinfo("Éxito", "Usuario modificado.")
        else:
            messagebox.showerror("Error", "Todos los campos son requeridos.")

    def eliminar_usuario(self, user_id):
        if user_id:
            self.db.eliminar_usuario(user_id)
            self.cargar_usuarios(self.tree)
            messagebox.showinfo("Éxito", "Usuario eliminado.")
        else:
            messagebox.showerror("Error", "ID requerido.")

    def cargar_usuarios(self, tree):
        for row in tree.get_children():
            tree.delete(row)
        for usuario in self.db.obtener_usuarios():
            tree.insert("", tk.END, values=usuario)
