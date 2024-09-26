import http.server
import socketserver

PORT = 8080

# إعداد معالج لتقديم الملفات الثابتة (مثل HTML, CSS, JavaScript)
Handler = http.server.SimpleHTTPRequestHandler

# بدء الخادم
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever() 
