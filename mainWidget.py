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

class MainWidget(FloatLayout):
    '''
    Widget principal do supervisório
    '''

    def __init__(self, **kwargs):
        '''
        Construtor do widget principal
        '''
        super().__init__()
        self._login = ""
        self._senha = ""
        self._serverIP = kwargs.get('server_ip')
        self._port = kwargs.get('server_port')
        Window.fullscreen = False
        Window.maximize()

        self._conn = ConnectSocketPopup(self._serverIP, self._port)
        #self._graphAltitude = DataGraph(20)

    pass

class DataGraph(FloatLayout):
    def __init__ (self, xmax, **kwargs):
        super().__init__(**kwargs)
        self.plot = LinePlot(line_width = 1.5, color = '#7D0101')
        self.ids.graphAltitude.add_plot(self.plot)
        self.ids.graphAltitude.xmax = xmax