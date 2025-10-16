import pandas as pd
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any

# La ruta absoluta al archivo Excel
EXCEL_FILE_PATH = "../data.xlsx"

app = FastAPI(
    title="API de Informe Ejecutivo",
    description="API para leer datos del archivo Excel de Proyectos y Recursos.",
    version="0.1.0",
)

# Configuración de CORS para permitir solicitudes desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Origen del frontend de React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Funciones de Ayuda para leer/escribir Excel ---

def read_excel_sheets():
    try:
        return pd.read_excel(EXCEL_FILE_PATH, sheet_name=None)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="El archivo Excel no se encontró.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al leer el archivo Excel: {e}")

def write_excel_sheets(sheets_dict):
    try:
        with pd.ExcelWriter(EXCEL_FILE_PATH, engine='openpyxl') as writer:
            for sheet_name, df in sheets_dict.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al escribir en el archivo Excel: {e}")

# --- Endpoints existentes ---

@app.get("/")
def read_root():
    """Endpoint de bienvenida."""
    return {"message": "Bienvenido a la API del Informe Ejecutivo"}

@app.get("/api/columns")
def get_columns(sheet: str):
    sheets = read_excel_sheets()
    if sheet not in sheets:
        raise HTTPException(status_code=404, detail=f"La hoja '{sheet}' no se encontró.")
    return {"columns": sheets[sheet].columns.tolist()}

@app.get("/api/filter")
def filter_data(sheet: str, request: Request):
    sheets = read_excel_sheets()
    if sheet not in sheets:
        raise HTTPException(status_code=404, detail=f"La hoja '{sheet}' no se encontró.")
    
    df = sheets[sheet].fillna('')
    filters = request.query_params
    for column, value in filters.items():
        if column == 'sheet':
            continue
        if column in df.columns:
            df = df[df[column].astype(str).str.contains(value, case=False, na=False)]

    return df.to_dict(orient='records')

@app.get("/api/unique-values")
def get_unique_values(sheet: str, column: str):
    sheets = read_excel_sheets()
    if sheet not in sheets:
        raise HTTPException(status_code=404, detail=f"La hoja '{sheet}' no se encontró.")
    
    df = sheets[sheet]
    if column not in df.columns:
        raise HTTPException(status_code=404, detail=f"La columna '{column}' no se encontró.")

    unique_values = df[column].unique().tolist()
    unique_values = [v for v in unique_values if pd.notna(v) and v != '']
    unique_values.sort()
    return {"values": unique_values}

@app.get("/api/staff-names")
def get_staff_names():
    sheets = read_excel_sheets()
    sheet_name = "STAFF"
    column_name = "NOMBRE"

    if sheet_name not in sheets:
        raise HTTPException(status_code=404, detail=f"La hoja '{sheet_name}' no se encontró.")

    df = sheets[sheet_name]

    if column_name not in df.columns:
        raise HTTPException(status_code=404, detail=f"La columna '{column_name}' no se encontró.")

    unique_values = df[column_name].unique().tolist()
    unique_values = [v for v in unique_values if pd.notna(v) and v != '']
    unique_values.sort()
    return {"staff_names": unique_values}

# --- Endpoints NUEVOS para CRUD ---

@app.post("/api/data/{sheet}")
async def add_row(sheet: str, row: Dict[str, Any]):
    sheets = read_excel_sheets()
    if sheet not in sheets:
        raise HTTPException(status_code=404, detail=f"La hoja '{sheet}' no se encontró.")
    
    df = sheets[sheet]
    new_row_df = pd.DataFrame([row])
    df = pd.concat([df, new_row_df], ignore_index=True)
    
    sheets[sheet] = df
    write_excel_sheets(sheets)
    
    return {"message": "Fila añadida correctamente."}

@app.put("/api/data/{sheet}/{row_index}")
async def update_row(sheet: str, row_index: int, row: Dict[str, Any]):
    sheets = read_excel_sheets()
    if sheet not in sheets:
        raise HTTPException(status_code=404, detail=f"La hoja '{sheet}' no se encontró.")

    df = sheets[sheet]
    if row_index < 0 or row_index >= len(df):
        raise HTTPException(status_code=404, detail="Índice de fila fuera de rango.")

    for col, value in row.items():
        if col in df.columns:
            df.at[row_index, col] = value

    sheets[sheet] = df
    write_excel_sheets(sheets)

    return {"message": "Fila actualizada correctamente."}

@app.delete("/api/data/{sheet}/{row_index}")
async def delete_row(sheet: str, row_index: int):
    sheets = read_excel_sheets()
    if sheet not in sheets:
        raise HTTPException(status_code=404, detail=f"La hoja '{sheet}' no se encontró.")

    df = sheets[sheet]
    if row_index < 0 or row_index >= len(df):
        raise HTTPException(status_code=404, detail="Índice de fila fuera de rango.")

    df = df.drop(df.index[row_index]).reset_index(drop=True)

    sheets[sheet] = df
    write_excel_sheets(sheets)

    return {"message": "Fila eliminada correctamente."}