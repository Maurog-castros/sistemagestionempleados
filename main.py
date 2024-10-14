from empresa.DTO.empleado import Empleado
from empresa.gestion.gestion_empleado import GestionEmpleado
from empresa.DAO.conexion_db import ConexionDB
from empresa.DTO.DTOpersona import Persona
from empresa.DTO.usuario import Usuario
from empresa.DAO.DAOpersona import DAOPersona

def main():

#CRUD - CREATE, READ, UPDATE, DELETE
#CLAE - CREAR, LEER, ACTUALIZAR, ELIMINAR   

# Crear una persona en la base de datos
    CrearPersona = DAOPersona()
    CrearPersona.crear_persona_db("Juan", "Perez", "juan.perez@ejemplo.com", "123456789")

#aca se demuestra la herencia de la clase usuario
    
if __name__ == '__main__':
    main()
