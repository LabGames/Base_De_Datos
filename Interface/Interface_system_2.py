import tkinter as tk
import datetime

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Dependencies.Conection import ConexionDB

class FormularioTareas:
    def __init__(self, db, switcher):
        self.db = ConexionDB()
        self.db.conectar()
        self.switcher = switcher

    def switching_interface(self):
        from .Interface_Switcher import InterfaceSwitcher
        switcher = InterfaceSwitcher(self.root)
        switcher.set_db(self.db)
        switcher.show_clientes()

    def switching_interface(self):
        self.switcher.show_clientes()

    def Formulario_2(self, root):
        bg_color = "#9babbb"
        frame_color = "#e0e7ef"
        label_color = "#2d4059"
        entry_bg = "#ffffff"
        button_bg = "#3a7ca5"
        button_fg = "#ffffff"
        groupbox_bg = "#b6c9e2"

        x_base, y_base = 0, 0
        x_groupbox, y_groupbox = 10, 10
        x_groupbox2, y_groupbox2 = 450, 50
        x_label_registrar, y_label_registrar = -10, 7
        
        base = tk.Frame(root, bg=bg_color)
        base.place(x=x_base, y=y_base, relwidth=1, relheight=1)
        
        groupBox = LabelFrame(
            base, text="Datos de las tareas", padx=5, pady=5,
            bg=groupbox_bg, fg=label_color, font=("Segoe UI Semibold", 12, "bold")
        )
        groupBox.place(x=x_groupbox, y=y_groupbox)

        LabelId = Label(groupBox, text="ID USUARIO:", width=13, font=("arial",12)).grid(row=0, column=0, padx=5, pady=5)
        self.textBoxId = Entry(groupBox, bg=entry_bg, state="readonly")
        self.textBoxId.grid(row=0, column=1, padx=5, pady=5)

        LabelId_2 = Label(groupBox, text="ID TAREA:", width=13, font=("arial",12)).grid(row=1, column=0, padx=5, pady=5)
        self.textBoxId_2 = Entry(groupBox, bg=entry_bg, state="readonly")
        self.textBoxId_2.grid(row=1, column=1, padx=5, pady=5)

        LabelTitulo = Label(groupBox, text="Titulo:", width=13, font=("arial",12)).grid(row=2, column=0, padx=5, pady=5)
        self.textBoxTittle = Entry(groupBox, bg=entry_bg)
        self.textBoxTittle.grid(row=2, column=1, padx=5, pady=5)

        LabelEstado = Label(groupBox, text="Estado:", width=13, font=("arial",12)).grid(row=3, column=0, padx=5, pady=5)
        self.seleccionEstado = StringVar()
        self.combo = ttk.Combobox(groupBox, values=["Pendiente", "En progreso", "Completada"], textvariable=self.seleccionEstado)
        self.combo.grid(row=3, column=1, padx=5, pady=5)
        self.seleccionEstado.set("Pendiente")

        LabelFechaLimite = Label(groupBox, text="FechaLimite:", width=13, font=("arial",12)).grid(row=4, column=0, padx=5, pady=5)
        self.fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
        self.textBoxFechaLimite = Entry(groupBox, bg=entry_bg)
        self.textBoxFechaLimite.insert(0, self.fecha_actual)
        self.textBoxFechaLimite.grid(row=4, column=1, padx=5, pady=5)

        LabelPrioridad = Label(groupBox, text="Prioridad:", width=13, font=("arial",12)).grid(row=5, column=0, padx=5, pady=5)
        self.seleccionPrioridad = StringVar()
        self.combo = ttk.Combobox(groupBox, values=["Alta", "Media", "Baja"], textvariable=self.seleccionPrioridad)
        self.combo.grid(row=5, column=1, padx=5, pady=5)
        self.seleccionPrioridad.set("Media")

        Button(
            groupBox, 
            text="Guardar", 
            width=10,
            bg=button_bg, fg=button_fg,
            command=lambda: self.guardar_tareas(self.textBoxId.get(), self.textBoxTittle.get(), self.seleccionEstado.get(), self.textBoxFechaLimite.get(), self.seleccionPrioridad.get(), self.textBoxId.get())
        ).grid(row=6, column=0,)

        Button(
            groupBox, 
            text="Modificar", 
            width=10,
            bg=button_bg, fg=button_fg,
            command=lambda: self.modificar_tareas(self.textBoxId_2.get(), self.textBoxTittle.get(), self.seleccionEstado.get(), self.textBoxFechaLimite.get(), self.seleccionPrioridad.get(), self.textBoxId.get())
        ).grid(row=6, column=1)

        Button(
            groupBox, 
            text="Eliminar", 
            width=10,
            bg=button_bg, fg=button_fg,
            command=lambda: self.eliminar_tareas(self.textBoxId_2.get())
        ).grid(row=6, column=2)

        Button(
            groupBox, 
            text="Personal", 
            width=10, 
            bg=button_bg, fg=button_fg, 
            command=lambda: self.switching_interface(root)
        ).grid(row=6, column=3, padx=2, pady=8)


        groupBox2 = LabelFrame(
            base, text="Lista de tareas", padx=5, pady=5,
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

        self.tabla = ttk.Treeview(root, columns=("id", "titulo", "estado", "fecha", "prioridad", "tarea ID"), show="headings")
        self.tabla.column("# 1", anchor=CENTER)
        self.tabla.heading("# 1", text="ID")

        self.tabla.column("# 2", anchor=CENTER)
        self.tabla.heading("# 2", text="Titulo")

        self.tabla.column("# 3", anchor=CENTER)
        self.tabla.heading("# 3", text="Estado")

        self.tabla.column("# 4", anchor=CENTER)
        self.tabla.heading("# 4", text="Fecha")

        self.tabla.column("# 5", anchor=CENTER)
        self.tabla.heading("# 5", text="Prioridad")

        self.tabla.column("# 6", anchor=CENTER)
        self.tabla.heading("# 7", text="Tarea ID")

        self.tabla.pack()
        self.tabla.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.cargar_tareas()

        label_registrar = tk.Label(
            base,
            text="REGISTRAR TAREAS",
            bg=bg_color,
            fg=button_bg,
            font=("Segoe UI Semibold", 15, "bold"),
            anchor="e"
        )
        label_registrar.place(relx=1.0, x=x_label_registrar, y=y_label_registrar, anchor="ne")

        self.base = base

    def destruir_interface(self):
        if hasattr(self, 'base'):
            self.base.destroy()

    def guardar_tareas(self, titulo, estado, fecha_limite, prioridad, usuario_id):
        if titulo and estado and fecha_limite and prioridad and usuario_id:
            print(f"NOMBRE: {titulo}, EMAIL: {estado}, FECHA: {fecha_limite}, PRIORIDAD: {prioridad}, USUARIO_ID: {usuario_id}")
            self.db.crear_tarea(titulo, estado, fecha_limite, prioridad, usuario_id)
            self.cargar_tareas(self.tabla)
            self.textBoxId.delete(0, tk.END)
            self.textBoxId_2.delete(1, tk.END)
            self.textBoxTittle.delete(2, tk.END)
            self.textBoxFechaLimite.delete(4, tk.END)
            messagebox.showinfo("Éxito", "Usuario guardado.")
        else:
            print(f"NOMBRE: {titulo}, EMAIL: {estado}, FECHA: {fecha_limite}, PRIORIDAD: {prioridad}, USUARIO_ID: {usuario_id}")
            messagebox.showerror("Error", "Todos los campos son requeridos.")

    def modificar_tareas(self, tarea_id, titulo, estado, fecha_limite, prioridad, usuario_id):
        if tarea_id and titulo and estado and fecha_limite and prioridad and usuario_id:
            self.db.actualizar_tarea(tarea_id, titulo, estado, fecha_limite, prioridad, usuario_id)
            self.cargar_tareas(self.tabla)
            messagebox.showinfo("Éxito", "Usuario modificado.")
        else:
            messagebox.showerror("Error", "Todos los campos son requeridos.")

    def eliminar_tareas(self, tarea_id):
        if tarea_id:
            self.db.eliminar_usuario(tarea_id)
            self.cargar_tareas(self.tabla)
            messagebox.showinfo("Éxito", "Usuario eliminado.")
        else:
            messagebox.showerror("Error", "ID requerido.")

    def cargar_tareas(self, tabla):
        for row in tabla.get_children():
            tabla.delete(row)
        for usuario in self.db.obtener_tareas():
            tabla.insert("", tk.END, values=usuario)

    def on_tree_select(self, event):
        selected_item = self.tabla.selection()
        if selected_item:
            item = self.tabla.item(selected_item)
            valores = item["values"]

            self.textBoxId.config(state="normal")
            self.textBoxId.delete(0, END)
            self.textBoxId.insert(0, valores[0])
            self.textBoxId.config(state="readonly")

            self.textBoxTittle.delete(0, tk.END)
            self.textBoxTittle.insert(0, valores[1])

            self.seleccionEstado.get(valores[2])

            self.textBoxFechaLimite.delete(0, tk.END)
            self.textBoxFechaLimite.insert(0, valores[3])

            self.seleccionPrioridad.get(valores[4])

            self.textBoxId.config(state="normal")
            self.textBoxId.delete(0, END)
            self.textBoxId.insert(0, valores[5])
            self.textBoxId.config(state="readonly")
            