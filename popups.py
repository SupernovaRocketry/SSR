from kivy.uix.popup import Popup

class ConnectSocketPopup(Popup):
    '''
    Popup para fazer a conexão socket.
    '''
    def __init__(self, server_ip, server_port, **kwargs):
        '''
        Construtor da classe connectSocket
        '''
        super().__init__(**kwargs)
        self.ids.txt_ip.text = str(server_ip)
        self.ids.txt_port.text = str(server_port)
    pass