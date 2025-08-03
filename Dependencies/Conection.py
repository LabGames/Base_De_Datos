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
        
    def crear_usuario(self, nombre, email):
        try:
            self.cursor.execute(
                "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)",
                (nombre, email)
            )
            self.conn.commit()
            print("Usuario creado correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al crear usuario: {e}")

    def actualizar_usuario(self, user_id, nombre, email):
        try:
            self.cursor.execute(
                "UPDATE usuarios SET nombre=%s, email=%s WHERE id=%s",
                (nombre, email, user_id)
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

    #Odio esta mierda
    def obtener_tareas(self):
        if not self.cursor:
            print("No hay conexión activa.")
            return []
        try:
            self.cursor.execute("SELECT * FROM tareas")
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error al acceder a la tabla usuarios: {e}")
            return []
        
    def crear_tareas(self, titulo, estado, fecha_limite, prioridad):
        try:
            self.cursor.execute(
                "INSERT INTO tareas (titulo, estado, fecha_limite, prioridad) VALUES (%s, %s)",
                (titulo, estado, fecha_limite, prioridad)
            )
            self.conn.commit()
            print("Tarea creado correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al crear usuario: {e}")

    def actualizar_tareas(self, user_id, titulo, estado, fecha_limite, prioridad):
        try:
            self.cursor.execute(
                "UPDATE tareas SET titulo=%s, estado=%s, fecha_limite=%s, prioridad=%s WHERE id=%s",
                (titulo, estado, fecha_limite, prioridad, user_id)
            )
            self.conn.commit()
            print("Tarea actualizado correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al actualizar usuario: {e}")

    def eliminar_tareas(self, title):
        try:
            self.cursor.execute(
                "DELETE FROM tareas SET titulo=%s VALUES (%s, %s)",
                (title)
            )
            self.conn.commit()
            print("Usuario eliminado correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al eliminar usuario: {e}")

    