from empresa.conexion_db import ConexionDB
from empresa.DTO.DTOpersona import DTOPersona


class DAOPersona:
    def __init__(self):
        self.conexion = ConexionDB(
            host='localhost', 
            user='empresauser', 
            password='carrera1903', 
            db='empresa'
        )

    def crear_persona_db(self, persona: DTOPersona):
        try:
            query = "INSERT INTO persona (nombre, apellido, correo, telefono) VALUES (%s, %s, %s, %s)"
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
            query = "SELECT id_persona, nombre, apellido, correo, telefono FROM persona"
            resultado = self.conexion.ejecuta_query(query)
            
            # Crear una lista de objetos DTOPersona con los resultados
            personas = [DTOPersona(id_persona=row[0], nombre=row[1], apellido=row[2], correo=row[3], telefono=row[4]) for row in resultado]
            
            return personas
        except Exception as e:
            print(f"Error al consultar personas en la base de datos: {e}")
            return []

    def consultar_por_id(self, id_persona):
        try:
            query = "SELECT id_persona, nombre, apellido, correo, telefono FROM Persona WHERE id_persona = %s"
            self.conexion.ejecuta_query(query, (id_persona))
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
            query = "UPDATE persona SET nombre = %s, apellido = %s, correo = %s, telefono = %s WHERE id_persona = %s"
            self.conexion.ejecuta_query(
                query, 
                (persona.get_nombre(), persona.get_apellido(), persona.get_correo(), persona.get_telefono(), persona.get_id_persona())
            )
            self.conexion.commit()
            print(f"Persona {persona.get_id_persona()} actualizada correctamente.")
        except Exception as e:
            print(f"Error al actualizar persona en la base de datos: {e}")
            self.conexion.rollback()

    def eliminar_por_id(self, id_persona):
        try:
            query = "DELETE FROM persona WHERE id_persona = %s"
            self.conexion.ejecuta_query(query, (id_persona))
            self.conexion.commit()
            print(f"Persona con ID {id_persona} eliminada correctamente.")
        except Exception as e:
            print(f"Error al eliminar persona en la base de datos: {e}")
            self.conexion.rollback()
