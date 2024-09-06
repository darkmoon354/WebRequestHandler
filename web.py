from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

class WebRequestHandler(BaseHTTPRequestHandler):
    # PAGINA DINAMICA
    contenidos = {
        '/proyecto/web-uno': """
<html>
  <h1>Proyecto: web-uno</h1>
</html>""",
        '/proyecto/web-dos': """
<html>
  <h1>Proyecto: web-dos</h1>
</html>""",
        '/proyecto/web-tres': """
<html>
  <h1>Proyecto: web-tres</h1>
</html>""",
    }

    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        if self.path == '/':
            # Lee el contenido de home.page
            contenido = self.load_home_html()
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(contenido.encode('utf-8'))
        elif self.path in self.contenidos:
            # Devolver el contenido del diccionario para otras rutas
            contenido = self.contenidos[self.path]
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(contenido.encode('utf-8'))
        else:
            # Ruta no encontrada, devolver un error 404
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(self.get_404_response().encode('utf-8'))

    def load_home_html(self):
        """Carga el contenido del archivo home.html."""
        with open('home.html', 'r', encoding='utf-8') as file:
            return file.read()

    def get_404_response(self):
        """Genera una respuesta HTML para un error 404."""
        return "<h1>404 Not Found</h1><p>The requested URL was not found on this server.</p>"
  #inicio de servidor y cambio de puerto. 
if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
