class DTOPersona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, correo=None, telefono=None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__telefono = telefono

    # Métodos Getter
    def get_id_persona(self):
        return self.__id_persona

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # Métodos Setter
    def set_id_persona(self, id_persona):
        self.__id_persona = id_persona

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_correo(self, correo):
        self.__correo = correo

    def set_telefono(self, telefono):
        self.__telefono = telefono

    # Método para representar el objeto como una cadena (opcional)
    def __str__(self):
        return f"Persona(ID: {self.__id_persona}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, Correo: {self.__correo}, Teléfono: {self.__telefono})"
