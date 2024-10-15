
import pymysql

host='127.0.0.1'
user='root'
password='Password01$'
db='empresa'


class ConexionDB:
    def _init_(self, host, user, password, db):
        self.db=pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db)
        self.cursor=self.db.cursor()
        
    def ejecuta_query(self,sql):
        self.cursor.execute(sql)
        return self.cursor
    
    def desconectar(self):
        self.db.close()

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()