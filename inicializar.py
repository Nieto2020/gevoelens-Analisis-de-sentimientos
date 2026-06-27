import json
import os
from datetime import datetime

ARCHIVO_DATA = "historial.json"

def inicializar_json():
    if not os.path.exists(ARCHIVO_DATA):
        try:
            with open(ARCHIVO_DATA, 'w', enconding='utf-8') as file:
                json.dump([], file)
            print(f"[INFO] Archivo {ARCHIVO_DATA} creado exitosamente.")
        except IOError as e:
            print(f"[ERROR] No se pudo crear el archivo: {e}")
            
            
def guardar_analisis(texto_original, sentimento, score):
    
    inicializar_json()
    
    try:
        with open(ARCHIVO_DATA, 'r', encoding='utf8') as file:
            historial = json.load(file)
    except (json.JSONDecodeError, IOError):
        historial = []
        
    nuevo_id = len(historial) + 1
    timestamp_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    nuevo_registro = {
        "id" : nuevo_id,
        "" :
    }