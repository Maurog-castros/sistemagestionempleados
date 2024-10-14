
import pymysql

host='localhost'
user='root'
password='Password01$'
db='empresa'

class ConexionDB:
    def __init__(self, host, user, password, db):
        self.db = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db)
        self.cursor = self.db.cursor()
    

    def ejecutar_query(self, query, parametros=()):
        self.cursor.execute(query, parametros)
        self.conn.commit()

    def cerrar(self):
        self.conn.close()

    def rollback(self):
        self.db.rollback()



   
