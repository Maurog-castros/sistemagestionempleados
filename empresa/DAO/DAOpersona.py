from empresa.conexion_db import ConexionDB
from empresa import config
class DAOPersona:
    def __init__(self):
        # Inicializamos la conexión
        self.conexion = ConexionDB(
            host='138.255.101.220', 
            user='maurocastro_python', 
            password='HVpvJg.Tyn)%', 
            db='maurocastro_empresa'
        )

    def crear_persona_db(self, nombre, apellido, correo, telefono):
        try:
            # Ejecutar el query con parámetros seguros
            query = "INSERT INTO Persona (nombre, apellido, correo, telefono) VALUES (%s, %s, %s, %s)"
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
    def eliminarporID(self, idPersona):
        try:
            # Ejecutamos el query para eliminar una persona específica por su ID
            query = "DELETE FROM Persona WHERE idPersona = %s"
            resultado = self.conexion.ejecuta_query(query, (idPersona,))
            
            # Confirmamos la transacción
            self.conexion.commit()
            
            # Verificamos si se eliminó algún registro
            if resultado.rowcount > 0:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error al eliminar persona de la base de datos: {e}")
            self.conexion.rollback()
            return False

        finally:
            # Cerrar la conexión en cualquier caso
            self.conexion.desconectar()
    def leer_todos(self):
        try:
            # Ejecutamos el query para leer todas las personas
            query = "SELECT idPersona, nombre, apellido, correo, telefono FROM Persona"
            personas = self.conexion.ejecuta_query(query)
            
            return personas

        except Exception as e:
            print(f"Error al leer personas de la base de datos: {e}")
            return []

        finally:
            # Cerrar la conexión en cualquier caso
            self.conexion.desconectar()
    def modificar_persona_db(self, idPersona, nombre, apellido, correo, telefono):
        try:
            # Ejecutar el query para actualizar los campos
            query = """ 
            UPDATE Persona 
            SET nombre = %s, apellido = %s, correo = %s, telefono = %s
            WHERE idPersona = %s
            """
            # Ejecutar el query con los parámetros proporcionados
            self.conexion.ejecuta_query(query, (nombre, apellido, correo, telefono, idPersona))
            
            # Confirmar la transacción
            self.conexion.commit()
            print(f"Persona con ID {idPersona} modificada exitosamente.")

        except Exception as e:
        # En caso de error, imprimir y realizar rollback si es necesario
          print(f"Error al modificar persona en la base de datos: {e}")
          self.conexion.rollback()

        finally:
        # Cerrar la conexión en cualquier caso
            self.conexion.desconectar()

    def consultaparticular(self, idPersona):
        try:
            # Ejecutamos el query para buscar una persona específica por su ID
            query = "SELECT * FROM Persona WHERE idPersona = %s"
            resultado = self.conexion.ejecuta_query(query, (idPersona,))
            
            # Obtenemos el primer (y único) resultado
            persona = resultado.fetchone()
            
            if persona:
                return persona
            else:
                return "No se encontraron registros"

        except Exception as e:
            print(f"Error al consultar persona en la base de datos: {e}")
            return "No se encontraron registros"

        finally:
            # Cerrar la conexión en cualquier caso
            self.conexion.desconectar()