import mysql.connector

class ConexionDB:
    def __init__(self, host="localhost", user="root", password="", database="gestiontarea"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("Conexión exitosa a la base de datos MySQL.")
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrar(self):
        if self.conn:
            self.conn.close()
            print("Conexión cerrada.")

    def obtener_usuarios(self):
        if not self.cursor:
            print("No hay conexión activa.")
            return []
        try:
            self.cursor.execute("SELECT * FROM usuarios")
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error al acceder a la tabla usuarios: {e}")
            return []
        
    def crear_usuario(self, nombre):
        try:
            self.cursor.execute(
                "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)",
                (nombre)
            )
            self.conn.commit()
            print("Usuario creado correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al crear usuario: {e}")

    def actualizar_usuario(self, user_id, nombre):
        try:
            self.cursor.execute(
                "UPDATE usuarios SET nombre=%s, email=%s WHERE id=%s",
                (nombre, user_id)
            )
            self.conn.commit()
            print("Usuario actualizado correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al actualizar usuario: {e}")

    def eliminar_usuario(self, user_id):
        try:
            self.cursor.execute(
                "DELETE FROM usuarios WHERE id=%s",
                (user_id,)
            )
            self.conn.commit()
            print("Usuario eliminado correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al eliminar usuario: {e}")

    #Funciones de un usuario
    def obtener_tareas(self):
        if not self.cursor:
            print("No hay conexión activa.")
            return []
        try:
            self.cursor.execute("SELECT * FROM tareas")
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error al acceder a la tabla tareas: {e}")
            return []

    def crear_tarea(self, titulo, estado, fecha_limite, prioridad, usuario_id):
        try:
            self.cursor.execute(
                "INSERT INTO tareas (titulo, estado, fecha_limite, prioridad, usuario_id) VALUES (%s, %s, %s, %s, %s)",
                (titulo, estado, fecha_limite, prioridad, usuario_id)
            )
            self.conn.commit()
            print("Tarea creada correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al crear tarea: {e}")

    def actualizar_tarea(self, tarea_id, titulo, estado, fecha_limite, prioridad, usuario_id):
        try:
            self.cursor.execute(
                "UPDATE tareas SET titulo=%s, estado=%s, fecha_limite=%s, prioridad=%s, usuario_id=%s WHERE id=%s",
                (titulo, estado, fecha_limite, prioridad, usuario_id, tarea_id)
            )
            self.conn.commit()
            print("Tarea actualizada correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al actualizar tarea: {e}")

    def eliminar_tarea(self, tarea_id):
        try:
            self.cursor.execute(
                "DELETE FROM tareas WHERE id=%s",
                (tarea_id,)
            )
            self.conn.commit()
            print("Tarea eliminada correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al eliminar tarea: {e}")