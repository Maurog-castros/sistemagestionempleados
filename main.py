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


# Crear una instancia de la clase Usuario utilizando el objeto persona
    usuario_uno = Usuario(
        id_usuario=persona_uno.id_persona,
        nombre_usuario=f"{persona_uno.nombre.lower()}{persona_uno.apellido.lower()}",
        contrasena="contraseña_temporal",
        persona=persona_uno
    )

    print(f"Se ha creado un usuario para: {usuario_uno.persona.get_nombre_completo()}")



    # Imprimir el nombre completo de la persona
    print(f"Se ha creado una persona: {persona_uno.get_nombre_completo()}")
    print(persona_uno.get_nombre_completo())





if __name__ == '__main__':
    main()
