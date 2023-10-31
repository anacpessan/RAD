import http.server
import socketserver
import webbrowser

# Defina a porta na qual você deseja executar o servidor
port = 8000

# Crie um manipulador de servidor para servir os arquivos HTML/CSS
handler = http.server.SimpleHTTPRequestHandler

# Inicialize o servidor na porta especificada
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Servidor rodando na porta {port}")
    webbrowser.open(f'http://localhost:{port}')  # Abre o site no navegador
    httpd.serve_forever()
