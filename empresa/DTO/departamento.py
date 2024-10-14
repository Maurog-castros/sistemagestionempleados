class Departamento:
    def __init__(self, id_departamento, nombre, gerente):
        self.__id_departamento = id_departamento
        self.__nombre = nombre
        self.__gerente = gerente
        self.__empleados = []

    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def mostrar_empleados(self):
        return [emp.mostrar_datos() for emp in self.__empleados]
