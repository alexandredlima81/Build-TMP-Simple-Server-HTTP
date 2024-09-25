# Importação dos módulos necessários
import http.server
import socketserver
import os
import logging

# Configurações de logging
log_file_path = '/files/weblog'  # Caminho para o arquivo de log
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')

PORT = 8000  # Porta do servidor

# Definindo o handler para o servidor HTTP
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        # Loga no arquivo
        logging.info("%s - - [%s] %s\n" % (self.client_address[0], self.log_date_time_string(), format % args))
        # Também imprime no terminal
        print("%s - - [%s] %s" % (self.client_address[0], self.log_date_time_string(), format % args))

# Define o diretório de trabalho
os.chdir('/files')  # Diretório onde o servidor irá servir os arquivos

# Cria o servidor HTTP
handler_object = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print(f"Serving at port {PORT}")
    print("Server is running. Press Ctrl+C to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    print("Server stopped.")
    httpd.server_close()
    print("Server closed.")
