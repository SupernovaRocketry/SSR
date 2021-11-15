from cliente import Cliente
from grafico2d import Grafico2d

from mainWidget import *
from kivy.app import App
from kivy.lang.builder import Builder




class MainApp(App):
    """
    Aplicativo Basico Kivy
    """

    def build(self):
        """
        Método que gera o aplicativo com o widget principal
        """
        self._widget = MainWidget(server_ip = "127.0.0.1", server_port = 9000)
        return self._widget

    def on_stop(self):
        """
        Método que fecha toda a aplicação
        """
        self._widget.stopRefresh()


if __name__ == '__main__':
    Builder.load_string(open('mainWidget.kv', encoding='utf8').read(), rulesonly=True)
    Builder.load_string(open('popups.kv', encoding='utf8').read(), rulesonly=True)
    MainApp().run()


# c = Grafico2d('localhost', 9000)

# c = Cliente('localhost', 9000)
# c.start()
