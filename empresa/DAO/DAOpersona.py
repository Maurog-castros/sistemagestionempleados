from empresa.DAO.conexion import ConexionDB

class DAOPersona:
    def __init__(self):
        self.conexion = ConexionDB()

    def crear_persona_db(self, nombre, apellido, correo, telefono):
        self.conexion.ejecutar_query("INSERT INTO persona (nombre, apellido, correo, telefono) VALUES (%s, %s, %s, %s)", (nombre, apellido, correo, telefono))
        self.conexion.commit()
        self.conexion.desconectar()

