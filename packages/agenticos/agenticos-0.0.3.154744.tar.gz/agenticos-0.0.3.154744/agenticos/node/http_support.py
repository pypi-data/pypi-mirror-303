import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

log = logging.getLogger(__name__)

class HTTPHealthEndpoint(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "ok"}')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")

class HTTPHealthServer(Thread):
    def __init__(self, port: int):
        super().__init__()
        self.port = port

    def run(self):
        self.server = HTTPServer(("localhost", self.port), HTTPHealthEndpoint)
        log.info(f"Starting health server on port {self.port}")
        self.server.serve_forever()
        log.info("Health server stopped")


    def stop(self):
        log.debug("Health server stop requested")
        self.server.shutdown()
