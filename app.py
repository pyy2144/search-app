"""Minimal server for local testing. Not needed after deploying to static hosting."""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import sys

os.chdir(os.path.join(os.path.dirname(__file__), 'static'))

port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
print(f'  Local:  http://localhost:{port}')
print(f'  Mobile: http://<your-ip>:{port}')
server.serve_forever()
