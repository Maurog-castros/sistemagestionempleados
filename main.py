from empresa.DAO.DAOpersona import DAOPersona

def main():
    # CRUD - CREATE, READ, UPDATE, DELETE
    # CLASE - CREAR, LEER, ACTUALIZAR, ELIMINAR

    # Crear una persona en la base de datos
    crear_persona = DAOPersona()
    crear_persona.crear_persona_db("Samir", "Goede", "samir.goede@ejemplo.com", "6543232")

    # Acá se podría demostrar la herencia de la clase usuario si existe alguna relación

if __name__ == '__main__':
    main()
