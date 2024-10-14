class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion, fecha_inicio):
        self.__id_proyecto = id_proyecto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio

    def mostrar_proyecto(self):
        return f"Proyecto: {self.__nombre}, Descripción: {self.__descripcion}, Fecha de Inicio: {self.__fecha_inicio}"
