from empresa.DTO.empleado import Empleado
from empresa.gestion.gestion_empleado import GestionEmpleado
from empresa.DAO.conexion_db import ConexionDB
from empresa.DTO.DTOpersona import Persona
from empresa.DTO.usuario import Usuario

def main():

#CRUD - CREATE, READ, UPDATE, DELETE
#CLAE - CREAR, LEER, ACTUALIZAR, ELIMINAR   

# Crear una persona en la base de datos
    persona_uno = Persona()
    persona_uno.crear_persona_db("Juan", "Perez", "juan.perez@ejemplo.com", "123456789")

#aca se demuestra la herencia de la clase usuario
    usuario = Usuario(
        id_usuario=persona_uno._Persona__id_persona,
        nombre_usuario=persona_uno._Persona__correo.split('@')[0],
        contrasena="contraseña_temporal",
        persona=persona_uno
)
if __name__ == '__main__':
    main()
