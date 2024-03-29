import socket
import json
from time import sleep
from datetime import datetime

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
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        


    def start(self):
        """
        Método que inicializa a execução do cliente
        """
        endpoint = (self._serverIP, self._port)
        try:
            self._tcp.connect(endpoint)
            print("Conexao realiza com sucesso.")
            # self._method()
        except Exception as e:
            print(f'Erro ao conectar {e.args}')
            raise e


    def _method(self):
        """
        Método que implementa as requisições do cliente e a IHM
        """
        try:
            msg = 'y'
            self._tcp.send(msg.encode())
            self._resp = self._tcp.recv(1024)
            self._resp = self._resp.decode()
            self._resp = eval(self._resp)
            self._resp['timestamp'] = datetime.now()
        except Exception as e:
            print(f'Erro ao realizar a comunicacao com o servidor {e.args}')
            raise e

        return self._resp

    def disconect(self):
        self._tcp.close()
        print("Desconectar!")

        

# class WiFi():
#     """
#     Classe WiFI - Supervisório Supernova Rocketry - Comunicação WiFi
#     """
#     def __init__(self):
        