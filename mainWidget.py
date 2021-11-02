from kivy.uix.behaviors import button
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from popups import ConnectSocketPopup
from timeseriesgraph import TimeSeriesGraph
from kivy_garden.graph import LinePlot
from cliente import Cliente
from threading import Thread
from time import sleep

class MainWidget(FloatLayout):
    '''
    Widget principal do supervisório
    '''
    _updateWidgets = True

    def __init__(self, **kwargs):
        '''
        Construtor do widget principal
        '''
        super().__init__()
        self._login = ""
        self._senha = ""
        self._serverIP = kwargs.get('server_ip')
        self._port = kwargs.get('server_port')
        self._conn = ConnectSocketPopup(self._serverIP, self._port)
        
        # self._connect.start()
        Window.fullscreen = False
        Window.maximize()

        
        #self._graphAltitude = DataGraph(20)

    pass

    def startDataRead(self, ip, port):
        """
        Método utilizado para configurar a conexão socket e inicializar uma thread para a leitura dos dados e atualização da interface grafica
        :param ip: ip da conexão socket
        :param port: porta para a conexao socket
        """
        self._serverIP = ip
        self._serverPort = port
        if self._login == 'supernova' and self._senha == 'astra':
            try:
                Window.set_system_cursor("wait")
                self._connect = Cliente(self._serverIP, self._port)
                self._connect.start()
                Window.set_system_cursor("arrow")
                self._updateThread = Thread(target = self.updater)
                self._updateThread.start()
                self.ids.imagem_conexao.background_normal = 'imgs/conectado.png'
                self._conn.dismiss()
            except:
                print("Falha ao inicinar startDataRead")
        else:
            print("Senha invalida!")

    
    def updater(self):
        """
        Metodo que invoca as rotinas de leitura de dados, utilizando a interface e inserção dos dados no banco de dados
        """
        try:
            while self._updateWidgets:
                #ler dados
                #atualizar a interface
                #insedir os dados no banco de dados

                #Le dados
                self._instDados = self._connect._method()

                # Atualiza dados
                self._updateGUI()


                sleep(.1)
        except Exception as e:
            print(f'Erro: {e}')

    
    def readData(self):
        """
        Método para a leitura de dados via socket
        """

    def _updateGUI(self):
        """
        Método para a atualização dos da interface gráfica
        """
        self.ids.altitude.text = str(self._instDados['Altitude'])
        self.ids.latitude.text = str(self._instDados['Latitude'])
        self.ids.longitude.text = str(self._instDados['Longitude'])
        self.ids.acelerometroX.text = str("{:.2f}".format(self._instDados['Acelerometro']['x']))
        self.ids.acelerometroY.text = str("{:.2f}".format(self._instDados['Acelerometro']['y']))
        self.ids.acelerometroZ.text = str("{:.1f}".format(self._instDados['Acelerometro']['z']))
        self.ids.giroscopioX.text = str(int(self._instDados['Giroscopio']['x']))
        self.ids.giroscopioY.text = str(int(self._instDados['Giroscopio']['y']))
        self.ids.giroscopioZ.text = str(int(self._instDados['Giroscopio']['z']))
        self.ids.mapa.lat = float(self._instDados['Latitude'])
        self.ids.mapa.lon = float(self._instDados['Longitude'])







class DataGraph(FloatLayout):
    def __init__ (self, xmax, **kwargs):
        super().__init__(**kwargs)
        self.plot = LinePlot(line_width = 1.5, color = '#7D0101')
        self.ids.graphAltitude.add_plot(self.plot)
        self.ids.graphAltitude.xmax = xmax