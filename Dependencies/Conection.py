import sqlite3

class ConexionDB:
    def __init__(self, db_path="gestiontarea.db"):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            print("Conexión exitosa a la base de datos.")
        except sqlite3.Error as e:
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
        except sqlite3.Error as e:
            print(f"Error al acceder a la tabla usuarios: {e}")
            return []
        
