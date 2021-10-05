from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from time import sleep
import threading
from urllib.parse import urlparse, unquote_plus, parse_qs
import main

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if 'output' in self.path:
                #Handle output
                rq_url = urlparse(self.path)
                rq_param = parse_qs(rq_url.query)
                print()
                for i in rq_param['q']:
                    print(i.strip())
                self.send_response(200)                        
                self.end_headers()
                self.wfile.write(main.cmd.encode())
                return    
        except:
            None
        while main.cmd == '':
            sleep(.25)
        self.send_response(200)                        
        self.end_headers()
        self.wfile.write(main.cmd.encode())
        main.cmd = ''

    def log_message(self, format, *args):
        return    

class THreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    http =THreadingSimpleServer( ('127.0.0.1', 80), Handler)
    http.serve_forever()


