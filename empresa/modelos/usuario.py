class Usuario(Persona):
    def __init__(self, id_persona, nombre, apellido, correo, telefono, clave, acceso):
        super().__init__(id_persona, nombre, apellido, correo, telefono)
        self.__clave = clave
        self.__acceso = acceso

    def verificar_acceso(self, clave):
        return self.__clave == clave

    def mostrar_usuario(self):
        return f"Usuario: {self.get_nombre_completo()}, Acceso: {self.__acceso}"
