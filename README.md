> [!NOTE]  
> # Sistema Gestión de Empleados

```
├── empresa/
│   ├── __init__.py             # Indica que es un paquete Python
│   ├── DAO/                    # Clases del modelo (Persona, Empleado, Usuario, Proyecto, etc.)
│   │   ├── __init__.py         # Importación de módulos
│   │   ├── DAOpersona.py       # Clase Persona
│   ├── DTO/                    # Lógica de negocio (gestión de empleados, usuarios, proyectos, registros de tiempo)
│   │   ├── __init__.py         # Importación de módulos
│   │   ├── DTOdepartamento.py  # Métodos de gestión de empleados
│   │   ├── DTOempleado.py      # Métodos de gestión de usuarios
│   │   ├── DTOpersona.py       # Métodos de gestión de proyectos
│   │   └── DTOusuario.py       # Métodos de gestión de registro de tiempo
├── conexion_db.py              # Configuraciones generales del proyecto (ej. variables de entorno)
├── main.py                     # Punto de entrada principal para ejecutar el programa
└── README.md                   # Descripción del proyecto y cómo ejecutarlo


> [!TIP]
> Construido modularmente con paradigma OOB Python.

> [!IMPORTANT]  
> No esta terminado aun, falta base de datos

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Este proyecto tiene la siguiente estructura de directorios:

