from empresa.DAO.conexion_db import ConexionDB

class DAOPersona:
    def __init__(self):
        # Inicializamos la conexión
        self.conexion = ConexionDB(host='127.0.0.1', user='root', password='Password01$', db='empresa')

    def crear_persona_db(self, nombre, apellido, correo, telefono):
        try:
            # Ejecutar el query con parámetros seguros
            query = "INSERT INTO persona (nombre, apellido, correo, telefono) VALUES (%s, %s, %s, %s)"
            self.conexion.ejecuta_query(query, (nombre, apellido, correo, telefono))
            
            # Confirmar la transacción
            self.conexion.commit()
        
        except Exception as e:
            # En caso de error, imprimir y realizar rollback si es necesario
            print(f"Error al insertar persona en la base de datos: {e}")
            self.conexion.rollback()  # Asegúrate de que ConexionDB soporte rollback

        finally:
            # Cerrar la conexión en cualquier caso
            self.conexion.desconectar()
