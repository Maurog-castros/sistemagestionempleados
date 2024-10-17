from empresa.conexion_db import ConexionDB
from empresa.DTO.DTOpersona import DTOPersona


class DAOPersona:
    def __init__(self):
        self.conexion = ConexionDB(
            host='138.255.101.220', 
            user='maurocastro_python', 
            password='HVpvJg.Tyn)%', 
            db='maurocastro_empresa'
        )

    def crear_persona_db(self, persona: DTOPersona):
        try:
            query = "INSERT INTO Persona (nombre, apellido, correo, telefono) VALUES (%s, %s, %s, %s)"
            self.conexion.ejecuta_query(
                query, 
                (persona.get_nombre(), persona.get_apellido(), persona.get_correo(), persona.get_telefono())
            )
            self.conexion.commit()
            print(f"Persona {persona.get_nombre()} {persona.get_apellido()} creada exitosamente.")
        except Exception as e:
            print(f"Error al insertar persona en la base de datos: {e}")
            self.conexion.rollback()

    def consultar_todos(self):
        try:
            query = "SELECT IdPersona, nombre, apellido, correo, telefono FROM Persona"
            resultado = self.conexion.ejecuta_query(query)
            
            # Crear una lista de objetos DTOPersona con los resultados
            personas = [DTOPersona(id_persona=row[0], nombre=row[1], apellido=row[2], correo=row[3], telefono=row[4]) for row in resultado]
            
            return personas
        except Exception as e:
            print(f"Error al consultar personas en la base de datos: {e}")
            return []

    def consultar_por_id(self, IdPersona):
        try:
            query = "SELECT idPersona, nombre, apellido, correo, telefono FROM Persona WHERE idPersona = %s"
            self.conexion.ejecuta_query(query, (IdPersona))
            resultado = self.conexion.cursor.fetchone()
            
            if resultado:
                # Ajustar el nombre del parámetro al que espera el constructor de DTOPersona
                return DTOPersona(id_persona=resultado[0], nombre=resultado[1], apellido=resultado[2], correo=resultado[3], telefono=resultado[4])
            else:
                return None
        except Exception as e:
            print(f"Error al consultar persona por ID: {e}")
            return None

    def modificar_persona_db(self, persona: DTOPersona):
        try:
            query = "UPDATE Persona SET nombre = %s, apellido = %s, correo = %s, telefono = %s WHERE idPersona = %s"
            self.conexion.ejecuta_query(
                query, 
                (persona.get_nombre(), persona.get_apellido(), persona.get_correo(), persona.get_telefono(), persona.get_IdPersona())
            )
            self.conexion.commit()
            print(f"Persona {persona.get_IdPersona()} actualizada correctamente.")
        except Exception as e:
            print(f"Error al actualizar persona en la base de datos: {e}")
            self.conexion.rollback()

    def eliminar_por_id(self, IdPersona):
        try:
            query = "DELETE FROM Persona WHERE IdPersona = %s"
            self.conexion.ejecuta_query(query, (IdPersona,))
            self.conexion.commit()
            print(f"Persona con ID {IdPersona} eliminada correctamente.")
        except Exception as e:
            print(f"Error al eliminar persona en la base de datos: {e}")
            self.conexion.rollback()
