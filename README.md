# fundamento_codespaces

Este proyecto está configurado para trabajar con Python en un entorno virtual y utilizar Streamlit para crear aplicaciones web interactivas.

## Requisitos previos

- Python 3.x instalado
- VS Code con la extensión de Python

## Crear y activar el entorno virtual

Desde la terminal, ejecuta:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Instalar dependencias

Con el entorno virtual activado, instala Streamlit:

```bash
pip install streamlit
```

## Ejecutar una aplicación Streamlit

1. Crea un archivo, por ejemplo, `app.py` con el siguiente contenido:

	```python
	import streamlit as st
	st.title('¡Hola, Streamlit!')
	st.write('Esta es una app de ejemplo.')
	```

2. Ejecuta la aplicación con:

	```bash
	streamlit run app.py
	```

Esto abrirá la app en tu navegador predeterminado.