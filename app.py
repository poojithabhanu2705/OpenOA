from http.server import BaseHTTPRequestHandler, HTTPServer
import openoa

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OpenOA deployed successfully!")

PORT = 10000

print("Starting server on port", PORT)
HTTPServer(("", PORT), Handler).serve_forever()