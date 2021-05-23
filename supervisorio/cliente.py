import socket
import json

class Cliente():
    """
    Classe Cliente - Supervisorio Supernova Rocketry - API Socket
    """

    def __init__(self, server_ip, port):
        """
        Construtor da classe cliente
        :param server_ip: ip do servidor
        :param port: porta do servidor
        """
        self._serverIP = server_ip
        self._port = port
        self._tcp = socket.socket(socket.AF_inet, socket.SOCK_STREAM)        


    def start(self):
        """
        Método que inicializa a execução do cliente
        """
        endpoint = (self.__serverIP, self.__port)
        try:
            self._tcp.connect(endpoint)
            print("Conexao realiza com sucesso.")
            self._method()
        except Exception as e:
            print(f'Erro ao conectar {e.args}')

    def _method(self):
        """
        Método que implementa as requisições do cliente e a IHM
        """
        try:
            msg=''
            while msg != 'x':
                msg = input("Digite a mensagem a ser enviada (x para sair): ")
                self._tcp.send(msg.encode())
                resp = self._tcp.recv(1024)
                print(resp.decode())
            self._tcp.close()
        except Exception as e:
            print(f'Erro ao realizar a comunicacao com o servidor {e.args}')