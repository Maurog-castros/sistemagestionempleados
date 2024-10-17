from empresa.conexion_db import ConexionDB

class DTOPersona:
    def __init__(self, id_persona, nombre, apellido, correo, telefono):
            self.__id_persona = id_persona
            self.__nombre = nombre
            self.__apellido = apellido
            self.__correo = correo
            self.__telefono = telefono

    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"
    
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

# Otras funcionalidades
