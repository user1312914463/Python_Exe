Compilador de Python a EXE

Introducción:
El Compilador de Python a EXE es una herramienta sencilla y fácil de usar que permite a los usuarios compilar scripts de Python en archivos ejecutables independientes (EXE). Esta herramienta ofrece una interfaz gráfica de usuario (GUI) intuitiva, que facilita la selección de archivos Python, directorios de salida, archivos de icono y la configuración de opciones de compilación. Además, se ha añadido un mecanismo de verificación de clave para garantizar la seguridad y el uso autorizado de la herramienta.

Características funcionales
Verificación de clave: Antes de usar la herramienta, es necesario introducir una clave válida para verificar, asegurando que solo los usuarios autorizados puedan utilizarla.
Interfaz gráfica de usuario: Proporciona una GUI intuitiva para que los usuarios seleccionen archivos y configuren opciones de compilación.
Configuración de opciones de compilación: Acepta una variedad de opciones de compilación, como el modo de archivo único, el modo de ventana, el modo de depuración, etc.
Guardado y carga de configuraciones: Los usuarios pueden guardar y cargar configuraciones de compilación para facilitar su uso en el futuro.
Salida de registro en tiempo real: Durante el proceso de compilación, se muestra un registro en tiempo real para que los usuarios puedan monitorizar el progreso.

Instalación y dependencia
Dependencias:
    Python 3.x
    PyInstaller: Se usa para compilar scripts de Python en archivos EXE.
    Pasos de instalación
    Asegúrate de tener instalado Python 3.x, que puedes descargar e instalar desde el sitio web oficial de Python.
Instala PyInstaller: Abre el terminal de línea de comandos y ejecuta el siguiente comando:
    pip install pyinstaller

Clona o descarga el código del proyecto en tu equipo local.

Método de uso (iniciar el programa):
    Abre el terminal de línea de comandos y navega hasta el directorio raíz del proyecto.
    Ejecuta el siguiente comando para iniciar el programa:
    python main.py

Verificación de claves:
    Al iniciar el programa por primera vez, aparecerá una ventana de verificación de clave.
    Introduce una clave válida y haz clic en el botón "Verificar".
    Si la verificación es exitosa, el programa se iniciará automáticamente; si falla, se mostrarán mensajes según el número de intentos restantes, y si se supera el límite de intentos fallidos, el archivo de clave se bloqueará.

Configuración de compilación:
    Archivo Python: Haz clic en el botón "Examinar..." para seleccionar el archivo Python que quieres compilar.
    Directorio de salida: Haz clic en el botón "Examinar..." para seleccionar el directorio donde se guardará el archivo EXE compilado.
    Archivo de icono (opcional): Haz clic en el botón "Examinar..." para seleccionar el archivo de icono (con extensión .ico) que se asignará al archivo EXE.
    Opciones de compilación:
    Modo de archivo único: Empaqueta todas las dependencias en un solo archivo EXE.
    Modo ventana (sin consola): El archivo EXE compilado se ejecuta sin mostrar una ventana de consola.
    Modo depuración: Activa el modo depuración para facilitar la depuración durante el proceso de compilación.
    Limpiar archivos temporales: Elimina los archivos temporales después de completar la compilación.
    Codificación de consola: Selecciona el formato de codificación para la salida de la consola.
    Guardado y carga de configuraciones
    Guardar configuraciones: Haz clic en el botón "Guardar configuraciones" para guardar las configuraciones actuales de compilación en el archivo py_to_exe_config.json.
    Cargar configuraciones: Haz clic en el botón "Cargar configuraciones" para cargar las configuraciones de compilación guardadas anteriormente desde el archivo py_to_exe_config.json.
    Iniciar la compilación
    Después de configurar las opciones de compilación, haz clic en el botón "Iniciar compilación" para comenzar el proceso.
    Durante la compilación, se mostrará el registro en tiempo real en el área de registro, y una barra de progreso indicará el avance.
    Una vez completada la compilación, aparecerá un cuadro de diálogo con el resultado.

Estructura del archivo:
exe/
├── main.py               # Punto de entrada del programa
├── key_verification.py   # Módulo de verificación de clave
├── compiler_gui.py       # Módulo de interfaz principal de compilación
├── compilation_engine.py # Módulo de motor de compilación
├── config_manager.py     # Módulo de gestión de configuraciones
├── resources/
│   └── keys.json         # Archivo de configuración de claves
├── py_to_exe_config.json # Archivo de guardado de configuraciones de compilación

!Notas!
Asegúrate de que la clave introducida sea válida; de lo contrario, es posible que la herramienta no funcione correctamente.
El proceso de compilación puede tardar algún tiempo, según la complejidad del script de Python y el rendimiento del sistema.
Si encuentras problemas durante la compilación, revisa la salida del registro y soluciona los errores según la información proporcionada.

Contribuciones y comentarios
Si encuentras algún error o tienes sugerencias de mejora, no dudes en agregar el QQ: 1312914463. También eres bienvenido a compartir tu experiencia de uso y proponer nuevas funcionalidades.