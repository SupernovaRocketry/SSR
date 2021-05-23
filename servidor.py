import socket # Biblioteca responsavel pela comunicação socket
import json   # Biblioteca usada para envio de Json
import random # Gerador de numeros aletorios para os dados

class Servidor():
    """
    Classe servidor - Simulador de dados de voo de um minifogute - API Socket
    """

    def __init__(self, host, port):
        """
        Construtor da classe Servidor
        """
        self._host = host
        self._port = port
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """
        Inicia a execução do serviço
        """
        endpoint = (self._host, self._port)
        try:
            self._tcp.bind(endpoint)
            self._tcp.listen(1)
            print(f'Servidor foi iniciado em {self._host}:{self._port}')
            while True:
                con, client = self._tcp.accept()
                self._service(con, client)
        except Exception as e:
            print(f"Erro ao inicializar o servidor: {e.args}")

    def _service(self, con, client):
        """
        Metodo que implementa o serviçõ de simulador de dados de voo
        :param con: objeto socket utilizado para enviar e receber os dados
        :param client: é o endereço e porta do cliente
        """
        # Gerando lista de dados
        self._altitude = [x for x in range(3000)] + [3000-x for x in range(3000)] # Simulando dados de altitude entre 0 e 3000.
        self._latitude = [10+random.randrange(-2,2) for x in range(6000)]         # Simulando dados de latitude entre 8 e 12.
        self._longitude = [20+random.randrange(-4,4) for x in range(6000)]        # Simulando dados de longitude entre 16 e 24.
        self._acionamentoPPE = [0]*2999 + [1] + [0]*3000                          # Simulando a confirmação do acionamento principal do paraquedas estabilizador
        self._acionamentoRPE = [0]*3004 + [1] + [0]*2995                          # Simulando a confirmação do acionamento redundante do paraquedas estabilizador
        self._acionamentoPPP = [0]*3449 + [1] + [0]*2500                          # Simulando a confirmação do acionamento principal do paraquedas principal
        self._acX = [2+random.randrange(-.2, .2) for x in range(6000)]            # Simulando a aceleração no eixo x
        self._acY = [3+random.randrange(-.3, .3) for x in range(6000)]            # Simulnado a aceleração no eixo y
        self._acZ = [50+random.randrange(-5, 5) for x in range(6000)]             # Simulando a aceleração no eixo z
        self._gyX = [100+random.randrange(-10,10) for x in range(6000)]           # Simulando a angulação no eixo x
        self._gyY = [300+random.randrange(-30,30) for x in range(6000)]           # Simulando a angulação no eixo y
        self._gyZ = [700+random.randrange(-15,15) for x in range(6000)]           # Simulando a angulação no eixo z


        #Serviço de simulador de dados. 
        print(f'Atendendo cliente {client}')
        try:
            msg = con.recv(1024)
            if str(msg.decode('ascii')) == 'y':
                for i in range(len(self._altitude)):
                    self._data = {"Altitude" : self._altitude[i],
                                  "Latitude" : self._latitude[i],
                                  "Longitude" : self._longitude[i],
                                  "Principal Paraquedas Estabilizador" : self._acionamentoPPE[i],
                                  "Redundancia Paraquedas Estabilizador" : self._acionamentoPPP[i],
                                  "Acelerometro" : {"x" : self._acX[i] , "y" : self._acY[i] , "z" : self._acZ[i]},
                                  "Giroscopio" : {"x" : self._gyX[i] , "y" : self._gyY[i] , "z" : self._gyZ[i]}
                                 }
                    self._data = json.dumps(self._data)
                    self._tcp.send(self._data.encode())
                    print("Dados enviados.")
        except OSError as e:
            print(f'Erro na conexao {client} : {e.args}')
            return
        except Exception as e:
            print(f'Erro na palavra de conexao recebida do client {client} : {e.args}')
                    

