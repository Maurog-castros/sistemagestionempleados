# Importar las clases Persona y Usuario
from empresa.modelos.persona import Persona
from empresa.modelos.usuario import Usuario


# Crear una instancia de la clase Persona
persona_uno = Persona(
    id_persona=1,
    nombre="Juan",
    apellido="Pérez",
    correo="juan.perez@ejemplo.com",
    telefono="123456789"
)

persona_dos = Persona(
    id_persona=2,
    nombre="Juana",
    apellido="Pérez",
    correo="juana.perez@ejemplo.com",
    telefono="12345"
)
persona_tres = Persona(
    id_persona=3,
    nombre="Juancha",
    apellido="Pérez",
    correo="juana.perez@ejemplo.com",
    telefono="12345"
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
