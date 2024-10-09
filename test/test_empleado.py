import unittest
from empresa.modelos.empleado import Empleado
from empresa.gestion.gestion_empleado import GestionEmpleado
from empresa.db.conexion_db import ConexionDB

class TestEmpleado(unittest.TestCase):
    def setUp(self):
        self.conexion = ConexionDB('empresa.db').conectar()
        self.gestion_empleado = GestionEmpleado()

    def test_registrar_empleado(self):
        empleado = Empleado(1, "Juan", "Pérez", "juan.perez@correo.com", None)
        self.gestion_empleado.registrar_empleado(self.conexion, empleado)
        # Aquí puedes verificar si se creó correctamente el empleado en la base de datos

    def tearDown(self):
        self.conexion.close()

if __name__ == '__main__':
    unittest.main()
