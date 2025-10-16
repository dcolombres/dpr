# Instrucciones para Gemini

## Objetivo del Proyecto

El objetivo es construir una aplicación web completa para que el usuario pueda manipular, analizar y generar informes a partir de los datos contenidos en el archivo `Proyectos y Recursos 2025.xlsx`.

## Stack Tecnológico

- **Backend:** Python, FastAPI, Pandas, Uvicorn.
- **Frontend:** React, TypeScript, Node.js/npm.

## Estructura de Directorios

- `/backend`: Contiene la aplicación FastAPI.
- `/frontend`: Contiene la aplicación React.
- `Proyectos y Recursos 2025.xlsx`: Es la fuente de datos principal. Se encuentra en el directorio raíz del proyecto.

## Instrucciones Clave

- **Fuente de Datos:** La ruta absoluta del archivo Excel es `/Users/dcolom/Informe ejecutivo/Proyectos y Recursos 2025.xlsx`. El backend debe leer este archivo.
- **Entornos:** Trabaja siempre con el entorno virtual de Python activado para el backend (`source backend/venv/bin/activate`) y utiliza `npm` o `npx` dentro de la carpeta `frontend` para las tareas relacionadas con la interfaz.
- **Comandos Backend:**
    - Instalar dependencias: `pip install -r backend/requirements.txt`
    - Ejecutar servidor: `cd backend && uvicorn main:app --reload`
- **Comandos Frontend:**
    - Instalar dependencias: `cd frontend && npm install`
    - Iniciar desarrollo: `cd frontend && npm start`
- **Proactividad:** Eres responsable de crear la estructura de carpetas (`backend`, `frontend`), los archivos de configuración (`requirements.txt`, `package.json`), y el código fuente para ambos componentes.
