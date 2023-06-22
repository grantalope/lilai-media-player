from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode())

        character_name = data.get('character_name', [''])[0]
        text = data.get('text', [''])[0]

        # your existing code here, using character_name and text as inputs

        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"{character_name} audio generated successfully.".encode())
        return
