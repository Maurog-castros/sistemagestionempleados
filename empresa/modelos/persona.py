class Persona:
    def __init__(self, id_persona, nombre, apellido, correo, telefono):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__telefono = telefono

    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

# Otras funcionalidades
