from empresa.DTO.persona import Persona  # Importa la clase Persona

class Empleado(Persona):
    def __init__(self, id_empleado, nombre, apellido, correo, departamento):
        self.__id_empleado = id_empleado
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__departamento = departamento

    # Getters y setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
