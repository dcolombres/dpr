#!/bin/bash

# Guardar el directorio actual
export PROJ_DIR=$(pwd)

# Función para verificar si un puerto está en uso
is_port_in_use() {
    lsof -i:$1 >/dev/null
}

# Iniciar el backend en una nueva pestaña de Terminal
if ! is_port_in_use 8000; then
    osascript -e "tell app \"Terminal\" to do script \"cd '$PROJ_DIR/backend' && source venv/bin/activate && uvicorn main:app --host 0.0.0.0 --port 8000\""
else
    echo "El puerto 8000 ya está en uso. Asumiendo que el backend ya se está ejecutando."
fi

# Iniciar el frontend en una nueva pestaña de Terminal
if ! is_port_in_use 3000; then
    osascript -e "tell app \"Terminal\" to do script \"cd '$PROJ_DIR/frontend' && npm start\""
else
    echo "El puerto 3000 ya está en uso. Asumiendo que el frontend ya se está ejecutando."
fi

# Esperar un momento para que los servidores se inicien
sleep 5

# Abrir el aplicativo en el navegador
open http://localhost:3000
