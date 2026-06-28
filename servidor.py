import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

http = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
http.serve_forever()