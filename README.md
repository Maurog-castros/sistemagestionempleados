# Sistema Gestión de Empleados
> .[!NOTE]
> Este proyecto tiene la siguiente estructura de directorios:

> .[!TIP]
> Python Project

> .[!IMPORTANT]
>  No esta terminado aun

> .[!WARNING]
> None

> [!NOTE]  
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]  
> Crucial information necessary for users to succeed.

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.

```
├── empresa/
│   ├── __init__.py            # Indica que es un paquete Python
│   ├── modelos/               # Clases del modelo (Persona, Empleado, Usuario, Proyecto, etc.)
│   │   ├── __init__.py        # Importación de módulos
│   │   ├── persona.py         # Clase Persona
│   │   ├── empleado.py        # Clase Empleado
│   │   ├── usuario.py         # Clase Usuario
│   │   ├── departamento.py    # Clase Departamento
│   │   ├── proyecto.py        # Clase Proyecto
│   │   ├── registro_tiempo.py # Clase RegistroTiempo
│   └── └── __init__.py
│   ├── gestion/               # Lógica de negocio (gestión de empleados, usuarios, proyectos, registros de tiempo)
│   │   ├── __init__.py        # Importación de módulos
│   │   ├── gestion_empleado.py  # Métodos de gestión de empleados
│   │   ├── gestion_usuario.py   # Métodos de gestión de usuarios
│   │   ├── gestion_proyecto.py  # Métodos de gestión de proyectos
│   │   └── gestion_registro_tiempo.py  # Métodos de gestión de registro de tiempo
│   ├── db/                    # Conexión a la base de datos y operaciones CRUD
│   │   ├── __init__.py        # Importación de módulos
│   │   ├── conexion_db.py     # Clase para conexión a la base de datos
│   │   ├── crear_tablas.py    # Script para crear las tablas en la base de datos
│   │   └── crud_registro_tiempo.py  # CRUD para registros de tiempo
│   └── utils/                 # Funciones utilitarias (validaciones, manejo de errores, etc.)
│       ├── __init__.py        # Importación de módulos
│       ├── validador.py       # Validaciones de datos
│       └── logger.py          # Registro de logs (logging)
├── tests/                     # Tests unitarios
│   ├── __init__.py
│   ├── test_empleado.py       # Pruebas para la clase Empleado
│   ├── test_usuario.py        # Pruebas para la clase Usuario
│   ├── test_registro_tiempo.py# Pruebas para la clase RegistroTiempo
│   └── test_gestion.py        # Pruebas para las gestiones de negocio
├── .gitignore                 # Archivos que deben ser ignorados por Git (ej. archivos .db)
├── config.py                  # Configuraciones generales del proyecto (ej. variables de entorno)
├── main.py                    # Punto de entrada principal para ejecutar el programa
└── README.md                  # Descripción del proyecto y cómo ejecutarlo
