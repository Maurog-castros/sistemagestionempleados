from empresa.DAO.DAOpersona import DAOPersona
from empresa.DTO.DTOpersona import DTOPersona
import os

def main():
    # CRUD - CREATE, READ, UPDATE, DELETE
    while True:
        menupincipal()  # Llamada a la función corregida
        opcion = input("Selecciona una opción: ").upper()
        
        if opcion == 'C':
            crear_registro_persona()
        elif opcion == 'R':
            menumostrar()
            subopcion = input("Selecciona una opción de MOSTRAR: ").upper()
            if subopcion == '1':
                mostrar_todo()
            elif subopcion == '2':
                mostrar_uno()
            elif subopcion == '4':
                continue  # Vuelve al menú principal
        elif opcion == 'U':
            modificar_registro_persona()
        elif opcion == 'D':
            eliminar_registro_persona()
        elif opcion == 'E':
            print("Saliendo del programa...")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menupincipal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    ============================================
            M E N Ú  P R I N C I P A L
    ============================================
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
    ============================================
        M E N Ú  M O S T R A R
    ============================================
    1.- MOSTRAR TODO
    2.- MOSTRAR UNO POR ID
    4.- VOLVER
    ================================
    """)

import os

def mostrar_todo():
    # Limpiar la pantalla según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Mostrar Todos los Registros ===\n")

    try:
        dao_persona = DAOPersona()  # Crear instancia de DAO
        personas = dao_persona.consultar_todos()  # Consultar todos los registros

        if not personas:
            print("No hay registros disponibles.")
        else:
            # Encabezado
            print(f"{'ID':<5} | {'Nombre':<15} | {'Apellido':<15} | {'Correo':<25} | {'Teléfono':<12}")
            print("-" * 75)
            
            # Mostrar cada persona con formato alineado
            for persona in personas:
                print(f"{persona.get_id_persona():<5} | {persona.get_nombre():<15} | {persona.get_apellido():<15} | {persona.get_correo():<25} | {persona.get_telefono():<12}")
            
            print("-" * 75)  # Separador final
            
        input("\nPresione Enter para continuar...")
        
    except Exception as e:
        print(f"Error al mostrar los registros: {e}")
        input("\nPresione Enter para continuar...")  # Pausar para que el usuario vea el error

def mostrar_uno():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Mostrar Registro por ID ===")
    
    try:
        id_persona = input("Ingrese el ID de la persona: ")
        dao_persona = DAOPersona()
        persona = dao_persona.consultar_por_id(id_persona)

        if persona:
            print("\n+-----------------------------+")
            print(f"| ID       : {persona.get_id_persona()}")
            print(f"| Nombre   : {persona.get_nombre()}")
            print(f"| Apellido : {persona.get_apellido()}")
            print(f"| Correo   : {persona.get_correo()}")
            print(f"| Teléfono : {persona.get_telefono() if persona.get_telefono() else 'No disponible'}")
            print("+-----------------------------+\n")
        else:
            print("\nNo se encontró ninguna persona con ese ID.\n")

        input("Presione Enter para continuar...")
    except Exception as e:
        print(f"Error al mostrar el registro: {e}")


def crear_registro_persona():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Crear Nuevo Registro de Persona ===")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    correo = input("Ingrese el correo electrónico: ")
    telefono = input("Ingrese el número de teléfono: ")
    
    # Crear instancia de DTOPersona con los datos ingresados
    persona = DTOPersona(nombre=nombre, apellido=apellido, correo=correo, telefono=telefono)
    
    try:
        dao_persona = DAOPersona()
        dao_persona.crear_persona_db(persona)
        print("Registro creado exitosamente.")
        input("Presione Enter para continuar...")        
    except Exception as e:
        print(f"Error al crear el registro: {e}")

def modificar_registro_persona():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Modificar Registro de Persona ===")
    
    try:
        idPersona = input("Ingrese el ID de la persona que desea modificar: ")
        datos = DAOPersona().consultar_por_id(idPersona)

        if not datos:
            print(f"No se encontraron datos para la persona con ID: {idPersona}")
            return

        # Mostrar los datos actuales
        print(f"\nDatos actuales de la persona con ID {idPersona}:")
        print(f"1. Nombre: {datos.get_nombre()}")
        print(f"2. Apellido: {datos.get_apellido()}")
        print(f"3. Correo: {datos.get_correo()}")
        print(f"4. Teléfono: {datos.get_telefono()}")

        # Modificar y actualizar la información
        nombre = input(f"Ingrese el nuevo nombre (actual: {datos.get_nombre()}): ") or datos.get_nombre()
        apellido = input(f"Ingrese el nuevo apellido (actual: {datos.get_apellido()}): ") or datos.get_apellido()
        correo = input(f"Ingrese el nuevo correo (actual: {datos.get_correo()}): ") or datos.get_correo()
        telefono = input(f"Ingrese el nuevo teléfono (actual: {datos.get_telefono()}): ") or datos.get_telefono()

        persona_modificada = DTOPersona(idPersona, nombre, apellido, correo, telefono)
        DAOPersona().modificar_persona_db(persona_modificada)
        print("Registro actualizado exitosamente.")
    
    except Exception as e:
        print(f"Error al modificar el registro: {e}")

    input("Presiona Enter para continuar...")

def eliminar_registro_persona():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Eliminar Registro de Persona ===")
    idPersona = input("Ingrese el ID de la persona a eliminar: ")
    
    try:
        resultado = DAOPersona().eliminar_por_id(idPersona)
        if resultado:
            print("No se encontró el registro o no se pudo eliminar.")
        else:
            print("Registro eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar el registro: {e}")
    
    input("Presiona Enter para continuar...")

if __name__ == '__main__':
    main()
