# Mi Aplicación Flask

Este es un proyecto de ejemplo que utiliza Flask, un microframework de Python.

## Estructura del Proyecto

- `app/`: Contiene el código de la aplicación.
- `app/__init__.py`: Inicializa la aplicación Flask y las rutas.
- `app/routes.py`: Define las rutas de la aplicación.
- `app/templates/`: Contiene las plantillas HTML.
- `app/static/`: Contiene los archivos estáticos como CSS.
- `tests/`: Contiene las pruebas unitarias de la aplicación.
- `config.py`: Configuración de la aplicación.
- `run.py`: Inicia la aplicación.
- `venv/`: Contiene el entorno virtual de Python.

## Cómo correr el proyecto

1. Activar el entorno virtual: `source venv/bin/activate`
2. Instalar las dependencias: `pip install -r requirements.txt`
3. Correr la aplicación: `python run.py`

## Cómo correr las pruebas

1. Activar el entorno virtual: `source venv/bin/activate`
2. Correr las pruebas: `python -m unittest discover tests`
```