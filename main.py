from cliente import Cliente
from grafico2d import Grafico2d

from kivy.uix.behaviors import button
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class BasicApp(App):
    """
    Aplicativo Basico Kivy
    """
    def build(self):
        """
        Construir o aplicativo 
        """
        layout = BoxLayout(orientation = 'vertical')
        lb = Label(text = 'label 1')
        bt = Button(text = "Botão 1")
        layout.add_widget(bt)
        layout.add_widget(lb)
        layout2 = BoxLayout(orientation = 'horizontal')
        lb2 = Label(text= 'label 2')
        lb3 = Label(text = 'label 3')
        layout2.add_widget(lb2)
        layout2.add_widget(lb3)
        layout.add_widget(layout2)
        return layout

if __name__ == '__main__':
    BasicApp().run()


c = Grafico2d('localhost', 9000)

#c = Cliente('localhost', 9000)
#c.start()