from empresa.modelos.empleado import Empleado
from empresa.gestion.gestion_empleado import GestionEmpleado
from empresa.db.conexion_db import ConexionDB

def main():
    # Inicializar la conexión a la base de datos
    conexion = ConexionDB('empresa.db')
    conexion.conectar()

    # Crear un empleado
    empleado1 = Empleado(1, "Juan", "Perez", "juan.perez@empresa.com", "123456789", "2024-01-01", 500000)
    gestion_empleado = GestionEmpleado(conexion)

    # Registrar el empleado en la base de datos
    gestion_empleado.registrar_empleado(empleado1)

    # Cerrar la conexión
    conexion.cerrar()

if __name__ == '__main__':
    main()
