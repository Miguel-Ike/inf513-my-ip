# INF513 My IP

Esta herramienta fue creada para generar un mensaje de solicitud de actualización de IP para realizar el proyecto del primer parcial de la materia INF513. La herramienta obtiene la dirección IP pública y genera un saludo personalizado según el horario del día en tres idiomas: español, francés e inglés.

## Características

- Obtención de la dirección IP pública.
- Generación de saludos personalizados según el horario del día.
- Mensajes generados en tres idiomas: español, francés e inglés.

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

### Paso 1: Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/Miguel-Ike/inf513-my-ip.git
cd inf513-my-ip
```

### Paso 2: Crear y Activar un Entorno Virtual

Crea y activa un entorno virtual para instalar las dependencias:

En Windows:

```bash
python -m venv env
.\env\Scripts\activate
```

En Linux:

```bash
python3 -m venv env
source env/bin/activate
```

### Paso 3: Instalar las Dependencias

Instala las dependencias necesarias para ejecutar el proyecto:

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar Variables de Entorno

Crea un archivo .env en la raíz del proyecto con el siguiente contenido, adaptando los valores según sea necesario:

```bash
GROUP=XX XX
FULL_NAME=your full name
TEACHER=name of the teacher
```

## Ejecución

Para ejecutar el proyecto, sigue los siguientes pasos:

### Paso 1: Ejecutar el Script

Ejecuta el script principal del proyecto:

```bash
python main.py
```

## Estructura del Proyecto

```bash
inf513-my-ip/
├── .env
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── services/
    ├── __init__.py
    ├── config.py
    ├── ip_service.py
    ├── greeting_service.py
    └── message_service.py
```

## Contribución
Si deseas contribuir a este proyecto, por favor, sigue estos pasos:

Haz un fork del repositorio.
Crea una rama para tu característica (git checkout -b feature/nueva-caracteristica).
Realiza tus cambios y haz commit (git commit -am 'Agrega nueva característica').
Sube tu rama (git push origin feature/nueva-caracteristica).
Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.