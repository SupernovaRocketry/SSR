from cliente import Cliente
from grafico2d import Grafico2d

from mainWidget import *
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.config import Config



class MainApp(App):
    """
    Aplicativo Basico Kivy
    """

    def build(self):
        """
        Método que gera o aplicativo com o widget principal
        """
        self._widget = MainWidget()
        return self._widget


if __name__ == '__main__':
    Builder.load_string(
        open('mainWidget.kv', encoding='utf8').read(), rulesonly=True)
    MainApp().run()


# c = Grafico2d('localhost', 9000)

# c = Cliente('localhost', 9000)
# c.start()
