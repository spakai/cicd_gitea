"""Minimal HTTP server exposing a Fibonacci endpoint."""

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

from .core import fibonacci


class FibRequestHandler(BaseHTTPRequestHandler):
    """Handle GET requests for Fibonacci numbers."""

    def do_GET(self) -> None:  # noqa: N802 (for method name; though no flake8 here)
        parsed = urlparse(self.path)
        if parsed.path != "/fib/":
            self.send_error(404)
            return

        params = parse_qs(parsed.query)
        if "n" not in params:
            self.send_error(400, "missing n parameter")
            return
        try:
            n = int(params["n"][0])
            value = fibonacci(n)
        except (ValueError, TypeError):
            self.send_error(400, "invalid n parameter")
            return

        body = json.dumps({"n": n, "value": value}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def run(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Run the HTTP server."""
    server = HTTPServer((host, port), FibRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
