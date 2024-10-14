from empresa.modelos.empleado import Empleado
from empresa.gestion.gestion_empleado import GestionEmpleado
from empresa.db.conexion_db import ConexionDB
from empresa.modelos.persona import Persona
from empresa.modelos.usuario import Usuario

def main():
   
# Crear una instancia de la clase Persona
    persona_uno = Persona(
    id_persona=1,
    nombre="Juan",
    apellido="Pérez",
    correo="juan.perez@ejemplo.com",
    telefono="123456789"
)
#aca se demuestra la herencia de la clase usuario
    usuario = Usuario(
        id_usuario=persona_uno._Persona__id_persona,
        nombre_usuario=persona_uno._Persona__correo.split('@')[0],
        contrasena="contraseña_temporal",
        persona=persona_uno
)
if __name__ == '__main__':
    main()
