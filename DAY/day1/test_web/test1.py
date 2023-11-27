from http.server import HTTPServer, BaseHTTPRequestHandler
from DAY.day1.test_web.main import *

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		# self.wfile.write(bytes(Message(), 'gbk'))
		self.wfile.write(bytes(edit(), 'gbk'))

def run(server_class=HTTPServer, handler_class=RequestHandler):
	server_address = ('', 8000)
	httpd = server_class(server_address, handler_class)
	print('Starting httpd...')
	httpd.serve_forever()

if __name__ == '__main__':
	run()