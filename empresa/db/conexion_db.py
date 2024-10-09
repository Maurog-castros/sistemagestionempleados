import sqlite3

class ConexionDB:
    def __init__(self, nombre_db):
        self.nombre_db = nombre_db

    def conectar(self):
        self.conn = sqlite3.connect(self.nombre_db)
        self.cursor = self.conn.cursor()

    def ejecutar_query(self, query, parametros=()):
        self.cursor.execute(query, parametros)
        self.conn.commit()

    def cerrar(self):
        self.conn.close()
