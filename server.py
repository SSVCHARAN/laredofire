import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = '/home/ssvcharan/Antigravity/LaredoFire'

class SafeHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(('0.0.0.0', PORT), SafeHandler) as httpd:
        print(f'Server running live on http://localhost:{PORT}/')
        httpd.serve_forever()
