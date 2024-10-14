import datetime

class RegistroTiempo:
    def __init__(self, empleado_id, proyecto_id, fecha, horas_trabajadas, descripcion):
        self.empleado_id = empleado_id
        self.proyecto_id = proyecto_id
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion

    # Método para mostrar el registro de tiempo
    def mostrar_registro(self):
        return {
            'Empleado ID': self.empleado_id,
            'Proyecto ID': self.proyecto_id,
            'Fecha': self.fecha.strftime('%Y-%m-%d'),
            'Horas Trabajadas': self.horas_trabajadas,
            'Descripción': self.descripcion
        }

    # Método para actualizar horas trabajadas y descripción
    def actualizar_registro(self, horas_trabajadas, descripcion):
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion
        print("Registro actualizado correctamente")

    # Método estático para validar el formato de la fecha
    @staticmethod
    def validar_fecha(fecha):
        try:
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    # Método estático para validar horas trabajadas
    @staticmethod
    def validar_horas(horas):
        return horas >= 0
