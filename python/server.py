from http.server import HTTPServer, BaseHTTPRequestHandler
import codecs
import base64 
import unicodedata

BIND_HOST = 'localhost'
PORT = 7878


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
     def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'')

    def do_POST(self):
        content_length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        res=body.decode('utf-8')
        print(res)
        res=res.replace(' ','')
        res=res.replace('0x','')
        hexa = codecs.decode(res, "hex")
        print(hexa)
        basix=base64.b64decode(hexa)
        print(basix)
        asc = basix.decode('unicode_escape')
        print(asc)
        data = unicodedata.normalize('NFKD', asc).encode('ascii', 'ignore')
        print(data)


print(f'Listening on http://{BIND_HOST}:{PORT}\n')
httpd = HTTPServer((BIND_HOST, PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
