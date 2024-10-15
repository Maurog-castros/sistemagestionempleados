
import pymysql

host='localhost'
user='mauro'
password='Password01$'
db='empresa'

class ConexionDB:
    def __init__(self):
        self.db = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db)
        self.cursor = self.db.cursor()
    def conectar(self):
        try:
            self.db = pymysql.connect(
                host=host,
                user=user,
                password=password,
                db=db
            )
            self.cursor = self.db.cursor()
            print("Conexión exitosa a la base de datos")
        except pymysql.err.OperationalError as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise

    def __init__(self):
        self.conectar()

    def ejecutar_query(self, query, parametros=()):
        self.cursor.execute(query, parametros)
        self.conn.commit()

    def cerrar(self):
        self.conn.close()

    def rollback(self):
        self.db.rollback()



   
