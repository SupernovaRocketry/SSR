import matplotlib.pyplot as plt
import numpy as np
from plotly import graph_objects as go
import matplotlib.animation as animation
from cliente import Cliente

class Grafico2d():
    """
    Classe destinada ao plot em tempo real da altitude do foguete.
    """

    def __init__(self, server_ip, port):
        """
        Construtor da classe Grafico2d
        :param server_ip: ip do servidor
        :param port: porta do servidor
        """
        self.__getDados = Cliente(server_ip, port)
        self.__xs = []
        self.__ys = []  


    def _animate(self):
        self._fig = go.Figure()

        self.__xs.append(self.__getDados._resp['Altitude'])
        self.__ys.append(self.__getDados._resp['Altitude'])

        # Limit x and y lists to 20 items
        self.__xs = self.__xs[-20:]
        self.__ys = self.__ys[-20:]

        # Draw x and y lists
        self._fig.add_trace(go.Scatter(x = self.__xs, y = self.__ys))

        self._fig.update_layout(
            title="Altitude foguete",
            xaxis_title="tempo (s)",
            yaxis_title="Altitude"
            )   


    def _plotarGrafico(self):
        ani = animation.FuncAnimation(self._fig, self._animate(), fargs=(self.__xs, self.__ys), interval=1000)
        plt.show()

        
        

