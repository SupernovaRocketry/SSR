from kivy.uix.behaviors import button
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MainWidget(BoxLayout):
    def incrementar(self):
        self.ids['lb'].text = str(int(self.ids['lb'].text)+1)

    pass