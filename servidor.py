from http.server import *
import urllib.parse
import json

from inicializar import ARCHIVO_DATA, inicializador_json, limpieza, scoring, guardar_analisis

PUERTO = 8080

class AnalizadorServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        if self.path == '/':
            # 1. Indicamos al navegador que la respuesta fue exitosa (200 OK)
            self.send_response(200)
            self.send_header('content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            # 2. Leemos archivo HTML de diseño
            with open('index.html', 'r', encoding='utf-8') as file:
                html_contenido = file.read()
                
            # 3. Leemos el JSON para contruir las filas de la tabla
            inicializador_json() # Aseguramos que exista
            with open(ARCHIVO_DATA, 'r', encoding='utf-8') as file:
                historial = json.load(file)
                
            # 4. Generamos el bloque de texto HTML dinámicamente
            filas_html = ""
            for registro in historial:
                filas_html += f"""
                <tr>
                    <td>{registro['id']}</td>
                    <td>{registro['text_input']}</td>
                    <td>{registro['sentiment']}</td>
                    <td>{registro['timestamp']}</td>
                </tr>
                """
                
            # 5. REEMPLAZAMOS puntaje de anclaje con las filas reales
            html_final = html_contenido.replace('', filas_html)
            
            # 6. Enviamos el HTML final modificado al navegador
            self.write(html_final.encode('utf-8'))
        
        else:
            # Si intentan entrar a otra ruta (ej. /secreta), mandamos un 404 Not Found
            self.send_error(404, "pagina no encontrada")
    
    def do_POST(self):
        # Recibir, procesar y guardar
        if self.path == '/':
            # 1. Averiguamos cuántos bytes de información nos envió el formulario
            longitud_datos = int(self.headers['Content-Length'])
            # 2. Leemos esos bytes crudos del flujo de entrada
            datos_crudos = self.rfile.read(longitud_datos).decode('utf-8')
            # 3. Decodificmos el formato del forulario (comentario=Texto+Ingresado)
            datos_parseados = urllib.parse.parse_qs(datos_crudos)
            # Obtenemos el valor de la llave 'comentario que definimos en el HTML
            texto_usuario = datos_parseados['comentario'[0]]
            # 4. LOGICA
            list = limpieza(texto_usuario)
            sentiment, score = scoring(list)
            # 5. Guardar analisis
            guardar_analisis(texto_usuario, score, sentiment)
            
            # 6. Redirección (HTTP 303): DEcimos al navegador que regrese a la raíz con un GET
            self.send_response(303)
            self.send_header('Location', '/')
            self.send_headers()
            
# --- ARRANQUE DEL SERVIDOR ---
if __name__ == '__main__':
    servidor = HTTPServer(('localhost', PUERTO), AnalizadorServer)
    print(f"[SERVIDOR ACTIVO] Servidor corriendo en http://localhost:{PUERTO}")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("n\[SERVIDOR DETENIDO] Apagando el sistema elgantemente.")
        servidor.server_close()

port = HTTPServer(('', 8080), GFG)

port.serve_forever()