from kivy.uix.behaviors import button
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from popups import connectSocket
from timeseriesgraph import TimeSeriesGraph
from kivy_garden.graph import LinePlot

class MainWidget(FloatLayout):
    '''
    Widget principal do supervisório
    '''

    def __init__(self, **kwargs):
        '''
        Construtor do widget principal
        '''
        super().__init__(**kwargs)
        self._login = kwargs.get('login')
        self._senha = kwargs.get('senha')
        Window.fullscreen = False
        Window.maximize()

        self._conn = connectSocket()
        #self._graphAltitude = DataGraph(20)

    pass

class DataGraph(FloatLayout):
    def __init__ (self, xmax, **kwargs):
        super().__init__(**kwargs)
        self.plot = LinePlot(line_width = 1.5, color = '#7D0101')
        self.ids.graphAltitude.add_plot(self.plot)
        self.ids.graphAltitude.xmax = xmax