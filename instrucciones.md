# Manual de Usuario: Dashboard de Proyectos y Recursos

## 1. Introducción

Esta aplicación es una herramienta web diseñada para visualizar, analizar y gestionar los datos contenidos en el archivo Excel `data.xlsx`. Permite ver la información en un dashboard con gráficos dinámicos y también editar los datos directamente desde una interfaz similar a una hoja de cálculo.

---

## 2. Primeros Pasos

### Requisitos
- macOS
- Tener las dependencias del backend y frontend instaladas (Python/pip y Node.js/npm).

### Cómo Iniciar la Aplicación

Para iniciar la aplicación, simplemente ejecuta el siguiente comando en tu terminal desde la carpeta raíz del proyecto:

```bash
./start.sh
```

Este script hará lo siguiente:
1.  Abrirá una nueva ventana de Terminal para el **backend** y lo iniciará.
2.  Abrirá otra nueva ventana de Terminal para el **frontend** y lo iniciará.
3.  Abrirá automáticamente tu navegador en `http://localhost:3000` con la aplicación lista para usar.

---

## 3. Secciones de la Aplicación

La aplicación tiene dos vistas principales y un selector de hojas.

- **Selector de Hojas (`Proyectos` / `Staff`):** Ubicado debajo de la cabecera, te permite elegir qué hoja del archivo Excel quieres visualizar o gestionar.
- **Vista `Dashboard`:** Es la vista principal para visualización y análisis de datos.
- **Vista `Gestionar Datos`:** Es la vista para editar, añadir o eliminar datos de las hojas.

You can switch between these views using the main navigation buttons in the header.

---

## 4. El Dashboard

Esta es la vista por defecto. Te permite analizar tus datos de forma visual e interactiva.

- **Filtros:** En la parte superior, encontrarás una serie de filtros. Puedes escribir en los campos de texto o seleccionar valores en los menús desplegables. Después de configurar tus filtros, pulsa **`Aplicar Filtros`**. Los gráficos y la tabla se actualizarán para mostrar solo los datos que coincidan con tu búsqueda. Usa **`Limpiar Filtros`** para volver a ver todos los datos.
- **Gráficos Dinámicos:** Debajo de los filtros, verás gráficos que resumen la información de la tabla. Estos gráficos son dinámicos y se actualizan automáticamente cada vez que aplicas un filtro.
- **Tabla de Datos:** Muestra los datos en formato de solo lectura.

---

## 5. Gestión de Datos

Esta vista te permite modificar el contenido del archivo `data.xlsx` directamente desde la web.

- **Editar Celdas:** Simplemente haz clic en cualquier celda de la tabla. Se convertirá en un campo de texto donde podrás escribir el nuevo valor.
- **Añadir Fila:** Pulsa el botón **`Añadir Fila`**. Aparecerá una nueva fila en blanco al final de la tabla para que la completes.
- **Eliminar Filas:** Marca la casilla de la izquierda en cada fila que desees eliminar. Luego, pulsa **`Eliminar Seleccionadas`**.
- **Guardar Cambios:** Este es el paso más importante. Después de hacer cualquier modificación (editar, añadir o eliminar), debes pulsar el botón **`Guardar Cambios`** para que todo se escriba permanentemente en el archivo `data.xlsx`.

---

## 6. Reglas de Oro y Advertencias

Para asegurar el buen funcionamiento de la aplicación, es crucial seguir estas reglas.

### ¡MUY IMPORTANTE: El Archivo Excel!

- **Cerrar Excel Siempre:** La aplicación necesita leer y escribir en el archivo `data.xlsx`. Si tienes este archivo abierto en Microsoft Excel, LibreOffice u otro programa, la aplicación **se colgará**. Asegúrate siempre de que el archivo esté completamente cerrado antes de usar la aplicación web.
- **Actualizar Datos Externos:** Si modificas el archivo `data.xlsx` externamente, la aplicación web no se actualizará en tiempo real. Para ver tus cambios, debes guardar y cerrar el archivo Excel, y luego en la web, refrescar los datos (por ejemplo, cambiando de hoja y volviendo a la original).
- **⚠️ ADVERTENCIA SOBRE PÉRDIDA DE DATOS:** Si estás en la vista `Gestionar Datos` y tienes cambios sin guardar en la tabla, **perderás esos cambios** si refrescas la página o cambias de hoja antes de pulsar "Guardar Cambios".

### ¡NO TOCAR: Columnas Críticas!

La aplicación depende de que ciertas columnas existan con un nombre exacto. Cambiar el nombre o eliminar estas columnas **romperá** los filtros y los gráficos.

- Para la hoja **`PROYECTOS`**, no modifiques los nombres de:
  - `Origen`
  - `Tier`
  - `Salud`
  - `Estado`
  - `Prioridad`

- Para la hoja **`STAFF`**, no modifiques los nombres de:
  - `Seniority`
  - `Tecnologia`
  - `Contrato`
  - `ROL`

### Solución de Problemas

- **"La aplicación se cuelga o no carga datos"**: La causa 99% de las veces es que el archivo `data.xlsx` está abierto en otro programa o se ha corrompido.
  1.  Asegúrate de que el archivo `data.xlsx` está cerrado en todas partes.
  2.  Si el problema persiste, es posible que el archivo esté dañado. La solución es crear un **nuevo archivo Excel en blanco**, copiar y pegar los datos de las hojas `PROYECTOS` y `STAFF` del archivo viejo al nuevo, y guardar el nuevo archivo como `data.xlsx`, sobrescribiendo el anterior.
