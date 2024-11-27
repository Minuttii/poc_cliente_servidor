import socket
import json
from handlers import processar_requisicao

class Servidor:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def iniciar(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Servidor iniciado em {self.host}:{self.port}")
            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Conexão estabelecida com {addr}")
                    dados = conn.recv(1024)
                    if dados:
                        requisicao = json.loads(dados.decode('utf-8'))
                        resposta = processar_requisicao(requisicao)
                        conn.sendall(json.dumps(resposta).encode('utf-8'))

if __name__ == "__main__":
    servidor = Servidor("localhost", 5000)
    servidor.iniciar()
