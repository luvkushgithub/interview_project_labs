import  http.server
import  socketserver 

PORT = 8000 

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("0.0.0.0",PORT)),Handler) as https:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
