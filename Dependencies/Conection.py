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
        
