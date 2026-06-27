import json
import os
import clean, score_sent
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
            
            
def guardar_analisis(texto_original, sentiment, score):
    
    inicializar_json()
    
    try:
        with open(ARCHIVO_DATA, 'r', encoding='utf8') as file:
            historial = json.load(file)
    except (json.JSONDecodeError, IOError):
        historial = []
        
    nuevo_id = len(historial) + 1
    timestamp_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    texto_limpio = clean.limpieza(texto_original)
    sentiment, score = score_sent.analizar_sentimiento(texto_limpio)
    
    
    nuevo_registro = {
        "id"         : nuevo_id,
        "text_input" : texto_original,
        "sentiment"  : sentiment,
        "score"      : score,
        "timestamp"  : timestamp_actual
    }
    
    historial.append(nuevo_registro)
    
    try:
        with open(ARCHIVO_DATA, 'w', encoding='utf-8') as file:
            json.dump(historial, file, indent=4, ensure_ascii=False)
        print(f"[EXITO] Reegistro #{nuevo_id} guardado correctamente.")
    except IOError as e:
        print(f"[ERROR] No se pudieron escribir los daros en el archivo: {e}")