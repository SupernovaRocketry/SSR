from kivy.uix.behaviors import button
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


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


    pass