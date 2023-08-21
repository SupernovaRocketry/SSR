from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

# class ConnectSocketPopup(Popup):
#     '''
#     Popup para fazer a conexão socket.
#     '''
#     def __init__(self, server_ip, server_port, **kwargs):
#         '''
#         Construtor da classe connectSocket
#         '''
#         super().__init__(**kwargs)
#         self.ids.txt_ip.text = str(server_ip)
#         self.ids.txt_port.text = str(server_port)
#     pass

class ConnectSocketPopup(Popup):
    '''
    Popup para fazer a conexão - (UART, WiFi)
    '''
    def __init__(self, server_ip, server_port, **kwargs):
        '''
        Construtor da classe connectSocket
        '''
        super().__init__(**kwargs)      
        self.manager = ScreenManager()
        self.manager.add_widget(UARTConnection(name='UART'))
        self.manager.add_widget(WiFiConnection(name='WiFiConnection'))


class ConnectSocketPopupError(Popup):
    """
        Popup de error de ConnectSocketPopup
        """
    def __init__(self, **kwargs):        
        super().__init__(**kwargs)
    pass

class ConfiguraGraficosPopup(Popup):
    """
    Popup para fazer a configuração dos graficos
    """
    def __init__(self, **kwargs):
        """
        Construtor da classe ConfiguraGraficosPopup
        """
        super().__init__(**kwargs)
        
class UARTConnection(Screen):
    pass

class WiFiConnection(Screen):
    pass