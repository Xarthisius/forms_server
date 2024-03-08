import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/form":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "http://localhost:3000")
            self.end_headers()
            with open("schema.json", "r") as file:
                schema = json.load(file)
            self.wfile.write(json.dumps(schema).encode())
        elif self.path == "/ui":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "http://localhost:3000")
            self.end_headers()
            with open("uischema.json", "r") as file:
                uischema = json.load(file)
            self.wfile.write(json.dumps(uischema).encode())
        else:
            self.send_response(404)
            self.end_headers()


def run_server():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()


run_server()
