# Informe Ejecutivo - Dashboard

Este proyecto es una aplicación web diseñada para visualizar y analizar los datos del archivo `Proyectos y Recursos 2025.xlsx`.

## Arquitectura

La aplicación consta de dos componentes principales:

1.  **Backend:** Una API desarrollada en Python con **FastAPI** que se encarga de leer y procesar los datos del archivo Excel.
2.  **Frontend:** Una interfaz de usuario interactiva desarrollada con **React** y **TypeScript** que consume los datos de la API y los presenta en un formato amigable.

## Configuración y Ejecución

### Prerrequisitos

- Python 3.8+
- Node.js y npm

### Backend

1.  **Navegar al directorio del backend:**
    ```bash
    cd backend
    ```
2.  **Crear y activar un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Ejecutar el servidor:**
    ```bash
    uvicorn main:app --reload
    ```
    El backend estará disponible en `http://127.0.0.1:8000`.

### Frontend

1.  **Navegar al directorio del frontend:**
    ```bash
    cd frontend
    ```
2.  **Instalar dependencias:**
    ```bash
    npm install
    ```
3.  **Iniciar la aplicación de desarrollo:**
    ```bash
    npm start
    ```
    La aplicación se abrirá automáticamente en `http://localhost:3000`.
