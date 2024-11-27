import socket
import json

class Cliente:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def enviar_requisicao(self, action: str, parameters: dict):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            mensagem = json.dumps({"action": action, "parameters": parameters})
            s.sendall(mensagem.encode('utf-8'))
            resposta = s.recv(1024)
            return json.loads(resposta.decode('utf-8'))

if __name__ == "__main__":
    cliente = Cliente("localhost", 5000)
    resposta = cliente.enviar_requisicao("soma", {"a": 10, "b": 20})
    print("Resposta do servidor:", resposta)
