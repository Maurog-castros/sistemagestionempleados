from empresa.modelos.empleado import Empleado
from empresa.db.conexion_db import ConexionDB

class GestionEmpleado:
    def __init__(self, conexion_db):
        self.conexion_db = conexion_db

    def registrar_empleado(self, empleado):
        query = """
        INSERT INTO empleados (id_persona, nombre, apellido, correo, telefono, fecha_contrato, salario) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        parametros = (
            empleado.get_id(),
            empleado.get_nombre(),
            empleado.get_apellido(),
            empleado.get_correo(),
            empleado.get_telefono(),
            empleado.get_fecha_contrato(),
            empleado.get_salario()
        )
        self.conexion_db.ejecutar_query(query, parametros)
