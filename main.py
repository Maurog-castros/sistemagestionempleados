from empresa.DAO.DAOpersona import DAOPersona
import os

def main():
    # CRUD - CREATE, READ, UPDATE, DELETE
    # CLAE - CREAR, LEER, ACTUALIZAR, ELIMINAR

    # Crear una persona en la base de datos
    # crear_persona = DAOPersona()
    # crear_persona.crear_persona_db("Mauro", "Castro", "mauro.castro@ejemplo.com", "6543232")

    while True:
        menupincipal()  # Llamada a la función corregida
        opcion = input("Selecciona una opción: ").upper()
        
        if opcion == 'C':
            crear_registro_persona()
            # Lógica de ingreso de datos aquí
        elif opcion == 'R':
            menumostrar()
            subopcion = input("Selecciona una opción de MOSTRAR: ").upper()
            if subopcion == '1':
                print("Mostrando todos los registros...")
            elif subopcion == '2':
                print("Mostrando un registro...")
            elif subopcion == '3':
                print("Mostrando registros parciales...")
            elif subopcion == '4':
                continue  # Vuelve al menú principal
        elif opcion == 'U':
            print("Opción MODIFICAR seleccionada.")
            # Lógica de modificación aquí
        elif opcion == 'D':
            print("Opción ELIMINAR seleccionada.")
            # Lógica de eliminación aquí
        elif opcion == 'E':
            print("Saliendo del programa...")
            os.system('cls' if os.name == 'nt' else 'clear')
            
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menupincipal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    ================================
            M E N Ú  P R I N C I P A L
    ================================
    1.- (C) INGRESAR
    2.- (R) MOSTRAR
    3.- (U) MODIFICAR
    4.- (D) ELIMINAR
    5.- (E) SALIR
    ================================
    """)

def menumostrar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    ================================
        M E N Ú  M O S T R A R
    ================================
    1.- MOSTRAR TODO
    2.- MOSTRAR UNO
    3.- MOSTRAR PARCIAL
    4.- VOLVER
    ================================
    """)
def crear_registro_persona():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Crear Nuevo Registro de Persona ===")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    correo = input("Ingrese el correo electrónico: ")
    telefono = input("Ingrese el número de teléfono: ")
    
    try:
        crear_persona = DAOPersona()
        crear_persona.crear_persona_db(nombre, apellido, correo, telefono)
        print("Registro creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el registro: {e}")

if __name__ == '__main__':
    main()
   

