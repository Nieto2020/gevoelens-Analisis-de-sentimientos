"""Gevoelens - Análisis de sentimiento.

Módulo único de lógica de negocio:
- Limpieza y tokenización de texto (limpieza).
- Clasificación de sentimiento por lexicón (scoring).
- Persistencia del historial en JSON (inicializar_json, guardar_analisis).
"""

import json
import os
import re
from datetime import datetime

ARCHIVO_DATA = "historial.json"

# Lexicón de sentimiento (punto único de verdad)
POSITIVE_LIST = ["good", "nice", "awesome", "genius", "fun", "amazing"]
NEGATIVE_LIST = ["bad", "horrible", "boring", "terrible", "awful", "shit"]


def inicializar_json():
    if not os.path.exists(ARCHIVO_DATA):
        try:
            with open(ARCHIVO_DATA, 'w', encoding='utf-8') as file:
                json.dump([], file)
            print(f"[INFO] Archivo {ARCHIVO_DATA} creado exitosamente.")
        except IOError as e:
            print(f"[ERROR] No se pudo crear el archivo: {e}")
 
def limpieza(comment):
    """Normaliza el texto y devuelve una lista de palabras individuales."""
    if not isinstance(comment, str) or not (len(comment) > 5 and len(comment) <= 100):
        raise ValueError("Longitud no aceptada (debe tener entre 6 y 100 caracteres).")
    comment = comment.lower()
    comment = re.sub(r"[-_?¿!¡,.#$%&/()']", " ", comment)
    return comment.split()

def scoring(palabras):
    positive_score = 0
    negative_score = 0
    score = 0
    for word in palabras:
        if word in POSITIVE_LIST:
            positive_score += 1
        elif word in NEGATIVE_LIST:
            negative_score += 1
    score = positive_score - negative_score
    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, score

def guardar_analisis(texto_original, sentiment, score):
    
    inicializar_json()
    
    try:
        with open(ARCHIVO_DATA, 'r', encoding='utf8') as file:
            historial = json.load(file)
    except (json.JSONDecodeError, IOError):
        historial = []
        
    nuevo_id = len(historial) + 1
    timestamp_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
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
        print(f"[EXITO] Registro #{nuevo_id} guardado correctamente.")
    except IOError as e:
        print(f"[ERROR] No se pudieron escribir los datos en el archivo: {e}")