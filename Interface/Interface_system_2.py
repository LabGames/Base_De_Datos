import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from Dependencies.Conection import ConexionDB
from .Interface_Switcher import InterfaceSwitcher

class FormularioTareas:
    def __init__(self, db, switcher):
        self.db = ConexionDB()
        self.db.conectar()
        self.switcher = switcher

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
        
        self.form_frame = ttk.LabelFrame(root, text="Datos de la tarea")
        self.form_frame.pack(fill="x", padx=10, pady=5)

        self.titulo_var = tk.StringVar()
        self.estado_var = tk.StringVar()
        self.fecha_limite_var = tk.StringVar()
        self.prioridad_var = tk.StringVar()

        ttk.Label(self.form_frame, text="Título:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.titulo_entry = ttk.Entry(self.form_frame, textvariable=self.titulo_var)
        self.titulo_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Estado:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.estado_combo = ttk.Combobox(self.form_frame, textvariable=self.estado_var, values=["Pendiente", "En Proceso", "Completado"])
        self.estado_combo.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Fecha límite (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.fecha_entry = ttk.Entry(self.form_frame, textvariable=self.fecha_limite_var)
        self.fecha_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Prioridad:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.prioridad_combo = ttk.Combobox(self.form_frame, textvariable=self.prioridad_var, values=["Baja", "Media", "Alta"])
        self.prioridad_combo.grid(row=1, column=3, padx=5, pady=5)

        self.boton_frame = ttk.Frame(root)
        self.boton_frame.pack(fill="x", padx=10, pady=5)

        ttk.Button(self.boton_frame, text="Guardar", command=self.guardar_tarea).pack(side="left", padx=5)
        ttk.Button(self.boton_frame, text="Modificar", command=self.modificar_tarea).pack(side="left", padx=5)
        ttk.Button(self.boton_frame, text="Eliminar", command=self.eliminar_tarea).pack(side="left", padx=5)

        self.tabla = ttk.Treeview(root, columns=("id", "titulo", "estado", "fecha", "prioridad"), show="headings")
        self.tabla.heading("id", text="ID")
        self.tabla.heading("titulo", text="Título")
        self.tabla.heading("estado", text="Estado")
        self.tabla.heading("fecha", text="Fecha Límite")
        self.tabla.heading("prioridad", text="Prioridad")
        self.tabla.column("id", width=30)
        self.tabla.pack(fill="both", expand=True, padx=10, pady=5)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_fila)

        self.cargar_tareas()

    def guardar_tarea(self):
        titulo = self.titulo_var.get()
        estado = self.estado_var.get()
        fecha = self.fecha_limite_var.get()
        prioridad = self.prioridad_var.get()

        if not (titulo and estado and fecha and prioridad):
            messagebox.showwarning("Campos incompletos", "Completa todos los campos.")
            return

        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "La fecha debe tener el formato YYYY-MM-DD.")
            return

        try:
            self.db.cursor.execute(
                "INSERT INTO tareas (titulo, estado, fecha_limite, prioridad) VALUES (%s, %s, %s, %s)",
                (titulo, estado, fecha, prioridad)
            )
            self.db.conn.commit()
            self.limpiar_formulario()
            self.cargar_tareas()
        except Exception as e:
            messagebox.showerror("Error al guardar", str(e))

    def modificar_tarea(self):
        selected = self.tabla.selection()
        if not selected:
            messagebox.showwarning("Selecciona una tarea", "Debes seleccionar una tarea para modificarla.")
            return

        item = self.tabla.item(selected[0])
        id_tarea = item["values"][0]

        titulo = self.titulo_var.get()
        estado = self.estado_var.get()
        fecha = self.fecha_limite_var.get()
        prioridad = self.prioridad_var.get()

        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "La fecha debe tener el formato YYYY-MM-DD.")
            return

        try:
            self.db.cursor.execute(
                "UPDATE tareas SET titulo=%s, estado=%s, fecha_limite=%s, prioridad=%s WHERE id=%s",
                (titulo, estado, fecha, prioridad, id_tarea)
            )
            self.db.conn.commit()
            self.limpiar_formulario()
            self.cargar_tareas()
        except Exception as e:
            messagebox.showerror("Error al modificar", str(e))

    def eliminar_tarea(self):
        selected = self.tabla.selection()
        if not selected:
            messagebox.showwarning("Selecciona una tarea", "Debes seleccionar una tarea para eliminarla.")
            return

        item = self.tabla.item(selected[0])
        id_tarea = item["values"][0]

        if messagebox.askyesno("Eliminar", "¿Seguro que deseas eliminar esta tarea?"):
            try:
                self.db.cursor.execute("DELETE FROM tareas WHERE id=%s", (id_tarea,))
                self.db.conn.commit()
                self.limpiar_formulario()
                self.cargar_tareas()
            except Exception as e:
                messagebox.showerror("Error al eliminar", str(e))

    def cargar_tareas(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)

        self.db.cursor.execute("SELECT * FROM tareas")
        for row in self.db.cursor.fetchall():
            self.tabla.insert("", "end", values=row)

    def seleccionar_fila(self, event):
        selected = self.tabla.selection()
        if selected:
            item = self.tabla.item(selected[0])
            id_tarea, titulo, estado, fecha, prioridad = item["values"]
            self.titulo_var.set(titulo)
            self.estado_var.set(estado)
            self.fecha_limite_var.set(fecha)
            self.prioridad_var.set(prioridad)

    def limpiar_formulario(self):
        self.titulo_var.set("")
        self.estado_var.set("")
        self.fecha_limite_var.set("")
        self.prioridad_var.set("")