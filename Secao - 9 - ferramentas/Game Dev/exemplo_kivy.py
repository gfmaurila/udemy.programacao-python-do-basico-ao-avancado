
# Exemplo básico com Kivy
from kivy.app import App
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        return Label(text="Olá, Kivy!")

MeuApp().run()
